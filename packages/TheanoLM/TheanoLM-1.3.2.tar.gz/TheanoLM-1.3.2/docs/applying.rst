Applying a language model
=========================

Scoring a text corpus
---------------------

``theanolm score`` command can be used to compute the perplexity of evaluation
data, or to rescore an n-best list by computing the probability of each
sentence. It takes two positional arguments. These specify the path to the
TheanoLM model and the text to be evaluated. Evaluation data is processed
identically to training and validation data, i.e. explicit start-of-sentence and
end-of-sentence tags are not needed in the beginning and end of each utterance,
except when one wants to compute the probability of the empty sentence
``<s> </s>``.

What the command prints can be controlled by the ``--output`` parameter. The
value can be one of:

perplexity
  Compute perplexity and other statistics of the entire corpus.

word-scores
  Display log probability scores of each word, in addition to sentence and
  corpus perplexities.

utterance-scores
  Write just the log probability score of each utterance, one per line. This can
  be used for rescoring n-best lists.

The easiest way to evaluate a model is to compute the perplexity of the model on
evaluation data, lower perplexity meaning a better match. Note that perplexity
values are meaningful to compare only when the vocabularies are identical. If
you want to compare perplexities with back-off model perplexities computed e.g.
using `SRILM <http://www.speech.sri.com/projects/srilm/>`_, note that SRILM
ignores OOV words when computing the perplexity. You get the same behaviour from
TheanoLM, if you use ``--exclude-unk``. TheanoLM includes sentence end tokens
in the perplexity computation, so you should look at the ``ppl`` value from
SRILM output. The example below shows how one can compute the perplexity of a
model on evaluation data, while ignoring OOV words::

    theanolm score model.h5 test-data.txt --output perplexity --exclude-unk

When the vocabulary of the neural network model is limited to a subset of the
words that occur in the training data (called *shortlist*), it is possible to
estimate the probability of the out-of-shortlist words using their unigram
frequencies in the training data. This approach is enabled using ``--shortlist``
argument, e.g.::

    theanolm score model.h5 test-data.txt --output perplexity --shortlist

The probability of the *<unk>* token is distributed among the out-of-shortlist
words that appear in the training data. Words that didn't appear in the training
data will be ignored. For this to work correctly, ``--exclude-unk`` shouldn't be
used when training the model.

Probabilities of individual words can be useful for debugging problems. The
``word-scores`` output can be compared to the ``-ppl -debug 2`` output of SRILM.
While the base chosen to represent log probabilities does not affect perplexity,
when comparing log probabilities, the same base has to be chosen. Internally
TheanoLM uses the natural logarithm, and by default also prints the log
probabilities in the natural base. SRILM prints base 10 log probabilities, so in
order to get comparable log probabilities, you should use ``--log-base 10`` with
TheanoLM. The example below shows how one can display individual word scores in
base 10::

    theanolm score model.h5 test-data.txt --output word-scores --log-base 10

Rescoring n-best lists
----------------------

A typical use of a neural network language model is to rescore n-best lists
generated during the first recognition pass. Often a word lattice that
represents the search space can be created as a by-product in an ASR decoder. An
n-best list can be decoded from a word lattice using lattice-tool from SRILM.
Normally there are many utterances, so the lattice files are listed in, say,
``lattices.txt``. The example below reads the lattices in HTK SLF format and
writes 100-best lists to the ``nbest`` directory::

    mkdir nbest
    lattice-tool -in-lattice-list lattices.txt -read-htk -nbest-decode 100 \
                 -out-nbest-dir nbest

It would be inefficient to call TheanoLM on each n-best list separately. A
better approach is to concatenate them into a single file and prefix each line
with the utterance ID::

    for gz_file in nbest/*.gz
    do
        utterance_id=$(basename "${gz_file}" .gz)
        zcat "${gz_file}" | sed "s/^/${utterance_id} /"
    done >nbest-all.txt

lattice-tool output includes the acoustic and language model scores. TheanoLM
needs only the sentences. You should use ``--log-base 10`` if you're rescoring
an n-best list generated using SRILM::

    cut -d' ' -f5- <nbest-all.txt >sentences.txt
    theanolm score model.h5 sentences.txt \
        --output-file scores.txt --output utterance-scores \
        --log-base 10

The resulting file ``scores.txt`` contains one log probability on each line.
These can be simply inserted into the original n-best list, or interpolated with
the original language model scores using some weight *lambda*::

    paste -d' ' scores.txt nbest-all.txt |
    awk -v "lambda=0.5" \
        '{ nnscore = $1; boscore = $4;
           $1 = ""; $4 = nnscore*lambda + boscore*(1-lambda);
           print }' |
    awk '{ $1=$1; print }' >nbest-interpolated.txt

The total score of a sentence can be computed by weighting the language model
scores with some value *lmscale* and adding the acoustic score. The best
sentences from each utterance are obtained by sorting by utterance ID and score,
and taking the first sentence of each utterance. The fields we have in the
n-best file are utterance ID, acoustic score, language model score, and number
of words::

    awk -v "lmscale=14.0" \
        '{ $2 = $2 + $3*lmscale; $3 = $4 = "";
           print }' <nbest-interpolated.txt |
    sort -k1,1 -k2,2gr |
    awk '$1 != id { id = $1; $2 = ""; print }' |
    awk '{ $1=$1; print }' >1best.ref

Decoding word lattices
----------------------

``theanolm decode`` command can be used to decode the best paths directly from
word lattices using neural network language model probabilities. This is more
efficient than creating an intermediate n-best list and rescoring every
sentence::

    theanolm decode model.h5 \
        --lattice-list lattices.txt --lattice-format slf \
        --output-file 1best.ref --output ref \
        --nnlm-weight 0.5 --lm-scale 14.0

The lattices may be in SLF format (originating from HTK recognizer) or text
CompactLattice format used by Kaldi recognizer. The format is selected using the
``--lattice-format`` argument (either "slf" or "kaldi"). With Kaldi format you
also have to provide a mapping from words to the word IDs used in the lattices,
using the ``--kaldi-vocabulary`` argument. Typically the file is called
"words.txt" and stored in the lang directory.

In principle, the context length is not limited in recurrent neural networks, so
an exhaustive search of word lattices would be too expensive. There are a number
of parameters that can be used to constrain the search space by pruning unlikely
tokens (partial hypotheses). These are:

--max-tokens-per-node : N
  Retain at most N tokens at each node. Limiting the number of tokens is very
  effective in cutting the computational cost. Higher values mean higher
  probability of finding the best path, but also higher computational cost. A
  good starting point is 64.

--beam : logprob
  Specifies the maximum log probability difference to the best token at a given
  time. Beam pruning starts to have effect when the beam is smaller than 1000,
  but the effect on word error rate is small before the beam is smaller than
  500.

--recombination-order : N
  When two tokens have identical history up to N previous words, keep only the
  best token. This means effectively that we assume that the influence of a word
  is limited to the probability of the next N words. Recombination seems to have
  little effect on word error rate before N is closer to 20.

--prune-relative : R
  If this argument is given, the ``--max-tokens-per-node`` and ``--beam``
  parameters will be adjusted relative to the number of tokens in each node.
  Those parameters will be divided by the number of tokens and multiplied by R.
  This is especially useful in cases such as character language models.

--abs-min-max-tokens : N
  Specifies a minimum value for the maximum number of tokens, when using
  ``--prune-relative``.

--abs-min-beam : logprob
  Specifies a minimum value for the beam, when using ``--prune-relative``.

The work can be divided to several jobs for a compute cluster, each processing
the same number of lattices. For example, the following SLURM job script would
create an array of 50 jobs. Each would run its own TheanoLM process and decode
its own set of lattices, limiting the number of tokens at each node to 10::

    #!/bin/sh
    #SBATCH --gres=gpu:1
    #SBATCH --array=0-49

    srun --gres=gpu:1 theanolm decode model.h5 \
        --lattice-list lattices.txt \
        --output-file "${SLURM_ARRAY_TASK_ID}.ref" --output ref \
        --nnlm-weight 0.5 --lm-scale 14.0 \
        --max-tokens-per-node 64 --beam 500 --recombination-order 20 \
        --num-jobs 50 --job "${SLURM_ARRAY_TASK_ID}"

When the vocabulary of the neural network model is limited, but the vocabulary
used to create the lattices is larger, the decoder needs to consider how to
score the out-of-vocabulary words. The frequency of the OOV words in the
training data may easily be so high that the model favors paths that contain
many OOV words. It may be better to penalize OOV words by manually setting their
log probability using the ``--unk-penalty`` argument. It is also possible to
distribute the *<unk>* token probability to out-of-shortlist words using the
``--shortlist`` argument, in the same way as with ``theanolm score`` command.
However, the lattice decoder needs to assign some probability to words that did
not exist in the training data, so you may want to combine these two arguments.

By setting ``--unk-penalty=-inf``, paths that contain OOV words will get zero
probability. The effect of interpolation weight can be confusing if either the
lattice or the neural network model assigns -inf log probability to some word.
The result of interpolation will be -inf regardless of the weight, as long as
the weight of -inf is greater than zero. If -inf is weighted by zero, it will be
ignored and the other probability will be used.

Rescoring word lattices
-----------------------

``theanolm decode`` command can also be used for rescoring and pruning word
lattices. Simply select either SLF or Kaldi output using ``--output slf`` or
``--output kaldi``. This is beneficial over decoding the best path if lattice
information is needed in further steps. The pruning options are identical.

The CompactLattice format of Kaldi is actually a weighted FST. Each arc is
associated with an acoustic cost and what is called a graph cost. The graph cost
incorporates other things besides the language model probability, including
pronunciation, transition, and silence probabilities. In order to compute the
effect of those other factors, we can subtract the original LM scores from the
graph scores.

Assuming that we want to replace old LM scores with those provided by TheanoLM
without interpolation, it is possible to include the rest of the graph score by
subtracting the old LM scores, interpolating with weight 0.5, and multiplying
the LM scale by 2. Below is an example that does this, using standard Kaldi
conventions for submitting a batch job::

    ${cmd} "JOB=1:${nj}" "${out_dir}/log/lmrescore_theanolm.JOB.log" \
      gunzip -c "${in_dir}/lat.JOB.gz" \| \
      lattice-lmrescore-const-arpa \
        --lm-scale=-1.0 \
        ark:- "${old_lm}" ark,t:- \| \
      theanolm decode ${nnlm} \
        --lattice-format kaldi \
        --kaldi-vocabulary "${lang_dir}/words.txt" \
        --output kaldi \
        --nnlm-weight 0.5 \
        --lm-scale $(perl -e "print 2 * ${lm_scale}") \
        --max-tokens-per-node "${max_tokens_per_node}" \
        --beam "${beam}" \
        --recombination-order "${recombination_order}" \
        "${theanolm_args[@]}" \
        --log-file "${out_dir}/log/theanolm_decode.JOB.log" \
        --log-level debug \| \
      lattice-minimize ark:- ark:- \| \
      gzip -c \>"${out_dir}/lat.JOB.gz"

The downside is that another command is needed for interpolating with the
original (n-gram) language model scores. There are two example scripts for Kaldi
in the TheanoLM repository. `lmrescore_theanolm.sh`_ creates rescored lattices
without interpolation. `lmrescore_theanolm_nbest.sh`_ creates n-best lists,
interpolating the lattice and NNLM probabilities. These can be used in the same
manner as the other lattice rescoring steps in the Kaldi recipes, for example::

    steps/lmrescore_theanolm.sh \
      --prune-beam 8 \
      --lm-scale 8.0 \
      --beam 600 \
      --recombination-order 20 \
      --max-tokens-per-node 120 \
      --cmd "utils/slurm.pl --mem 20G" \
      data/lang \
      nnlm.h5 \
      model/dev-decode \
      model/dev-rescore
    local/score.sh \
      --cmd utils/slurm.pl \
      --min-lmwt 4 \
      data/dev \
      data/lang \
      model/dev-rescore

.. _lmrescore_theanolm.sh: https://github.com/senarvi/theanolm/blob/master/kaldi/steps/lmrescore_theanolm.sh
.. _lmrescore_theanolm_nbest.sh: https://github.com/senarvi/theanolm/blob/master/kaldi/steps/lmrescore_theanolm_nbest.sh

Generating text
---------------

A neural network language model can also be used to generate text, using the
``theanolm sample`` command::

    theanolm sample model.h5 --num-sentences 10

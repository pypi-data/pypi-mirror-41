============
**terITori**
============

Introduction
------------

Finding the origin (ORI) and terminus (TER) of replication is important for all research involving sequencing of genomic data, mainly because it gives clearly defined start and end points for a sequence, and enables comparison and analysis of different samples. Knowing these locations also provides verification that the sequences are correctly assembled. As it currently stands there are no one-stop software solutions for ORI and TER identification in bacteria; researchers have to rely on a combination of different tools and manual inspection of results.

To solve this, we developed **terITori**, an automatic tool for identifying origin and terminus of replication in bacterial genomes, which combines different key genomic features into a single final reliable prediction. The result is also statistically tested, which gives the user an idea about how accurate the prediction is. In terITori we believe we have created a useful program which will fill a gap in the available software of today, and make replication-related research simpler, faster and more accurate.

The three features that are included calculated in terITori are genomic skews (GC and TA), gene strand orientation, and conserved motifs (specifically dnaA boxes, dif motifs and rRNAs). terITori takes a FASTA file of the query bacterial genome as input, and allows the user to specify which features to include in the analysis (one, a combination of two, or all three). It also provides a file predicted genes in the bacteria, which have been predicted by the prokaryotic prediction program Prodigal. If a Prodigal gene prediction is already available, the user can specify this as an input.

The program is still in a very early stage, and the results might not always be fully accurate. The execution time could also be very long at times (up to several hours).

Description
----------------

The terITori script combines the three genomic feature scripts (skew, gene orientation, conserved motifs) and produces a final prediction of the ORI and TER positions. The results are combined in the following way:

* Run Prodigal if the all features, skew or gene orientation are included and no GFF file with already predict genes is entered. Save the predicted genes in a FASTA file.

* Predict ORI and TER using...

 * Identified rRNAs, DnaA boxes and dif motifs. Produces ORI and TER intervals, if possible.

 * Gene orientation data provided by the Prodigal output. Produces ORI and TER intervals and a significance estimation (p-value), through bootstrapping, for each.

 * Skew calculations. Produces predicted ORI and TER positions, along with p-values for each.

* Use the final prediction script to combine results and p-values.

* Save the predictions and p-values from all used methods in a results CSV file.

* Create and save an illustration as a PNG file (if the user has specified to do so). This will contain the cumulative GC and TA skew plots (if that script is included), the location and direction of conserved motifs (if the motifs calculation was included), and/or (if skew is not included but gene orientation is) the plot of the calculated statistic from the gene orientation script. Both gene orientation and skew plots cannot be included in the same figure as they have considerably different scales.

The results will be located in a directory terITori/Results/ located in the directory where the program is run. A log with timestamps for each step in the program is also produced and saved in the same location as the results.

Installation
------------

terITori can be installed via pip::

    $ pip install teritori

If the bin location is added to PATH it can then be run by typing::

   $ terITori

Dependencies
^^^^^^^^^^^^

Python (>=3.5)

Required Packages
"""""""""""""""""

- Biopython (``$ pip install biopython``)

- Numpy (``$ pip install biopython``)

- Matplotlib (``$ pip install matplotlib``)

- Scipy (``$ pip install scipy``)

- scikit-learn (``$ pip install scikit-learn``)

External Software
^^^^^^^^^^^^^^^^^^^^^

Executables should be in user's ``$PATH`` if nothing else specified.

Prodigal
"""""""""""""""""

A prokaryotic gene prediction software by Doug Hyatt. Tested with v. 2.6.2. Can be installed via apt::

 $ sudo apt install prodigal

or downloaded at `https://github.com/hyattpd/Prodigal <https://github.com/hyattpd/Prodigal>`_.

HMMER3
"""""""""""""""""

HMMER: biosequence analysis using profile hidden Markov models, by Sean Eddy and coworkers. Tested with v. 3.1b2. Can be installed via apt::

 $ sudo apt install hmmer

or downloaded at `http://hmmer.org/ <http://hmmer.org/>`_.

RNAmmer and HMMER2
""""""""""""""""""

You can find RNAMMER and instructions at `http://www.cbs.dtu.dk/services/doc/rnammer-1.2.readme <http://www.cbs.dtu.dk/services/doc/rnammer-1.2.readme>`_. Put the directory ``rnammer-1.2`` and the script file ``rnammer`` separately in ``*python package path*/teritori/conserved_motifs`` (usually ``/home/*username*/.local/lib/python3.x/site-packages/teritori/conserved_motifs``).

RNAmmer specifically requires HMMER version 2.2g to run, so you will need to download this in addition to HMMER3 (can be found `here <http://eddylab.org/software/hmmer/hmmer-2.2g.tar.gz>`_). Unzip the program and put the whole ``hmmer-2.2`` directory in the same directory as RNAmmer (``conserved_motifs``).

Now, open the ``rnammer`` file and modify the following:

- ``my $INSTALL_PATH``: set this to the **absolute** path of the ``rnammer-1.2`` directory (``your/path/to/rnammer-1.2``).

- ``$HMMSEARCH_BINARY``: set this to the **absolute** path of ``binaries/hmmsearch`` which can be found in the ``hmmer-2.2g`` directory (``your/path/to/hmmer-2.2g/binaries/hmmsearch``).

NOTE: RNAmmer and HMMER 2.2g do **not** need to be executable or accessible from the ``$PATH``.

Usage
^^^^^^^^^^^^^^^^^^^^^

Arguments
"""""""""""""""""

 -h                          show help message and exit
 -i I, --input I             **Required**. FASTA file with the bacterial genome to analyze.

                             Must contain exactly one sequence
 --genes GENES               GFF file containing all genes of the genome as predicted by Prodigal.

                             Must be on the exact format of a Prodigal prediction
 -o O, --output O            Output name format O. Output files will have this name.

                             If nothing specified, name will be parsed from input.
 -a                          Include all three genomic features in prediction.
                             Default mode if nothing specified
 --gc                        Include skew calculations in the prediction
 --go                        Include gene orientation in the prediction
 --cm                        Include conserved motifs in the prediction
 -l                          The genome is linear (default is circular)
 --graph                     Output graph of results in PNG file

Examples
"""""""""""""""""
Coming soon


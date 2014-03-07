Title: Topic Trending in Scientific Literature
Slug: arxivword
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/arxivword.html
Tags: Data Mining, Machine Learning, Classification, Text Classification
Type: xproject
Comments: True
Summary: Explore the topic trending of scientific literature by mining the ArXiv literature.

## Project Synopsis

The online archive repository where preprints are stored and distributed
provides a treasure trove of information. We wish to exploit these and similar data
to build a trending tool to identify trending topics in a specific scientific field.

## Project Description

This is a blue-sky project. This means the basic idea is known, but how
we implement it is not. At its simplest, we could simply apply standard
Hadoop Map-reduce to this problem, the Word count is the standard Hadoop
demonstration project. However, considerable work has been developed
recently that provides other mechanisms to identify 'hot trends' in
text data, as word frequency may not be ideal in all cases.

Different models have been developed to tackle different challenges. One
example is Latent Semantic Analysis (LSA), which uses singular value
decomposition (SVD) to identify important words. Other approaches
include probabilistic LSA, Vector Space Model (VSM), and Latent Dirichlet
Allocation (LDA). An nice review article, that focuses on LDA, by Blei (2012) is
available that provides more information.

## Programming Notes

The implementation language will ideally be Python. There is a python
library available to help develop topic modeling analyses. -  Java
implementation?

We can use Hadoop via Python, translate things to Java, try to run a
Python map-reduce engine, or perhaps simply use parallel Python.

## Starting Conditions

This project is currently in the design stage.

## Expected Outcome

TBD

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- [ADS Labs](http://labs.adsabs.harvard.edu/adsabs) where a similar effort is performed on the contents of
the NASA ADS archive.

- [Twitter Data
mining](http://figshare.com/articles/Tweets_linking_to_arXiv_preprints,
_Jan_-_Oct_2012/97109) of scientific literature tweets.

- [Octopy](https://code.google.com/p/octopy/) a MapReduce in Pure Python

- [MinceMeat](https://github.com/michaelfairley/mincemeatpy) another MapReduce framework in Pure Python

- [MapReduce in
Hadoop](http://www.michael-noll.com/tutorials/writing-an-hadoop-
mapreduce-program-in-python/) called from Python

- [LSA](http://en.wikipedia.org/wiki/Latent_semantic_analysis)

- [GenSim](http://en.wikipedia.org/wiki/Gensim) python library for implementing LSA.

- [LDA](http://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

- [Blei Review](http://www.cs.princeton.edu/~blei/papers/Blei2012.pdf) article.

Title: Probabilistic Cosmological Measurements
Slug: probcosmo
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/probcosmo.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject
Comments: True
Construction: True
Summary: Develop Probabilistic versions of existing cosmology codes

## Project Synopsis
Develop a probabilistic two-point correlation code.

## Project Description
The two-point correlation function (TPCF) is a very important
measure of the distribution of a set of points, particularly in
Cosmology, where it is used to measure the clustering of galaxies in the
Universe. TPCF measurements can be compared to theoretical predictions
in order to constrain the allowed values of cosmological quantities like
the amount of dark matter or dark energy in the Universe. Most current
TPACF implementations, however, always assume a source measured in a sky
survey is unambiguously a galaxy and that it has a known distance from
Earth.

This project is designed to remove these limitations. By including a
probabilistic classification for whether a source is a galaxy or not and
a probability density function for the distance a source is located from
Earth, we can use significantly more data to make more precise
cosmological measurements with exact same input data.

## Programming Notes

TBD

## Starting Conditions
A fast, dual-tree implementation of the TPACF
algorithm has been developed and published by our group. This code is
written in C and forms the basis for the new code implementation. An
optional project is to also develop a probabilistic power spectrum
estimator, for which we also have an existing implementation written in
C. Both of these codes are run on supercomputers to make their computations.

## Expected Outcome
The student will first modify the existing TPACF
code to read probabilities for each source (along with their positions
on the sky) from an input file. Second, the student will modify the
TPACF computation to include these probabilities in the calculation of
the correlation function (the probabilities will effectively act like a
weight for each source in the measurement). Finally, the student will
test the accuracy and performance of the new code on existing data. An
optional second algorithm is the Angular Power Spectrum, for which a similar
modification can be made.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- Original [Two-point
correlation](http://www.linuxclustersinstitute.org/conferences/archive/
2008/PDF/Dolence_98279.pdf) paper
- [Demonstration](http://arxiv.org/abs/1303.2432) of our two-point code.
- TPACF](/code/tpacf.html) source code.
- Original [Angular Power Spectrum](http://arxiv.org/abs/1112.5723) paper.
- [APS](http://lcdm.astro.illinois.edu/code/aps.html) source code.
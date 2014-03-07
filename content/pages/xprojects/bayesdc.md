Title: Bayesian Source Detection and Characterization
Slug: bayesdc
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/bayesdc.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Source Detection
Type: xproject-hot
Comments: True
Latex: True
Summary: Develop an image based Bayesian source detection and characterization code.

## Project Synopsis

We will develop a Bayesian, pixel-based, model fitting
technique to robustly quantify both the number of sources and the best
functional representations for these sources within single-band images
across the sky.

## Project Description

Currently, most source detection for astronomy images is performed in a
standard peak finding approach that measures a standard set of shape
parameters and determines the flux of an object through standard
apertures (e.g., a circle of a specified radius). For example, this is
how the SExtractor tool operates. While easy to understand, this
approach fails to fully extract the maximal information from a source
within an image, and completely fails to account for differences a
source might display between images taken in different filters or at
different times. More sophisticated approaches will sometimes perform
model fitting to the image to extract additional information, or to
match apertures between images taken through different filters (e.g.,
the SDSS image processing pipeline).

While useful, these approaches fail to provide a complete picture of the
sources present in an image, and currently remain tied to a set of
pre-defined models. We instead believe that the best option is to
instead find and characterize sources in astronomy images in a Bayesian
approach, where the number of sources are characterized by finding and
characterizing them by using a set of basis functions. For example, a
nested sampling technique, as described by Feroz and Hobson, can find
sources in an image, after which we can optimally characterize the
functional form of the light distribution for all sources. The latter
approach has recently been demonstrated by Lang & Hogg.

This is a challenging problem, but one that will have profound impact.
First, we will maximally extract the information from an image. Second,
we will be able to recreate the image by using our model representation,
thus we create an accurate, highly compressed, lossy compression of the
original image. Third, this approach can be used to look for residuals
in the image that might be gravitational lenses or image artifacts that
need to be cleaned. Fourth, we can extend this technique to
simultaneously detect and fit in multiple images taken through
different filters. Finally, we can extend this technique to modle
sources observed at different epochs in order to characterize how our
models change in time.

## Programming Notes

This is an ambitious project, but many parts are conceptually simple.

- We will initially develop a bayesian detection method in Python, PyMC
could prove useful. This will initially focus on small single-band
images, for example in the SDSS $r$-band, and we will start with a
mixture of Gaussians as the first set of basis functions. This set can
be recorded as a sparse representation format.

- This initial work will be extended to work in multiple bands, for
example, by applying the technique to SDSS $u$, $g$, $r$, $i$, and $z$ bands.

- (Optional) Extend to large data sets

- (Optional) Look for image residuals

- (Optional) Extend to multiple Epochs

## Starting Conditions

This project is currently in the design stage.

## Expected Outcome

At a minimum, we would expect a Python implementation finds and fits
sources in a single image by using Bayesian Modeling.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://www.sdss3.org)
- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- [SExtractor](http://www.astromatic.net/software/sextractor) source extractor code

- [PyMC](http://pymc-devs.github.io/pymc/) Python based Bayesian Modeling

- [EMCEE Hammer](https://github.com/dfm/emcee) Pure Python fast MCMC

- [Multinest Bayesian Analysis](http://arxiv.org/abs/0704.3704) with
application to Bayesian source detection.

- [Multinest source
code](http://ccpforge.cse.rl.ac.uk/gf/project/multinest/), note not
truly open source. 

- Python [Multinest Sampler](https://github.com/JohannesBuchner/PyMultiNest) might be of interest.

- [Galaxy Profile Fitting](http://arxiv.org/abs/1210.6563) by Hogg and Lang

- [Sparse
Representation](http://en.wikipedia.org/wiki/Sparse_approximation) where
we can represent a function as an expansion in a pre-determined set of
basis functions.


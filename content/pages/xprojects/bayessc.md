Title: Bayesian Source Classification
Slug: bayessc
Date: 2014-03-03
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/bayessc.html
Tags: Data Mining, Machine Learning, Classification, Astronomy Database 
Type: xproject
Comments: True
Construction: True
Summary: Develop Python implementation of Bayesian source classification.

## Project Synopsis

Develop a Python-based implementation of a Bayesian source
classification algorithm that can scale to billions of sources. 

## Project Description

Astronomers have entered the era of survey astronomy, for
example we have the recently completed [Sloan Digital Sky
Survey](http://www.sdss.org) (SDSS) and the recently started [Dark
Energy Survey](https://www.darkenergysurvey.org) (DES). These surveys
generate TBs and now PBs of imaging data that can be used to answer
fundamental questions about our Cosmos. But before the processed image
data can be used scientifically, we must first separate out the stars in
our Milky Way galaxy from the galaxies that make up the cosmic web.

One new approach to classifying sources in a an astronomical survey was
recently developed by Henrion et al. (2011), additional discussions were
provided by Fadeley et al. (2012). This approach computes the Bayesian
Evidence from the input photometric measurements and makes a
probabilistic classification. Their implementation is written in he R
programming language and was applied to a small data set from the UKIDDS
survey (an infrared sky survey). To make this approach more effective
and to enable future enhancements to the method, we are looking for a
student to convert this R implementation into Python.

## Programming Notes

TBD

## Starting Conditions

The R implementation is available on github and
provides an implementation of the algorithm. 

## Expected Outcome

We have test data on which to compare the new
Python version to the original R version. At a minimum we expect the
student to complet the Python version and verify its accuracy against
the R version. A second gola would be to apply this data to a large,
deep survey data to test scaling performance and identify bottlenecks.
The final goal will be to implement performance improvements to
accelerate this new implementation to scale to billions of sources.

## Personnel

The lead mentor for this project is Edward Kim, with assistance from Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://www.sdss3.org)
- The [Dark Energy Survey](http://www.darkenergysurvey.org)
- [Bayesian Star Galaxy Classification](http://arxiv.org/abs/1011.5770) by Henrion et al.
- [Star Galaxy Classification](http://arxiv.org/abs/1206.4306) by Fadeley et al.

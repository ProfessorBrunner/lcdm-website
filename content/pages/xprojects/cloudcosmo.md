Title: Cloud-based Cosmological Measurements
Slug: cloudcosmo
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/cloudcosmo.html
Tags: Cloud Computing, Cosmology, Power Spectrum, Correlation Function
Type: xproject
Comments: True
Construction: True
Summary: Develop new, cloud-based cosmological measurement codes

## Project Synopsis
Develop a cloud-computing based implementation of the standard
two-point correlation function and the angular power spectrum.

## Project Description
A correlation function measures the likelihood that one
source (like a galaxy) will be within a given distance from another
source (like another galaxy). Correlation functions are often done in
angular coordinates, so the distance is a one-dimensional angle. In this
project, the student will develop a two-dimensional correlation
function. This approach will uniquely be able to measure if any	
systematic effects due solely to the observational strategy are present.

The angular power spectrum is the Legendre transform of the correlation function.

## Programming Notes

TBD

## Starting Conditions
An prototype Hadoop implementation of an angular two-point correlation
function exists. We also have fast, two-point and angular power spectrum
codes published and available.


## Expected Outcome
The student will convert this to Java to run on Hadoop, and second,
extend this new implementation to measure the correlation function in
terms of two angles. Finally, the student will test this new
implementation to verify its accuracy.

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
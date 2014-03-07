Title: Cloud-based Cosmological Measurements
Slug: cloudcosmo
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/cloudcosmo.html
Tags: Cloud Computing, Cosmology, Power Spectrum, Correlation Function
Type: xproject
Comments: True
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

<img src="{filename}/static/images/corrfig.png"
alt="Galaxy shown in different filters"
width="450px" height="auto" align="center"
display="block" />

The angular power spectrum is the Legendre transform of the correlation
function, and is typically calculated from a pixelized map. This map is
often constructed by using the HEALPix pixelization scheme. In this
case, we likely will encode the probabilities directly into the galaxy
over/under density within this pixel map.

## Programming Notes

These codes will likely be written in Java to run within Hadoop.

## Starting Conditions

A prototype Hadoop implementation of an angular two-point correlation
function exists. We also have fast, two-point and angular power spectrum
codes published and available on the LCDM website.


## Expected Outcome

The student will convert this to Java to run on Hadoop, and second,
extend this new implementation to measure the correlation function in
terms of two angles. Finally, the student will test this new
implementation to verify its accuracy.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

The current code for computing the TPACF within Hadoop will be posted to github soon.

- Original [Two-point
correlation](http://www.linuxclustersinstitute.org/conferences/archive/
2008/PDF/Dolence_98279.pdf) paper

- [Demonstration](http://arxiv.org/abs/1303.2432) of our two-point code.

- [TPACF](/code/tpacf.html) source code.

- Original [Angular Power Spectrum](http://arxiv.org/abs/1112.5723) paper.

- [APS](http://lcdm.astro.illinois.edu/code/aps.html) source code.

- [HEALPix](http://healpix.jpl.nasa.gov) Home Page.
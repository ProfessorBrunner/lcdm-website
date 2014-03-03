Title: Model-Based detection of Strong Gravitational Lenses
Slug: sglmodel
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/sglmodel.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject
Comments: True
Construction: True
Summary: Model lensing galaxies in astronomical images to detect strong gravitational lenses as residuals.

## Project Synopsis

Finding strong gravitational lenses in astronomical image data is
difficult. Most lens systems, either quasars or galaxy arcs have been
found completely, or in large part, due to human visualization. We will
develop an automated approach to reduce the requirement for human
visualization. 

## Project Description

Model lensing galaxy and remove.
Test if residuals are at right distance from lens (Einstein Radius).
Machine learn patterns, or Bayesian model comparison.

Can apply to SDSS data at start, move to DES and maybe CFHTLS and KIDS data. PanSTARRs?

## Programming Notes

- The model fitting will be performed in Python, and will use the
[astropy](http://www.astropy.org) framework.

- Model Residual testing will be done in Python.

- Machine Learning of residuals will be TBD.

- The implementation will need to scale to PBs of image data.

## Starting Conditions

This project is currently in the design stage.

## Expected Outcome

At a minimum, the image model fitting and residual testing should be
completed. Secondary considerations will be scaling the code to support
large image repositories and to incorporate machine learning in the
residual classification.

## Personnel

The lead mentor for this project is Edward Kim, with assistance from Professor Brunner.

## References

- Strong Lens Review
- LensTractor?
- Other lens modeling stuff?
- ds9
- 
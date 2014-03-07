Title: Image Pixel Based Photometric Redshift Estimation
Slug: ipbpz
Date: 2014-03-02
Modified: 2014-03-03
Authors: Robert J. Brunner
Save_as: xprojects/ipbpz.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject-hot
Comments: True
Latex: True
Summary: Estimate photometric redshifts for sources directly from astronomical images.

## Project Synopsis

Treat each pixel as an observation and use this multi-band information
to estimate a pixel photometric redshift. This can be done by using
existing tools like MLZ. Then need to aggregate pixel estimates for all
pixels assigned to a given source.

## Project Description

<img src="{filename}/static/images/gal_color.png"
alt="Galaxy shown in different filters"
width="200px" height="auto" align="right"
display="block" style="margin-left: 20px;" />

Currently,  estimation of the distances to galaxies (known as a photo-z)
uses the reduced summary information extracted each images. This data
includes the flux of an object, where the information from each pixel
assigned to an object is gathered within each filter in the survey like
the image in Figure 1. Both the training and validation for computing
photo-zs are done by using these precomputed information with remarkable
results.

<img src="{filename}/static/images/pixel_im.jpg"
alt="Galaxy shown in different filters"
width="200px" height="auto" align="right"
display="block" style="margin-left: 20px;" />

But what if we apply current machine learning techniques earlier in the
process, and instead estimate distances to each pixel independently? We
can aggregate the information for each pixel (see, for example, Figure 2)
to obtain an even better prediction, or a better identification of
outliers in the distribution. 

This project will directly address this issue by training and testing the
algorithms at the pixel level, which overcomes the requirement of having
predefined models or per-source apertures, which might bias the distance
estimation. 

This project is on the cutting-edge of galaxy distance estimation.

## Programming Notes

Python is the preferred language for this project. The following list
provides schematic outline of the main steps required to complete this
project.

- Image registration to make sure the pixels are aligned between different filters.

- Generate training samples by using redshift information, assuming
little or no variation for the distance among the pixels.

- Extract pixel information from each image and put it on a structured
format. For example, for a data set containing five filters (or bands),
each $N \times M$ image will have a five-element vector corresponding to each
pixel.

- Compute distances and aggregate distance information for each pixel
using a Bayesian model.

- (Optional) Extend this technique to perform source classification,
object identification, and all-sky modeling.

- (Optional) Scale to Petabyte Image data sets.

## Starting Conditions

This project is currently in the design stage:

- The SDSS image data set will form the initial test data. Images will
be provided to initiate the project, and additional data will be
provided as needed.

- Different machine learning algorithms to compute photometric redshifts
will be made available. This will primarily (perhaps exclusively) be
done by using the Machine Learning for Photo-Z estimation code.

- To start, the project requires no additional computational resources.
As the project develops, and larger data sets are processed, additional
computational resources will be provided.

## Expected Outcome

TBD

## Personnel

The lead mentor for this project is Matias Carrasco-Kind, with assistance from Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://www.sdss3.org)
- [Machine Learning for Photometric Redshifts](/code/mlz.html)
- [Trees for Photo-z](/papers/TPZ.html)
- [Self Organizing Maps for Photo-Z](/papers/SOMz.html)
- [ds9](http://ds9.si.edu/site/Home.html)  image viewer
- The [Source Extractor](http://www.astromatic.net/software/sextractor) program.
- [Astronomical Python](http://www.astropy.org) libraries
- [Python image processing](http://scikit-image.org) libraries

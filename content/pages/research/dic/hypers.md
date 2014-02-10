Title: Image-based identification of Strong Gravitational Lenses
Slug: hypers
Date: 2014-02-10
Modified: 
Authors: Robert J. Brunner
Save_as: research/dic/hypers.html
Tags: Image Processing, Hyperspectral, Source Detection, Photometry
Type: subproject
Parent: dic
Construction: True
Summary: We are exploring new methods for hyper spectral image processing and analysis.

Techniques for astronomical image processing for source detection and
extraction were first developed decades ago for analyzing digitized
photographic plates. With the advent and growh of digital astronomy,
these techniques (e.g.,
[SExtractor](https://www.astromatic.net/software/sextractor)) have been
slightly modified, but still focus on single-band peak finding, with
forced photometry in additional bands. 

The computer vision communities
have been working on novel techniques for [hyperspectral
imaging](http://en.wikipedia.org/wiki/Hyperspectral_imaging). In this
approach, all data is analyzed to extract the maximum possible
information. In collaboration with the [Image Formation and Processing
group](http://beckman.illinois.edu/research/themes/hcii/image-formation-
and-processing) at the [Beckman Institute](http://beckman.illinois.edu),
we are exploring the application of hyperspectral image processing to
explore if this new technique can generate more complete and accurate
source catalogs from astrophysical data.

## Data

The primary application data for this technique is currently the SDSS
imaging data. Initial application data will come from the [SDSS fCalib
files](https://www.sdss3.org/dr10/imaging/images.php#corr). In this
survey, we have five bands with which to simultaneously detect and
photometer. Total data volume for this test is approximately ten TBs. This will require a
more careful plan for the overall workflow of pre-processing,
processing, and archiving all relevant data. This project is a strong
candidate for a move to a cloud-computing paradigm.

The number of possible application data sets is quite varied. We can
either extend the techniques we develop immediately to the DES and
Pan-Starrs data, which are Petascale optical based surveys like the SDSS. Or,
alternatively, we could explore combining multi-wavelength data with the
SDSS (or DES) directly to explore source detection and photometry across
UV, optical, and infrared (and possibly to other wavelengths).

## Personnel

The lead students on this project are Zhangyang (Atlas) Wang and Zhaowen Wang.



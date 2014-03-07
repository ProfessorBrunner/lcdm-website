Title: An updated, calibrated format, SDSS RC3 catalog
Slug: sdssrc3
Date: 2014-03-06
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/sdssrc3.html
Tags: ASDSS, RC3, Image Mosaic, Calibrated Image, FITs
Type: xproject
Comments: True
Summary: Develop a new, scientifically calibrated version of the RC3 cataloged sources contained within the SDSS.

## Project Synopsis
The RC3 catalog provides a reasonable complete listing of bright
galaxies. We provide color composite images and scientifically
calibrated FITs images in all five SDSS bands for each of these galaxies
that lie within the SDSS footprint.

## Project Description

The RC3 catalog, as corrected by Corwin, contains a listing of
approximately 23,000 galaxies. Many of these galaxies lie within the
SDSS footprint. Hogg and Blanton made an SDSS RC3 catalog by using data
from the SDSS DR6. We would like to update and improve on their work, by
using the more recent SDSS data reductions to make both the color images
as well as scientifically calibrated image mosaics for each galaxy in
the RC3 catalog that lies within the SDSS footprint.

If successful, we will expand this project to include other sources,
including objects like  Planetary Nebulae and Galaxy Clusters. We also
will work to extend this project to include data from other surveys like
the DES.

## Programming Notes

Most likely we will develop a Python program to call Montage iteratively
on the data needed to build each RC3 galaxy that lies with in the SDSS
footprint. We will then build a color image by using STIFF. This project
is not conceptually difficult, but doing right will take patience and
good record-keeping. All files will eventually be served off the LCDM
website.

## Starting Conditions

We have made many composite images from SDSS, so the basic knowledge of
doing this with SDSS exists (as do various scripts), see Figure 1 for
example, which is m101 made from the SDSS.


<img src="{filename}/static/images/m101.jpg"
alt="Galaxy shown in different filters"
width="400px" height="auto" align="right"
display="block" style="margin: 20px;" />

## Expected Outcome

Calibrated, mosaiced images from the SDSS of RC3 galaxies, displayed via
a web page, or possible Web application that connects to a back end data
store.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://www.sdss3.org)

- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- [NYU](http://cosmo.nyu.edu/hogg/rc3/) catalog by Hogg and Blanton.

- [RC3](http://cdsarc.u-strasbg.fr/viz-bin/Cat?VII/155) catalog hosted by CDS

- [Montage](http://montage.ipac.caltech.edu) fits image mosaicing software

- [STIFF](https://www.astromatic.net/software/stiff) can create color images from input astronomy images.

- [Astropy](http://www.astropy.org) astronomy Python library, can be used for reading FITs
images and using WCS.

- [SDSS Image Mosaic
Tools](http://www.arcetri.astro.it/~zibetti/Software/SDSSmosaic.html)
can be used as well, but have a lot of dependencies.

- [Mosaic SDSS images](http://www.physics.ox.ac.uk/users/msshin/science/code/#SDSS_tools) 
python tool that calls the IRSA montage server.
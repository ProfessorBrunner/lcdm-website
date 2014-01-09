Title: Fast Angular Power Spectrum Estimation Code
Slug: aps-code
Date: 2011-12-01
Modified: 2013-09-06
Authors: Robert J. Brunner
Save_as: code/aps.html
TAGS: APS, angular power spectrum, cosmology, hpc, openmp, quadratic estimator
Construction: True
Summary: We have released our fast quadratic function angular power spectrum estimation code.

## Introduction

We have implemented a pixel-based, quadratic esimtation algorithm to
compute the galaxy angular power spectrum The implementation was first described in 
[Hayes, Brunner, & Ross 2012](http://adsabs.harvard.edu/abs/2012MNRAS.421.2043H)
and was also used in
[Hayes & Brunner 2013](http://adsabs.harvard.edu/abs/2013MNRAS.428.3487H).

## Public Archive

The code base is currently being migrated to [github](https://github.com/ProfessorBrunner).

## Original Archive

The originally published [quadratic
estimator](/static/apsqe/KL_spectrum.tar.gz) implementation is permanently
archived at the LCDM site.

Once compiled, the program is run with two inputs: a HEALPix pixelated
data file and a bandpower file specifying the starts, ends, and initial
values of the bandpowers.

For the HEALPix input file, the NESTED coordinates must be used, and the
name of the file MUST have the following format: it must begin with the
HEALPix resolution, followed by an underscore, then the total number of
unmasked galaxies in the sample, followed by an underscore, followed by
the rest of the name (i.e., "256_18923408_..."). The value of each pixel
should be the galaxy overdensity of that pixel, and masked pixels should
have a value of less than -1 (they will be ignored). We provide a 
[sample FITS file](/static/apsqe/64_18860538_mag18-21_type0.0-1.0_stripe_9-37.fits).

For the bandpower input file, the format matches the output of the code.
The seven columns are: bandpower number, bandpower midpoint, bandpower
start, bandpower end, initial value of C_l, error of C_l, and the
initial value of C_l (repeated). For the read-in of this file, all
columns other than the third, fourth, and fifth columns are ignored. We provide a 
[sample bandpower input](/static/apsqe/C_18-21_0.0-1.0_9-37_64_200.dat) file.

## Contact:

If you have any questions about these codes, please contact Robert
Brunner (<bigdog@illinois.edu>)

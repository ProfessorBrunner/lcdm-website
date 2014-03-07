Title: GSOC 2014 Code Problem 
Slug: gsoc14code 
Date: 2014-03-06
Modified: 
Authors: Robert J. Brunner 
Save_as: gsoccode.html 
Tags: GSoC,Proposal Code Problem 
Latex: True 
Summary: A coding problem for LCDM GSoC applicants.

## GSoC Problem Description

To aid the LCDM group in evaluating a candidate's ability to work on a
project effectively, we encourage all applicants to complete the
following Python programming assignment. This is not a requirement, but
having code helps us to understand your programming ability.
Alternatively, you could send code more directly related to a specific
project. In this case, however, it will be up to you to determine what
part of the project to tackle now in order to have code to share with us.

The sample programming task is to read in an astronomy image, find the
center of the light distribution, compute the second order moments of
the light distribution, use these to compute the principal axes of the
the light distribution (i.e, ellipticity), and finally to display the image
with the center pixel marked and the principal axis of the image
indicated.

## GSoC Problem Data

You can download the <a href="/static/data/M86.fits.bz2">sample data
image</a>, which is an image of the M86 galaxy (shown in Figure 1). This
file is in the astronomical FITs standard format. To read this file into
a Python program, use pyfits, which is part of the astropy library. This
will allow you to pull he image into your Python program as a numpy 2D
array.

<img src="/static/images/M86.png"
alt="Galaxy shown in different filters"
width="400px" height="auto" display="block" />

## GSoC Problem algorithm

To find the center of the image, you first need to determine a threshold
value (above which we consider a pixel to be part of an object, below
this we say it is likely noise). An easy way to do this is to find the
mean and standard deviations of the values contained in the image
pixels. The threshold can simply be set to the mean value plus one
standard deviation. 

The center of all of these pixels above the threshold can be computed as
a weighted mean (in x and y directions). If you understand the center of
mass, this is the same idea. The second order moments ($I_{x x}$, $I_{x
y}$, $I_{y y}$) of the light distribution (like moments of inertia)
indicate the preferred axes of the light distribution. When you plot the
image with matplotlib, use a log normalization:

```python
    norm=lm(image.mean() + 0.5 * image.std(), image.max(), clip='True'), \
        cmap=cm.gray, origin="lower")
```
Your final plot should look like this:

<img src="/static/images/M86-rjb.png"
alt="Galaxy shown in different filters"
width="400px" height="auto" display="block" />

Submit your Python code and the final image to Professor Brunner.

## References

- The model fitting will be performed in Python, and will use the
[astropy](http://www.astropy.org) framework.

- The [Centroid](http://en.wikipedia.org/wiki/Centroid) can be used to
find the center of mass.

- Calculating
[Moments](http://en.wikipedia.org/wiki/Moment_(mathematics)) for
distributions. Note that an image is a pixelized or discrete
distribution.


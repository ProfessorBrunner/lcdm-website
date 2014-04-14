Title: Model-Based detection of Strong Gravitational Lenses
Slug: sglmodel
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/sglmodel.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject
Comments: True
Latex: True
Summary: Model lensing galaxies in astronomical images to detect strong gravitational lenses as residuals.

## Project Synopsis

Finding strong gravitational lenses in astronomical image data is
difficult. Most lens systems, either quasars or galaxy arcs have been
found completely, or in large part, due to human visualization. We will
develop an automated approach to reduce the requirement for human
visualization. 

## Project Description

This project is conceptually simple. First, we wish to model the smooth
light profile of the lensing galaxy (see Figure 1). Generally this galaxy will be an
Elliptical galaxy, which can be fit by a 2D sersic model. Given this
model light distribution, we will subtract off the light to look at the
residuals. Any potential resiudals could imply interesting astrophysics,
such as a nuclear dust lanes, a bar, or evidence of interactions;
inaccuracis in the model used to fit the light, possibly tied to the
interesting astrophysics; a possibly systematic effect that was missed
in the image reduction process; or possibly a gravitational lens.

Here we present the $u$, $g$, $r$, $i$, and $z$ band images of an SDSS
gravitational lens, along with a color image made by combining the $g$,
$r$, and $i$ images.

![u-band image of SDSS gravitational lens]({filename}/static/images/l1u.png)
![g-band image of SDSS gravitational lens]({filename}/static/images/l1g.png)
![r-band image of SDSS gravitational lens]({filename}/static/images/l1r.png)
![i-band image of SDSS gravitational lens]({filename}/static/images/l1i.png)
![z-band image of SDSS gravitational lens]({filename}/static/images/l1z.png)
![Color composite image of SDSS gravitational lens]({filename}/static/images/l1c.png)

To test the lensing hypothesis, we can measure the angular distance
between the lensing galaxy and the residual to see if the residuals are
located close to the predicted Einstein radius. At this point we can
visually inspect candidates, or perhaps we can add in a futher
restriction by imposing a machine learning step to reduce the number of
possible candidates (note: given the paucity of known lenses, it is
likely easier to train an algorithm on **not** lenses). We also might
impose a Bayesian learning process to optimize the search for known
types of lenses, or use simulations to boost the training sample of known lenses.

Initially we will apply this to the SDSS data to recover the known
lenses, but this can be extended to data form the  Dark Energy Survey
(DES), the CFHTLS, the KIDS data, as well as the Pan-STARRs data.

## Programming Notes

- The model fitting will be performed in Python, and will use the
[astropy](http://www.astropy.org) framework.

- Model Residual testing will be done in Python.

- Machine Learning of residuals will probably use Python.

- Eventually, we will want to scale the implementation will need to PBs
of image data.

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

- The [Sloan Digital Sky Survey](http://cas.sdss.org) database

- The [Sloan Digital Sky Survey](http://www.sdss3.org)

- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- The [CFHTLS](http://www.cfht.hawaii.edu/Science/CFHTLS/) data

- The [KIDS](http://kids.strw.leidenuniv.nl) project

- [Pan-STARRs](http://pan-starrs.ifa.hawaii.edu/public/) project

- Dr Phil Marshall [demonstrates](http://www.youtube.com/watch?v=PviYbX7cUUg) Gravitational Lensing

- Introductory [review article](http://www.annualreviews.org/doi/full/10.1146/annurev-astro-081309-130924) on strong gravitation lensing

- The [ds9](http://ds9.si.edu/site/Home.html) FITs image viewer

- The [fv](http://heasarc.gsfc.nasa.gov/ftools/fv/) FITs image viewer

- The [CASTLES Survey](http://www.cfa.harvard.edu/castles/) Lens database

- The [Cassowary Lens](http://www.ast.cam.ac.uk/ioa/research/cassowary/) gravitational lens search

- [SpaceWarps](http://spacewarps.org) crowdsourcing lens search

- The [LensTractor](https://github.com/davidwhogg/LensTractor) lens
modeling system. A similar idea to the one proposed here.

- [PCA-based](http://arxiv.org/abs/1403.1063) lens finding technique

- [RingFinder](http://arxiv.org/abs/1403.1041) lens finding technique

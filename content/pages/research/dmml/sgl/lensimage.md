Title: Image-based identification of Strong Gravitational Lenses
Slug: lensimage
Date: 2014-02-10
Modified: 
Authors: Robert J. Brunner
Save_as: research/dmml/sgl/lensimage.html
Tags: Data Mining, Machine Learning, Strong Gravitational Lens, Image Classification
Type: subproject
Parent: sgl
Construction: True
Summary: We are exploring image-based anomaly detection techniques to identify strong gravitational lenses.

Strong gravitation lenses, in particular arcs, are anomalous in large,
astrophysical image data. Considerable effort has been applied within
the computer vision community to identify anomalous items (for obvious
reasons), leading to the concept of
[saliency](http://en.wikipedia.org/wiki/Salience_(neuroscience)). In
collaboration with the [Image Formation and Processing
group](http://beckman.illinois.edu/research/themes/hcii/image-formation-
and-processing) at the [Beckman Institute](http://beckman.illinois.edu),
we are exploring the application of salient detection to finding arcs
and multiple imaged sources in astrophysical data sets.classification of
astrophysical sources.

## Data

The primary application data for this technique is currently the SDSS
imaging data. Positive training data come from the
[Cassowary](http://www.ast.cam.ac.uk/ioa/research/cassowary/) project
and the GalaxyZoo [Space Warps](http://spacewarps.org) project, led by
Phil Marshall. This project has leveraged the GalaxyZoo infrastructure
to identify possible gravitational lenses in different data sets,
including the SDSS. For this project, we have extracted multi-band
_positive_ image cutouts from SDSS fCalib frames. We also need to
extract _negative_ candidates, but this sample remains t.b.d.

Once training has been completed, we will apply the resulting algorithm
to both SDSS, Pan-Starrs, and DES data sets. This will require a
more careful plan for the overall workflow of pre-processing,
processing, and archiving all relevant data. This project is a strong
candidate for a move to a cloud-computing paradigm.


## Personnel

The lead student on this project is Kai-Hsiang (Sean) Lin.



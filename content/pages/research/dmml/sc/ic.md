Title: Source Classification in Astrophysical Images
Slug: ic
Date: 2014-02-10
Modified: 
Authors: Robert J. Brunner
Save_as: research/dmml/sc/ic.html
Tags: Data Mining, Machine Learning, Classification, Image Classification
Type: subproject
Parent: sc
Construction: True
Summary: We are applying the techniques of deep learning to classify sources directly from astrophysical images.

The field of computer vision has made tremendous strides in identifying
and clasifying sources in commercial digital imaging. In collaboration
with the [Image Formation and Processing
group](http://beckman.illinois.edu/research/themes/hcii/image-formation-
and-processing) at the [Beckman Institute](http://beckman.illinois.edu),
we are exploring the application of [deep
learning](http://en.wikipedia.org/wiki/Deep_learning) to the
classification of astrophysical sources.

## Data

Our initial application area will be data from the SDSS. The best
training sample available has been generated by the human volunteers
within the GalaxyZoo project. The GalaxyZoo project, under Kyle Willett
has created a [Kaggle
competition](http://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge)
for the image classification. The images in this project are stored as
JPegs, which might be a useful starting point. However, we likely will
want the five-band [Atlas
images](http://www.sdss3.org/dr10/imaging/images.php#atlas) for the
sources to classify. Acquiring atlas images is possible, but will require
pre-processing to properly extract all five bands (note special SDSS
software exists to extract the images).

Eventual goals for this project will be to apply these techniques to the
larger datasets of the Pan-Starrs and DES projects. This will require a
more careful plan for the overall workflow of pre-processing,
processing, and archiving all relevant data. This project is a strong
candidate for a move to a cloud-computing paradigm.

## Personnel

The lead student on this project is Honghui Shi, with support from Wei Han and Tom Paine.



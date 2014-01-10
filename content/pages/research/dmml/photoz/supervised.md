Title: Supervised Photo-Z Estimation
Slug: supervised
Date: 2012-08-15
Modified: 
Authors: Matias Carrasco-Kind, Robert J. Brunner
Save_as: research/dmml/photoz/supervised.html
Tags: Data Mining, Machine Learning, Supervised, Photometric Redshift, Random Forest, Python, Decision Trees
Type: subproject
Parent: photoz
Construction: True
Summary: We develop and apply supervised machine learning techniques to the problem of estimating photometric redshifts.

## Supervised Photometric Redshift Estimation.

We have recently taken a more complete approach to this problem by
introducing Trees for Photo-Z (TPZ; Carrasco & Brunner 2013a), a new,
Python-based, machine learning, parallel code for estimating photometric
redshift PDFs by using prediction trees and random forest techniques
(Breiman et al. 1984; Breiman 2001). Our approach is an ensemble
learning method that generates several classifiers and combines their
results into a final output. Prediction trees partition the
multi-dimensional space recursively into smaller regions, which are
terminated when a leaf only contains a few elements. Within these final
leaves, our algorithm can leverage a simple model for the actual
prediction, by using, for example, the mean value for a regression or
the mode in a voting process for the photo-z classification.

Likewise, the basic idea of a random forest method is to use bootstrap
samples from the training data to build a set of prediction trees. These
trees are constructed by selecting the best split point from a random
subsample of the dimensions (e.g., magnitudes or colors) along which the
data is subdivided. By aggregating the predictions from this forest of
trees, we produce a more accurate estimate. In our implementation, we
incorporate the errors on the measured attributes by perturbing the
galaxy parameters by their uncertainties. We repeat this process,
generating multiple individual new observations of each galaxy that are
subsequently combined into a final PDF, which can be used as desired to
estimate a single redshift and its associated error. In addition, our
implementation of this technique naturally incorporates data with
missing values and also provides extra meta information, such as an
unbiased estimate of the prediction error, a measure of the relative
importance of the parameters used in the photo-z estimation as a
function of redshift, an identification of regions where the training
data provide poor predictions, and an identification of galaxies that
are likely incorrectly outliers.

### Trees for Photo-Z

This work has been
[published](/papers/TPZ.html) by the
Monthly Notices of the Royal Astronomical Society

Title: Photometric Redshift Estimation
Slug: photoz-back
Date: 2014-01-03
Modified: 2014-01-06
Authors: Robert J. Brunner
Save_as: research/dmml/photoz/photoz-back.html
Tags: Data Mining, Machine Learning, Photometric Redshift, PDF
Type: background
Parent: photoz
Construction: True

<!-- PELICAN_BEGIN_SUMMARY -->

The estimation of galaxy redshifts using multi band photometry was first
performed by Baum (1962), while Koo (1985) and Loh & Spillar (1986) were
the first to compute galaxy redshifts by using digital photometric
observations from charge coupled devices. In the last two decades,
however, the estimation of redshifts from broadband photometry has grown
significantly. Broadly speaking, all of these techniques can be
categorized as either model-based or empirical-based.

<!-- PELICAN_END_SUMMARY -->

Fundamentally, the challenge of photometric redshift estimation is to
use the limited information provided by photometric observations to
reconstruct the true source redshift. In the figure below, we show (in
white) the spectrum of an elliptical galaxy (in dashed white, we show
the same galaxy spectrum as it would be observed if the same galaxy was
at a redshift of 0.4). Overlaid on this figure are the eight photometric
filters from the DEEP2 survey. Algorithmcally, we either need to sample
our models in the same manner as the observations to determine the best
fit model or we need to train an empirical technique to predict the
redshift from the limited photometric data.

<img src="{filename}/static/images/deep2_filt.png"
alt="Elliptical galaxy spectrum with DEEP2 photometric filters overlaid"
width="450px" height="auto" align="left"
display="block" style="margin-right: 60px;" />

The model-based algorithms (e.g., Benitez 2000; Bolzonella et al. 2000;
Csabai et al. 2003; Ilbert et al. 2006; Feldmann et al.. 2006) use
either empirical (e.g., Coleman et al. 1980) or synthetic spectral model
templates (e.g., Bruzual & Charlot 2003) to estimate a photometric
redshift by finding the best match between the observed magnitudes or
colors and the synthetic magnitude or colors from the templates that are
sampled across the expected redshift range of the photometric
observations.

Empirical-based methods use a spectroscopic training data set to
calibrate an algorithm that can be quickly applied to new photometric
observations. Initially the training set was used to map a polynomial
function between the colors and the redshift (e.g., Connolly et al.
1995; Brunner et al. 1997). More recently, this process has been
extended to machine learning algorithms, including artificial neural
networks (e.g., Collister & Lahav 2004; Oyaizu et al. 2008b), boosted
decision trees (e.g., Gerdes et al. 2010), random forest (e.g., Carliles
et al. 2010), nearest neighbors (e.g., Ball et al. 2007, 2008; Lima et
al. 2008), self-organized maps (e.g., Geach 2012; Way & Klose 2012),
spectral connectivity analysis (e.g., Freeman et al. 2009), Gaussian
process (e.g., Way et al. 2009; Bonfield et al. 2010), support vector
machines (e.g., Wadadekar 2005) or Quasi Newton Algorithm (e.g., Cavuoti
et al. 2012).

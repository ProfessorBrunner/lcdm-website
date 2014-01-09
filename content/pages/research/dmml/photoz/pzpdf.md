Title: Photo-z PDF Storage
Slug: pzpdf
Date: 2014-01-05
Modified: 
Authors: Matias Carrasco-Kind, Robert J. Brunner
Save_as: research/dmml/photoz/pzpdf.html
Tags: Data Mining, Machine Learning, Photometric Redshift, Python, PDF
Type: subproject
Parent: photoz
Construction: True
Summary: Exploring optimal storage techniques for photometric redshift probability density functions. 

## Storage Techniques for Photometric Redshift PDFs

A single photometric redshift probability density function (PDF) can be quite large, dpending on the redshift range covered by a photometric survey and the accuaracy of the sampled PDF. For a survey with resolution of $\deltaz = 0.02$ that covers $0 \leq z \leq 1.0$, we have fifty bins, which for 16 bit scaled integers requires 100 bytes. For larger redshift ranges, or higher numerical precision, the number of bytes becomes even larger.

If a survey computes multiple PDFs for billions of sources, the storage of the PDFs can easily become several TBs, which is both a stroage and a computation issue. 

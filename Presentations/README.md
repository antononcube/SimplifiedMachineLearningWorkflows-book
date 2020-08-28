# Presentations

## WTC-2019

Here is the Markdown version 
-- made with [M2MD](https://github.com/kubaPod/M2MD) -- 
of the presentation notebook:
- ["Anomalies, breaks, and outliers detection in time series"](./WTC-2019/Anomalies-breaks-and-outliers-detection-in-time-series.md).

Here is the abstract:

>In this presentation we show, explain, and compare methods for finding anomalies, breaks, and outliers in time series. 
We are interested in finding anomalies in both a single time series and a collection of time series.

>We (mostly) employ non-parametric methods. First, we look at some motivational examples from well known datasets.
Then we look into definitions of anomalies and definitions for measuring success of time series anomaly detection. 

>For a single time series we apply both WL built-in algorithms and additional, specialized algorithms. 
>We discuss in more detail algorithms based on K-Nearest Neighbors (KNN), Dimension Reduction, Linear Regression, Quantile Regression, Prefix Trees.

>For collections of time series we discuss: transformations into uniform representations, 
>simple outlier finding based on variables distributions, anomalous trends finding, anomalies finding with KNN, and other related algorithms.

>We are going to discuss how anomalies finding helps in producing faithful simulations of multi-variable datasets.

>Concrete, real life time series are used in the examples.

>See the related dedicated 
>[MathematicaVsR](https://github.com/antononcube/MathematicaVsR) 
>project 
>["Time series anomalies, breaks, and outliers detection"](https://github.com/antononcube/MathematicaVsR/tree/master/Projects/TimeSeriesAnomaliesBreaksAndOutliersDetection).

## UseR!-2020

Here is a video recording: 

- ["How to simplify Machine learning workflows specifications - useR! 2020 Conference" (YouTube)](https://youtu.be/QqH6eha73xk).

Here are the slides for the (lightning) talk:
[HTML](https://htmlpreview.github.io/?https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/blob/master/Presentations/UseR!-2020/How-to-simplify-ML-workflows-specifications-slides.html),
[Markdown](./UseR!-2020/How-to-simplify-ML-workflows-specifications-slides.md),
[Rmd](./UseR!-2020/How-to-simplify-ML-workflows-specifications-slides.Rmd).

Here is the (extended) abstract of the *proposed* presentation:

- ["How to simplify Machine learning workflows specifications?"](https://htmlpreview.github.io/?https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/blob/master/Presentations/UseR!-2020/How-to-simplify-ML-workflows-specifications.nb.html). 

Versions:
[HTML](https://htmlpreview.github.io/?https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/blob/master/Presentations/UseR!-2020/How-to-simplify-ML-workflows-specifications.nb.html), 
[Rmd](./UseR!-2020/How-to-simplify-ML-workflows-specifications.Rmd).
 
Here is the *submitted* abstract:

> In this presentation we discuss a systematic approach of software development
that gives us the ability to rapidly specify Machine Learning (ML) computations
using both programming Domain Specific Languages (DSL's) and natural language commands.
We present in detail the selection of programming paradigms, languages, and packages.

>A central topic of the presentation is the transformation of sequences of natural 
commands into corresponding DSL pipelines for ML computations. 

>We use monadic programming and code generation for implementation of ML packages.
We use Raku (Perl 6) for grammar specifications, parsers generation, and interpreters.

>Numerous examples are used based on ML packages written in R
and English-based grammar rules. We look into code generation 
of ML workflows for supervised learning, time series analysis, latent semantic analysis, 
and recommendations. We show how with the same natural commands pipelines in other
programming languages can be generated.

>Finally we discuss the extensions of the presented approach to (1) handling wrong commands and
spelling mistakes, (2) using multiple natural languages, and (3) making conversational agents.

## RStudio::global (2021)

Here is the call for talks page: 
["rstudio::global() call for talks"](https://blog.rstudio.com/2020/07/17/rstudio-global-call-for-talks/).

Here is the *submitted* abstract:

**TITLE:** Multi-language Data Wrangling Translations

**ABSTRACT:**

We want to facilitate the rapid specification of data wrangling workflows using natural language commands.

Here are our primary motivation points:

- Often we have to apply the same data transformation workflows within different
  programming languages and/or packages. 
  
- Although the high-level data transformation workflows are the same, it might be time consuming
  to express those workflows in the logic and syntax of concrete programming languages or packages.
  
- It would be nice to have software solutions that speed-up the processes for
  multi-language expression of data transformation workflows.

In this presentation we demonstrate the data wrangling code generation for different programming languages, using different packages. 
We focus on these three data wrangling packages:

- R-base
- R-tidyverse
- Python-pandas

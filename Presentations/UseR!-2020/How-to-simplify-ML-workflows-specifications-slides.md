---
title: ""
author: "Anton Antonov"
header-includes: "useR! 2020 Conference"
output:
  slidy_presentation:
     css: userstyle.css
     footer: "useR! 2020 Conference, lightning talk"
     keep_md: TRUE
---



## How to simplify Machine Learning workflows specifications?

### *useR! 2020 Conference, lightning talk*

**Anton Antonov**   
*Senior Research Scientist*   
*Accendo Data LLC*   
*https://github.com/antononcube*    

<img src="userlogo.png" width="300"/>


## What is this about?

Rapid specification of Machine Learning (ML) workflows using natural language commands.

The easiest things to automate with ML are ML workflows. 

This presentation demonstrates that with interfaces based on natural language commands.


## Motivation

Assume that:

1. We want to create conversation agents that help Data Science (DS) and ML 
practitioners to quickly create first, initial versions of different DS and ML workflows 
for different programming languages and related packages. 

2. We expect that the initial versions of programming code are tweaked further.
(In order to produce desired outcomes in the application area of interest.)



## The workflows considered

In this presentation we focus on these three ML areas:

- Quantile Regression (QR)

- Latent Semantic Analysis (LSA)

- Recommendations



## First example data

Assume we have a data frame with temperature data. 
Here is a summary:


```r
summary(dfTemperatureData)
```

```
##       Time            Temperature   
##  Min.   :3.629e+09   Min.   : 4.72  
##  1st Qu.:3.661e+09   1st Qu.:19.67  
##  Median :3.692e+09   Median :23.33  
##  Mean   :3.692e+09   Mean   :22.28  
##  3rd Qu.:3.724e+09   3rd Qu.:26.11  
##  Max.   :3.755e+09   Max.   :31.17
```


```r
ggplot2::ggplot(dfTemperatureData) + ggplot2::geom_point( ggplot2::aes( x = Time, y = Temperature ) )
```

![](How-to-simplify-ML-workflows-specifications-slides_files/figure-slidy/unnamed-chunk-2-1.png)<!-- -->



## Quantile Regression worfklow: first example

Here is a Quantile Regression (QR) workflow specification:


```r
qrmon2 <- 
  eval( expr = to_QRMon_R_command( 
    "create from dfTemperatureData;
     compute quantile regression with 12 knots and probabilities 0.25, 0.5, and 0.75;
     show date list plot with date origin 1900-01-01;", parse = TRUE) )
```

![](How-to-simplify-ML-workflows-specifications-slides_files/figure-slidy/unnamed-chunk-3-1.png)<!-- -->


## How it is done?

For a given ML domain (like QR or LSA) we create two types of Domain Specific Languages (DSL's):

1. a software monad (i.e. programming language pipeline package) and 

2. a DSL that is a subset of a spoken language.

These two DSL's are combined: the latter translates natural language commands into the former.

By executing those translations we interpret commands of spoken DSL's into ML computational results.

Note, that we assume that there is a separate system that converts speech into text.


## Development cycle

Here is a clarification diagram:

![MonadicMakingOfMLConversationalAgents](https://github.com/antononcube/ConversationalAgents/raw/master/ConceptualDiagrams/Monadic-making-of-ML-conversational-agents.jpg)


## Grammars and parsers

For each type of workflow is developed a specialized DSL translation [Raku](https://raku.org) module.

Each Raku module:

1. Has grammars for parsing a sequence of natural commands of a certain DSL

2. Translates the parsing results into corresponding software monad code

Different programming languages and packages can be the targets of the DSL translation.

(At this point are implemented DSL-translators to Python, R, and Wolfram Language.)

Here is an [example grammar](https://github.com/antononcube/ConversationalAgents/blob/master/Packages/Perl6/QuantileRegressionWorkflows/lib/QuantileRegressionWorkflows/Grammar.pm6). 


## Quantile Regression workflow: translation

Here is how a sequence of natural commands that specifies a QR workflow
is translated into code for a QR software monad:


```r
qrExpr <- 
  to_QRMon_R_command( 
    "create from dfTemperatureData;
     compute quantile regression with knots 12 and probabilities 0.05, 0.95;
     find outliers;", parse = FALSE )
qrExpr
```

```
## [1] "QRMonUnit( data = dfTemperatureData) %>%"                            "QRMonQuantileRegression(df = 12, probabilities = c(0.05, 0.95)) %>%"
## [3] "QRMonOutliers() %>% QRMonOutliersPlot()"
```


## Quantile Regression workflow: evaluation

Here we evaluate the generated QR monad code:


```r
qrmon2 <- eval(expr = parse( text = paste(qrExpr)))
```

```
## Warning in QRMonSetData(res, data): The argument data is expected to be a data frame with columns: { Regressor, Value }.
```

```
## Warning in QRMonSetData(res, data): Proceeding by renaming the first columm "Time" as "Regressor" and renaming the second columm "Temperature" as "Value".
```

![](How-to-simplify-ML-workflows-specifications-slides_files/figure-slidy/unnamed-chunk-5-1.png)<!-- -->

## Latent Semantic Analysis workflow: translation

Here is how a sequence of natural commands that specifies a LSA workflow
is translated into code for a LSA software monad:


```r
lsaExpr <- 
  to_LSAMon_R_command( 
    "create from textHamlet;
     make document term matrix with automatic stop words and without stemming;
     apply lsi functions global weight function idf, local term weight function none, normalizer function cosine;
     extract 12 topics using method SVD, max steps 120, and min number of documents per term 2;
     show thesaurus table for ghost and grave;", parse = FALSE  )
lsaExpr
```

```
## [1] "LSAMonUnit(textHamlet) %>%"                                                                                                         
## [2] "LSAMonMakeDocumentTermMatrix( stopWords = NULL, stemWordsQ = FALSE) %>%"                                                            
## [3] "LSAMonApplyTermWeightFunctions(globalWeightFunction = \"IDF\", localWeightFunction = \"None\", normalizerFunction = \"Cosine\") %>%"
## [4] "LSAMonExtractTopics( numberOfTopics = 12, method = \"SVD\",  maxSteps = 120, minNumberOfDocumentsPerTerm = 2) %>%"                  
## [5] "LSAMonEchoStatisticalThesaurus( words = c(\"ghost\", \"grave\"))"
```


## Latent Semantic Analysis workflow: evaluation

Here we execute the generated LSA monad code:


```r
lsamon2 <- eval(expr = parse( text = paste(lsaExpr)))
```

```
## Warning in NonNegativeMatrixFactorization::NearestWords(lsaObj$H, word, : More that one column name corresponds to the search word; the first match is used.
```

```
##    SearchTerm Word.Distance Word.Index Word.Word
## 1       ghost  0.0000000000        623     ghost
## 2       ghost  2.7104585243         27     again
## 3       ghost  3.0329619792        513    father
## 4       ghost  3.1748348980       1465     stage
## 5       ghost  3.2285530964       1644     under
## 6       ghost  3.2393851854        319     cries
## 7       ghost  3.3816775817       1312         s
## 8       ghost  3.4975218903       1512     swear
## 9       ghost  3.5203690983        935       mar
## 10      ghost  3.5864016626        744       hor
## 11      ghost  3.5865925495       1550      thee
## 12      ghost  3.5899890210       1587       thy
## 13      grave  0.0000000000        648     grave
## 14      grave  0.0002163256         60       any
## 15      grave  0.0002283049       1597    tongue
## 16      grave  0.0002401747        151    better
## 17      grave  0.0002528864        741    honour
## 18      grave  0.0002926401       1317      said
## 19      grave  0.0003375491       1419     sleep
## 20      grave  0.0003536033        897      long
## 21      grave  0.0003747190       1251    reason
## 22      grave  0.0004035973       1362      sent
## 23      grave  0.0004207916       1735     while
## 24      grave  0.0004210154       1288      ring
```


## Recommender workflow: data 

Consider the making of a recommender over the Titanic data:


```r
dfTitanic[sample(1:nrow(dfTitanic), 12), ]
```

```
##           id passengerClass passengerAge passengerSex passengerSurvival
## 609   id.609            3rd           30         male              died
## 335   id.335            2nd           30         male              died
## 1105 id.1105            3rd           20         male              died
## 330   id.330            2nd           40       female          survived
## 1292 id.1292            3rd           -1         male              died
## 17     id.17            1st           20         male              died
## 472   id.472            2nd           40       female          survived
## 410   id.410            2nd           40         male              died
## 666   id.666            3rd           20       female              died
## 929   id.929            3rd           -1       female              died
## 949   id.949            3rd           -1         male              died
## 171   id.171            1st           50         male          survived
```


```r
summary(as.data.frame(unclass(dfTitanic), stringsAsFactors = TRUE))
```

```
##        id       passengerClass  passengerAge   passengerSex passengerSurvival
##  id.1   :   1   1st:323        Min.   :-1.00   female:466   died    :809     
##  id.10  :   1   2nd:277        1st Qu.:10.00   male  :843   survived:500     
##  id.100 :   1   3rd:709        Median :20.00                                 
##  id.1000:   1                  Mean   :23.55                                 
##  id.1001:   1                  3rd Qu.:40.00                                 
##  id.1002:   1                  Max.   :80.00                                 
##  (Other):1303
```

## Recommender workflow

Here are recommender workflow specification and evaluation results:


```r
smrmon2 <- 
  eval( expr = to_SMRMon_R_command( 
    "create from dfTitanic; 
     apply the LSI functions inverse document frequency, term frequency, and cosine;
     compute the top 6 recommendations for the profile female=1, 30=1; 
     extend recommendations with dfTitanic;
     show pipeline value", parse = TRUE ) )
```

```
##   Score Index      id passengerClass passengerAge passengerSex passengerSurvival
## 1     2     1    id.1            1st           30       female          survived
## 2     2    33 id.1027            3rd           30       female          survived
## 3     2    68 id.1059            3rd           30       female              died
## 4     2    72 id.1062            3rd           30       female          survived
## 5     2    99 id.1087            3rd           30       female              died
## 6     2   108 id.1095            3rd           30       female          survived
```


## Handling misspellings

The approach taken in the design and implementation of the natural language commands interpreters 
can handle misspellings:


```r
smrmon2 <- 
  eval( expr = to_SMRMon_R_command( 
    "create from dfTitanic; 
     aply the LSI functions inverse document frequency, term frequency, and cosine;
     compute the top 6 recomendations for the profle female=1, 30=1; 
     extend recommendations with dfTitanic;
     show pipeline value" ) )
```

```
## [1] "Possible misspelling of 'apply' as 'aply'."                     "Possible misspelling of 'recommendations' as 'recomendations'."
## [3] "Possible misspelling of 'profile' as 'profle'."                
##   Score Index      id passengerClass passengerAge passengerSex passengerSurvival
## 1     2     1    id.1            1st           30       female          survived
## 2     2    33 id.1027            3rd           30       female          survived
## 3     2    68 id.1059            3rd           30       female              died
## 4     2    72 id.1062            3rd           30       female          survived
## 5     2    99 id.1087            3rd           30       female              died
## 6     2   108 id.1095            3rd           30       female          survived
```

## Not just ML workflows

Obviously this approach can be used for any type of computational workflows.

Here is an example of an Epidemiology Modeling workflow:


```r
ecmCommands <- 
'create with the model susceptible exposed infected two hospitalized recovered;
 assign 100000 to the susceptible population;
 set infected normally symptomatic population to be 0;
 set infected severely symptomatic population to be 1;
 assign 0.56 to contact rate of infected normally symptomatic population;
 assign 0.58 to contact rate of infected severely symptomatic population;
 assign 0.1 to contact rate of the hospitalized population;
 simulate for 240 days;
 plot populations results;'
```


```r
to_ECMMon_R_command(ecmCommands, parse = TRUE)
```

```
## expression(ECMMonUnit(model = SEI2HRModel()) %>% ECMMonAssignInitialConditions(initConds = c(SPt = 1e+05)) %>% 
##     ECMMonAssignInitialConditions(initConds = c(INSPt = 0)) %>% 
##     ECMMonAssignInitialConditions(initConds = c(ISSPt = 1)) %>% 
##     ECMMonAssignRateValues(rateValues = c(contactRateINSP = 0.56)) %>% 
##     ECMMonAssignRateValues(rateValues = c(contactRateISSP = 0.58)) %>% 
##     ECMMonAssignRateValues(rateValues = c(contactRateHP = 0.1)) %>% 
##     ECMMonSimulate(maxTime = 240) %>% ECMMonPlotSolutions(stocksSpec = ".*Population"))
```


```r
ecmmon2 <- eval( to_ECMMon_R_command(ecmCommands) )
```

![](How-to-simplify-ML-workflows-specifications-slides_files/figure-slidy/unnamed-chunk-14-1.png)<!-- -->

## References

### Repositories

[AAr1] Anton Antonov, [R-packages](https://github.com/antononcube/R-packages), (2019), GitHub.

[AAr2] Anton Antonov, [Conversational Agents](https://github.com/antononcube/ConversationalAgents), (2017), GitHub.

### Packages

[AAp1] Anton Antonov, 
[Quantle Regression Monad in R](https://github.com/antononcube/QRMon-R), 
(2019),
GitHub.

[AAp2] Anton Antonov, 
[Latent Semantic Analysis Monad in R](https://github.com/antononcube/R-packages/tree/master/LSAMon-R), 
(2019),
[R-packages at GitHub](https://github.com/antononcube/R-packages).

[AAp3] Anton Antonov, 
[Sparse Matrix Recommender Monad in R](https://github.com/antononcube/R-packages/tree/master/SMRMon-R), 
(2019),
[R-packages at GitHub](https://github.com/antononcube/R-packages).

[AAp4] Anton Antonov, 
[Epidemiology Compartmental Modeling Monad in R](https://github.com/antononcube/ECMMon-R), 
(2020),
GitHub.
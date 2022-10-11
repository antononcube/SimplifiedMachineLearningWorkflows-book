# Mermaid-JS flowcharts

Anton Antonov   
Vanna-do    
[SimplifiedMachineLearningWorkflows-book at GitHub](https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book)   
September-October 2022    

-----

## Introduction

This document has flowcharts specified using the Domain Specific Language (DSL) of
[mermaid-js](https://mermaid-js.github.io).

In web browsers GitHub produces diagrams corresponding to mermaid-js specifications.
One can also use https://mermaid.live/ .


------

## Data transformations

```mermaid
graph LR
    a([English])
    b([Bulgarian])
    c([Raku])
    d([R-tidyverse])
    e([Python-pandas])
    f{{"Interpreter (Raku)"}}
    g([Julia])
    h([Python])
    i([R])
    j([WL])
    k([SQL])
    l([Raku])
    g1>DataFrames]
    h1>pandas]
    i1>base]
    i2>tidyverse]
    i3>data.table]
    j1>System]
    k1>MySQL]
    k2>PostgreSQL]
    l1>Reshapers]
    l2>Red]
    l3>Dan]
    subgraph .
        f1([Bulgaian])
        f2([English])
        f3([Korean])
        f4([Russian])
        f5([Spanish])
    end
    a & b & c & d & e -->f
    f-->g & h & i & j & k & l
    g-->g1
    h-->h1
    i-->i1 & i2 & i3
    j-->j1
    k-->k1 & k2
    l-->l1 & l2 & l3
    f---->f1
    style c #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style d #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style e #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style i3 #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style k1 #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style k2 #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style l2 #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    style l3 #,stroke:stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

-----

## Classification workflows

### Competition classifiers mind-map

```mermaid
graph LR
a[Making competitions classifiers]
b1[Competition organization]
c1[Judges]
c2[Submissions management]
d1[Give training set]
d2[Withold test set]
d3[Submission logs]
d4[Score calculation]
d5[Verificiation]
e1[Judges training dataset]
e2[Competitors know the labels]
e3[Judges test dataset]
e4[Competitiors do *not* know the labels]
f[Submission preperation]
g1[Study]
g2[Make the competition classifier]
h1[Data analysis]
h2[Preliminary data transformations]
h3[Classifier training]
h4[Transform the judges training dataset according to findings in the study]
h5[Train a classifier with the method found to be best]
h6[Run the classifier over the judges test dataset]
h7[Submit the found tables]
i1[Summaries]
i2[Distribution charts]
i3[Mosaic plots]
i4[etc.]
i5[Categorical variables handling]
i6[Feature extraction]
i7[Dimension reduction]
i8[etc.]
i9[Optional]
i10[Do multiple times]
i11[Pick the best classifier and transformation]
j1[Come up with relevant data transformations]
j2[Come up with different feature engineering procedures]
j3[Split the judges training dataset]
j4[Train classifiers]
j5[Classifier measurements]
k1[Training dataset]
k2[Test dataset]
k3[Different data transformations]
k4[Different classifer algorithms]
k5[Accuracy, Precision, Recall]
k6[Confusion matrix]
k7[ROC]
k8[etc.]
a-->b1-->c1 & c2
c1-->d1 & d2
c2-->d3 & d4 & d5
d1-->e1 & e2
d2-->e3 & e4
a-->f
f-->g1 & g2
g1-->h1 & h2 & h3
g2-->h4 & h5 & h6 & h7
h1-->i1 & i2 & i3 & i4
h2-->i5 & i6 & i7 & i8
h3-->i9 & i10 & i11
i9-->j1 & j2
i10-->j3 & j4 & j5
j3-->k1 & k2
j4-->k3 & k4
j5-->k5 & k6 & k7 & k8
e1-.->g1
e3-.->g2
h7-.->c2
h4-->h5-->h6-->h7
```

### Workflow

```mermaid
graph TB
    a[/Data specification/]
    b[Take the specific dataset]
    c[(Data repository)]
    d[Transform data]
    e[Compute summary statistics]
    f{Do the data assumptions hold?}
    g>Display of intermediate results]
    g1[/Failure/]
    g2[Take training, testing, and optional validation subsets]
    h[[Train a classifier]]
    h1[[Compute classifier measurements]]
    i{Too many classifer trainings?}
    j{Acceptable accuracy?}
    k[/Accuracy, precision, ROC/]
    l[/Classifier specification/]
    a-->b
    b-->d
    b-.->c
    c-.->b
    d-->e
    e-->f
    e-.->g
    g-.->e
    f--No-->g1
    f--Yes--->g2
    g2-->h
    h-->h1
    h1-->i
    i--No--->j
    j--No-->h
    j--Yes-->k
    l-->h
    i--Yes--->g1
    g-...->h
    h-.->g
```

------

## Latent Semantic Analysis workflows

### Workflow flowchart

```mermaid
graph TB
 a[/Text data/]
 b[Process text data]
 b1[[Remove stop words]]
 b2[[Remove unacceptable words]]
 b3[[Stem words]]
 c[Linear Vector Space representation]
 c1[[Make document-term contingency matrix]]
 d{Do the data assumptions hold?}
 e[/Assumptions Failure/]
 e1>Display summary statistics]
 f[Apply Latent Semantic Indexing functions]
 g[Map queries and new documents into the space of terms]
 h{Too many topic extractions?}
 i{Too many full pipeline executions?}
 i1[/Failure/]
 j[/Topic extraction parameters specification/]
 k[Extract topics]
 l[Display topics by their top words]
 m[Display statistical thesaurus for a suitable set of words]
 n{Acceptable topics and thesaurus?}
 n1[Map queries and new documents into the space of topics]
 n2[Tag each documents, find tags representation by topics]
 n3[Association or similarity graphs by topics representation]
 n4[Find most important documents]
a-->b--->c--->d
d--Yes-->f-->h
h--No-->j-->k-->l-->m-->n
n--Yes--->n1 & n2 & n3 & n4
n--No-->h
h--Yes--->i
i--Yes-->i1
i--No-->b
b-.->b1 & b2 & b3
b1 & b2 & b3 -..->b
c-.->c1
c1-.->c
c-.->e1
e1-.->c
e-.->e1
e-.->d
d--No-->e
f-->g
```

### Pipeline flowchart

```mermaid
graph TB
 subgraph one
 a[(LSAMon context)]
 b((LSAMon pipeline value)) 
 end
 subgraph LSAMon monad pipeline 
 c[LSAMonMakeDocumentTermMatrix]
 d[LSAMonApplyTermWeightFunctions]
 e[LSAMonExtractTopics]
 f[LSAMonEchoTopicsTable]
 g[LSAMonEchoStatisticalThesaurus]
 h[LSAMonTopicsRepresentation]
 end
 i[/_?VectorQ_Association/]
 j>Echo output]
 k[/_?SSparseMatrixQ/]
 l[documents, documentTermMatrix, weightedDocumentTermMatrix, terms, W, H, topicsTable, statisticalThesaurus]
 c-->d-->e-->f-->g-->h
i-->c
h-->k
f & g--->j
c-.documenttermMatrix.->a
d-.weightedDocumentTermMatrix.->a
e-.W,H.->a
f-.topicTable.->a
g-.statisticalThesaurus.->a
a-.Keys.->l
```

------

## Quantile regression

```mermaid
graph TB
 a[/Data specification/]
 b[Take the specified dataset]
 b1[(Data repository)]
 c[Transform data]
 c1[[Extract paths from time series objects]]
 c2[[Delte rows with missing values]]
 c3[[Rescale]]
 c4[[Moving average or map]]
 d[Compute summary statistics]
 d1>Display of intermediate results]
 e{Do the data assumptions hold?}
 e1[/Failure/]
 f{Too many fittings?}
 f1{Acceptable result?}
 g[/Regression parameters specification/]
 h[Regression fit]
 i[Plot data and regression curves]
 j{Acceptable fit?}
 k[Pick a preoblem and related task]
 k1[Find and plot errors]
 k2[Find and plot outliers]
 k3[Simulate and plot time series]
 k4[Find and plot conditional CDF's]
 k5[Find and plot local extrema]
 a-->b---->c-->d--->e
 b-.->b1
 c-.->c1 & c2 & c3 & c4
 c1 & c2 & c3 & c4-.->c
 e--No-->e1
 e--Yes-->f
 f--Yes-->e1
 f--No-->g-->h-->i-->j
 j--No-->f
 j--Yes-->k
 k-->k1 & k2 & k3 & k4 & k5
 k1 & k2 & k3 & k4 & k5-->f1
 f1--No-->f
 d1-.->d & c
 d & c-..->d1
```

-------

## Recommender workflows

```mermaid
graph TB
 a[/Dataset/]
 b[Create item-tag contingency matrices and recomendation matrix]
 b1[[Make contingency matrices from long form dataset]]
 b2[[Make contingency matrices from wide form dataset]]
 c[Reshape recommendation matrix]
 c1[/Items, tags, or filter specifications/]
 d[Extract properties or compute summary statistics]
 d1>Display intermediate results]
 e{Do data assumptions hold?}
 e1[/Failure/]
 f[Apply Latent Semantic Indexing functions]
 f1[Find history reccomendations]
 f2[Provide reccomendations explaination/proofs]
 f3[/Scored history items/]
 f4[Find profile]
 g[Find profile recommedations]
 g1[/Scored profile tags/]
 g2[Classify]
 h[Join recommendations with additional data]
 i>Display results]
 j{Do results make sense?}
 j1[/Failure/]
 j2[Compute Learning To Tank statistics]
 j3[Create interactive interface for recommendation explorations]
    a-->b-->c-->d-->e
    b-.-b1 & b2
    c1-->c
    d-.->d1
    d1-.->d
    e--Yes-->f-->g-->h
    e--No-->e1
    f-->f1-->f2
    f3-->f1 & f4
    f1--->h
    h-.->i
    i-->j
    j--No-->j1
    j--Yes-->j2 & j3
    g1-->g2-.->i
    g1-->g
    g & f1 & f2 & f4-..->i
```

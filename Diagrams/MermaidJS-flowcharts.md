# Mermaid-JS flowcharts

##### Anton Antonov
##### Vanna-da
##### September-October 2022

## Classification workflows

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
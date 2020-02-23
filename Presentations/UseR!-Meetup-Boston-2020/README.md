# Latent Semantic Analysis Workflows 
***useR! Meetup Boston, April 2020***   
***Extended abstract***


## In brief

In this (tutorial) presentation we are going to:
1. Overview Latent Semantic Analysis (LSA) typical problems and basic workflows
2. Discus philosophical, scientific, and mathematical justifications
3. Discuss the theory behind the dimensional reduction algorithms used (ICA, NNMF, SVD) and how they compare
4. Follow LSA's application to document collections in more detail
5. See various LSA applications: search engines support, natural language translations,
image classification, and others. 

The presentation is based on the (monadic) R package 
[LSAMon-R](https://github.com/antononcube/R-packages/tree/master/LSAMon-R), \[AAp1\].

It is emphasized that the presented LSA worfklows are universal and can be used within any powerful enough 
programming language.

 
## Part 1 - Overview (25 min)

In the first part we are going to clarify the basics of LSA's theory and methodology by providing answers to 
the questions in the following list.

   - What are the typical applications of LSA?   
   - Why use LSA?     
   - What it the fundamental philosophical or scientific assumptions for LSA?   
   - What is the most important and/or fundamental step of LSA?   
   - What is the difference between LSA and Latent Semantic Indexing (LSI)?   
   - What are the alternatives?
     - Using Neural Networks instead?   
   - How is LSA used to derive similarities between two given texts?   
   - How is LSA used to evaluate the proximity of phrases?
     (That have different words, but close semantic meaning.)   
   - How the main dimensional reduction methods compare? 

### Dimensional reduction algorithms

Here is a list of the 
[Dimensional reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction) 
algorithms discussed in the tutorial (and used by `LSAMon`):
- [Independent Component Analysis](https://en.wikipedia.org/wiki/Independent_component_analysis),
- [Non-Negative Matrix Factorization (NNMF)](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization),
- [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition).

(The most important is NNMF; one of the primary reasons for developing "LSAMon-R" is to streamline applications of NNMF.)


## Part 2 - Applications (25 min)

In the second part of the tutorial were a going to look into concrete applications
derived from different practical uses cases. 
(From the domains of digital content consumption, logistics, academic research, and others.)  

A list of LSA applications examples follows.
 
- Utilize LSA for document similarities evaluations.  
  (Like ["Conference Abstracts Similarities"](https://htmlpreview.github.io/?https://github.com/antononcube/MathematicaVsR/blob/master/Projects/ConferenceAbstactsSimilarities/R/ConferenceAbstractsSimilarities.nb.html).)

- Apply LSA to image classification.
  (Like ["Handwritten digits classification by matrix factorization"](https://cdn.rawgit.com/antononcube/MathematicaVsR/master/Projects/HandwrittenDigitsClassificationByMatrixFactorization/R/HandwrittenDigitsClassificationByMatrixFactorization.html).) 

- Apply LSA to [Great Conversation](https://en.wikipedia.org/wiki/Great_Conversation) studies.

- Derive a custom taxonomy over a document collection.

- Use LSA for translation of natural languages.

- Use LSA for making or improving search engines.

- (Others...)

## The software monad 

Here is a basic `LSAMon` pipeline example:

```r
LSAMonUnit( texts ) %>% 
  LSAMonMakeDocumentTermMatrix( stemWordsQ = FALSE, stopWords = stopwords::stopwords() ) %>% 
  LSAMonApplyTermWeightFunctions( globalWeightFunction = "IDF", localWeightFunction = "TermFrequency", normalizerFunction = "Cosine" ) %>% 
  LSAMonExtractTopics( numberOfTopics = 24, minNumberOfDocumentsPerTerm = 200, method = "NNMF", maxSteps = 12 ) %>%
  LSAMonEchoTopicsTable( numberOfTerms = 10 )
```

The `LSAMon` pipeline above corresponds to the following sequence of natural language commands:

```
create from texts;
make document term matrix with stemming FALSE and automatic stop words;
apply LSI functions global weight function IDF, local term weight function TermFrequency, normalizer function Cosine;
extract 12 topics using method NNMF and max steps 12 and 200 min number of documents per term;
show topics table with 10 terms;
``` 
 
## Data 

(Most of) the data used is available 
[here](../../Data). 

## Flow chart

Here is a flow chart diagram for the typical LSA workflows:

![LSAWorkflows](../../Part-2-Monadic-Workflows/Diagrams/A-monad-for-Latent-Semantic-Analysis-workflows/LSA-workflows.jpg)


## References

\[AAt1\] Anton Antonov, 
[Wolfram-U Latent Semantic Analysis live-coding sessions](https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/tree/master/Tutorials/WolframU-LSAMon-workflows).

\[AAp1\] Anton Antonov, 
[Latent Semantic Analysis Monad in R](https://github.com/antononcube/R-packages/tree/master/LSAMon-R), 
(2019),
[R-packages at GitHub](https://github.com/antononcube/R-packages). 

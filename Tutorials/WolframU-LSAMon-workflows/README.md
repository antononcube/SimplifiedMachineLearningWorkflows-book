# Wolfram U Latent Semantic Analysis workflows lectures

## In brief

The lectures on 
[Latent Semantic Analysis (LSA)](https://en.wikipedia.org/wiki/Latent_semantic_analysis) 
are to be recorded through Wolfram University (Wolfram U) in December 2019 and January-February 2020.

-----

## The lectures (as live-coding sessions)

### 1. [X] Overview Latent Semantic Analysis (LSA) typical problems and basic workflows

Answering preliminary anticipated questions.     

Here is 
[the recording of the first session at YouTube](https://www.youtube.com/watch?v=d5M54_9AMVQ) .
   
- What are the typical applications of LSA?   
- Why use LSA?     
- What it the fundamental philosophical or scientific assumption for LSA?   
- What is the most important and/or fundamental step of LSA?   
- What is the difference between LSA and Latent Semantic Indexing (LSI)?   
- What are the alternatives?
  - Using Neural Networks instead?   
- How is LSA used to derive similarities between two given texts?   
- How is LSA used to evaluate the proximity of phrases?
  (That have different words, but close semantic meaning.)   
- How the main dimension reduction methods compare?
      
------

### 2. [X] LSA for document collections

Here is [the recording of the second session at YouTube](https://www.youtube.com/watch?v=5pX5WAfPNb8).

- Motivational example -- full blown LSA workflow.
    
- Fundamentals, text transformation (the hard way):
  - bag of words model,
  - stop words,
  - stemming.

- The easy way with 
  [LSAMon](https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/blob/master/Part-2-Monadic-Workflows/A-monad-for-Latent-Semantic-Analysis-workflows.md).

- "Eat your own dog food" example.

------

### 3. [X] Representation of the documents - the fundamental matrix object

Here is [the recording of the third session at YouTube](https://www.youtube.com/watch?v=MNQR28P8Juc).
   
- Review: last session's example.
   
- Review: the motivational example -- full blown LSA workflow.

- Linear vector space representation:
  - LSA's most fundamental operation,
  - matrix with named rows and columns.

- Pareto Principle adherence
  - for a document,
  - for a document collection, and
  - (in general.)

------

### 4. [X] Representation of unseen documents

Here is [the recording of the fourth session at YouTube](https://www.youtube.com/watch?v=ElwOLyd9GC4).
   
- Review: last session's matrix object.
  - Sparse matrix with named rows and columns.

- Queries representation.
  
  - Representing 
    [rstudio-conf-2019 abstracts](../../Data/RStudio-conf-2019-abstracts.json)
    in the vector space of 
    [WTC-2019 abstracts](../../Data/Wolfram-Technology-Conference-2019-abstracts.json).

- Making a search engine for
  
  - [ ] [Raku's documentation](https://github.com/Raku/doc),    
  - [X] WTC-2019 abstracts.

- Dimension reduction over an image collection.

  - Topics over [random mandalas](https://resources.wolframcloud.com/FunctionRepository/resources/RandomMandala).
  - Representation of unseen mandala images.

------

### 5. [X] LSA for image de-noising and classification

Here is [the recording of the fifth session at YouTube](https://www.youtube.com/watch?v=_KBecGdzoS0).
   
- Review: last session's image collection topics extraction.
  - Let us try that two other datasets:
    - handwritten digits, and
    - [Hentaigana](https://en.wikipedia.org/wiki/Hentaigana) (maybe).
        
- Image de-noising: 
  - Using handwritten digits (again).
     
- Image classification:
  - Handwritten digits.
   
------

### 6. [X] Further use cases

Here is [the recording of the sixth session at YouTube](https://www.youtube.com/watch?v=Hxawq1O3Oec).

- Derive a custom taxonomy over a document collection.
  - Clustering with the reduced dimension.
- Apply LSA to Great Conversation studies.	
- Use LSA for translation of natural languages.
  - Using Dostoevsky's novel "The Idiot".
    - [Russian chapters breakdown](../../Data/Dostoyevsky-The-Idiot-Russian-chapters.json.zip).
    - [English chapters breakdown](../../Data/Dostoyevsky-The-Idiot-English-chapters.json.zip).
- Use LSA for making or improving search engines.
- LSA for time series collections.
     
   

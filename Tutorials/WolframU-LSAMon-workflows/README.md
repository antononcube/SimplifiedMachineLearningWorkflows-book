# Wolfram U Latent Semantic Analysis workflows lectures

## In brief

The lectures on 
[Latent Semantic Analysis (LSA)](https://en.wikipedia.org/wiki/Latent_semantic_analysis) 
are to be recorded through Wolfram University (Wolfram U) in December 2019 and January-February 2020.


## The lectures (as live-coding sessions)

1. [X] Overview Latent Semantic Analysis (LSA) typical problems and basic workflows.    
   Answering preliminary anticipated questions.     
   Here is 
   [the recording of the first session at Twitch](https://www.twitch.tv/videos/517562647) .
   
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
      
2. [X] LSA for document collections.   
   Here is [the recording of the second session at Twitch](https://www.twitch.tv/videos/523306241) .
   
    - Motivational example -- full blown LSA workflow.
    
    - Fundamentals, text transformation (the hard way):
        - bag of words model,
        - stop words,
        - stemming.

    - The easy way with 
      [LSAMon](https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/blob/master/Part-2-Monadic-Workflows/A-monad-for-Latent-Semantic-Analysis-workflows.md).

     - "Eat your own dog food" example.

3. [X] Representation of the documents - the fundamental matrix object.   
   Here is [the recording of the third session at Twitch](https://www.twitch.tv/videos/533991174) .
   
   - Review: last session's example.
   
   - Review: the motivational example -- full blown LSA workflow.

   - Linear vector space representation:
       - LSA's most fundamental operation,
       - matrix with named rows and columns.

   - Pareto Principle adherence
       - for a document,
       - for a document collection, and
       - (in general.)

4. [ ] Typical use cases.     

   - Representation of unseen documents.
   - Similarity between two text: 
     - the "local world" perspective, and 
     - the "bigger universe" perspective.
   - Dimension reduction methods comparisons.
   
5. [ ] LSA for image collections.

   - Representation of the documents.
   - Dimension reduction methods comparisons.
   - Representation of unseen documents.
   
6. [ ] Further use cases.

   - LSA based image classification.
   - LSA for time series collections.

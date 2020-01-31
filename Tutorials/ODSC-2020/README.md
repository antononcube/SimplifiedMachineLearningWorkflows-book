# Recommendation systems workflows

*(Here is the
[call for speakers](https://odsc.com/boston/call-for-speakers/) for
[Open Data Science Conference (ODSC) East 2020](https://odsc.com/boston/).)* 

## Title

Recommendation systems work-flows

## Abstract

In this tutorial we consider work-flows of typical recommendation systems.
We use both item-item and item-user recommenders. 

For clarity we use both programming code and sequences of natural language commands. 
We also introduce and exemplify the use of different recommender interactive interfaces.

The discussed recommender work-flows are constructed with dedicated R packages. 
We mostly use (monadic) pipeline specifications.

All parts of the tutorial are illustrated with a diverse set of examples based on 
the following types of data: digital content (books, movies, music), 
financial time series, document collections, retail invoices, medical data.

The following plan is (roughly) followed.

1. General set-up: problem formulation, scope, areas of focus.

2. Description of the standard work-flows followed by more advanced or 
specialized work-flows. 

3. Elements of the theory of different aspects of recommendations computation
algorithms and related interpretations. 

4. Demonstration of different extensions of recommendation systems for doing
Progressive learning and Time series collections analysis.
 
5. Discussion of the making of conversational agents that generate recommender 
work-flows. (Julia, Python, R, WL.)
 
## Detailed tutorial plan 

- General set-up.
   - The recommendation problem.
   - Approaches.
   - Recommendation systems types.

- Core work-flows.
   - Creation
      - Creation by contingency matrices.
      - Creation by specifications.
   - Categorization of numerical data.
   - LSI functions application.
   - Recommendation by history.
   - Recommendation by profile.
   - Explanations and proofs.
   - Recommendations re-ordering.
   - Cut-off selection by outlier identifiers.
   
- Further work-flows.
   - Tuning recommendations.
   - Recommendations breakdown.
   - Classification.
   - Anomalies identification.
   
- Computations theory.
   - Sparse Matrix Linear Algebra.
   - Using scored-lists / hash-maps.
   - Using graphs and centrality measures.
   - Pre-computation of nearest neighbors scored-lists. 
   - LSA and LSI utilization.
   - Designing more specialized and/or advanced algorithms.
     - Based on quick recommender computations.
   
- Recommender object transformations.
  - Joining two or more recommenders.
  - Reduction by predicates. 
  - Adding and removing sub-matrices / tag types.
  
- Application to Progressive learning.  
  - Incremental recommender enhancement.
  - Why it works?
  - Evaluation.
  - Examples.
  
- Time series search engine.
  - The general approach.
  - The special interactive interface.
  - Finding trends.
  - Finding nearest neighbours.
  
- Making an item-user recommender.
  - Bi-partite graph based.
  - Pure collaborative filtering.
  - Examples.
  
- Composite recommenders.
  - The Composite design pattern.
  - Normalization and weighted voting.
  
- Tags significance determination and Learning to rank. 

- Conversational agents for generating recommender work-flows.

- Summary and Q&A.
  



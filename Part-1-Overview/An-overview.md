# An overview

## Introduction

Some of the easiest things to automate with Machine Learning are Machine Learning and Data Science workflows.

This book shows how such automation can be systematically developed for several core Machine Learning
sub-cultures as Classification, Regression Analysis, Latent Semantic Analysis, Recommendations, 
Time Series feature extraction, Neural Networks.

We do the workflows automation by providing Domain Specific Languages (DSL's) for each of the considered ML sub-cultures.

In this chapter we give an overview of the workflows use in this book and what are the bigger contexts they belong to.

# The workflows within Machine Learning 

Machine Learning can be roughly divided into three parts:

- Supervised learning,

- Unsupervised learning, and

- Reinforcement learning.

In this book we deal with two Supervised learning workflows: Classificaton and Neural Networks.
The rest are Unsupervised leaning workflows: Regression Analysis, Latent Semantic Analysis, Recommendations, and 
Time Series Feature Extraction belong. The approach taken in this can be applied also to Reinforcement learning workflows
and, more generally, to different Data Science tasks. (And throughout the book those kind of applications are briefly
discussed.)

## The end goal 

In this section we describe the software engineering context for the ML workflows in this book.

Consider the making of conversational agent that produces ML software code through 
natural language commands. The reasons to make such a conversational agent are two-fold:

- we want to quickly generate stencil code that embodies ML know-how,

- natural languages are not suitable for specifying technical details of algorithms,

- well designed software code (a DSL) can provide rapid computations specification, and
 
- sufficient control of related tuning parameters.

In other words we are making a conversational agent for generating software code that makes Data Scientists 
lives easier; we are not making a conversational agent that provides ML functionalities to laypersons.

Programming-wise we extensively use 
[Software Monad](https://en.wikipedia.org/wiki/Monad_(functional_programming)) 
designs to make programming languages DSL's and 
[Extended Backus-Naur Form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
grammar specifications to make natural language DSL's. 
For more details of applying that approach using Wolfram Language (WL) see \[AA1\].

### Workflow example

TBD...

### The strategy

Here is the a diagram that outlines the strategy proposed and carried out in this book.

![Monadic-making-of-ML-conversational-agents](https://github.com/antononcube/ConversationalAgents/raw/master/ConceptualDiagrams/Monadic-making-of-ML-conversational-agents.jpg)

Let us describe the methodology given in the diagram above. 
TBD...


## Example a Quantile Regression workflow

TBD...

## Cross-workflow combinations and pipelines

TBD...

## References

[AA1] Anton Antonov, 
[Software Design Methods with Wolfram Language](https://github.com/antononcube/SoftwareDesignMethodsWithWL-book), 
2020, GitHub.

[JB1] John Backus, "Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs",
(1978), Association for Computing Machinery.







  
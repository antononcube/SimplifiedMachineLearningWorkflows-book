# Data transformation workflows

## General description

The Data Transformation (DT) lectures outlined below are *to be* recorded for 
[Wolfram U](https://www.wolfram.com/wolfram-u/) 
in October-December 2020.

- Each tutorial lecture is between 25 and 40 minutes.

- Most of the workflows in the lectures have (easy to derive) corresponding code in the programming languages: Julia, Python, R, and WL.
  (In Python and Julia dedicated data transformation packages are utilized.)

- For didactic purposes we are going to use the Domain Specific Language (DSL) 
[Raku](https://www.raku.org)-programmed 
system 
[DSL::English::DataQueryWorkflows](https://github.com/antononcube/Raku-DSL-English-DataQueryWorkflows), \[AAp1\], 
that generates code for the programming languages R and WL and 
the software packages:
  - [Julia-DataFrames](http://juliadata.github.io/DataFrames.jl/stable/) 
  - [Python-pandas](https://pandas.pydata.org) 
  - [R-tidyverse](https://www.tidyverse.org) (mostly [dplyr](https://dplyr.tidyverse.org))

- The WL generated code uses functions from the [Wolfram Function Repository](https://resources.wolframcloud.com/FunctionRepository/).   
  (See the references section "Wolfram Function Repository functions".)
 
- The tutorials sequence has an "inverted" structure: the most conceptually rich and technical sessions are presented first. 

## Detailed tutorial plan

### Introduction through questions and answers

- What are the simplifying assumptions for the family of workflows considered in this tutorial?
  - We do not consider hard to generalize- or too specialized transformations.
  - For example, we do not consider:
    - Data gathering/harvesting 
    - Data ingestion by parsing of, say, XML structures
    - Date-time specific transformations
    - Natural text specific transformations
    - Etc. 
  
- What are the simplifying assumptions about the targeted data and transformations? 
  - Tabular data and collections of tabular data. (E.g. lists of datasets.)
  - Transformation workflows that can be expressed with a certain "standard" or "well-known" subset of SQL.
  - The flow chart given below illustrates well the targeted DT.
 
- Do these workflows apply to other programming languages and/or data systems?
  - Yes, with the presented DT know-how we target multiple "data science" programming languages.
  
- Are additional packages needed to run the codes?
  - Yes and no: depends on the target data transformation system.
  - Sometimes the WL code uses Wolfram Function Repository functions. 

- Are there similar tutorials dedicated to other programming languages or packages?
  - Yes, many. Both for WL and the rest (Julia/Python/R.)
  - That said, in this tutorial we use a certain simplified and streamlined data-and-transformations model 
    that allows the development of cross-system, transferable know-how and workflows. 
  
- What are the most important concepts for a newcomer to data wrangling?
  1. Cross tabulation (or contingency matrices)
  2. (Inner) joins 
  3. The so called Split-apply-combine pattern
  4. Long form and wide form (or data pivoting)

- How do the considered DT workflows relate to well known Machine Learning (ML) workflows? 
  - Generally speaking, data has to be transformed into formats convenient for the application of ML algorithms.
    How much transformation is needed depends a lot on the host system or targeted ML package(s). 
  - For example, WL has extensive ML data on-boarding functions. 
    ("Encoders" and "decoders" that make the use of Neural Networks more streamlined.) 
    Hence, for using ML in WL less DT is needed.  
  
- How much is WL used?
  - Approximately 80% we use WL; for illustration purposes we show some of the workflows in other languages. 
    (Run within the same Mathematica presentation notebooks.)
  
- Mental model (of the considered DT queries) 

  - Simplifying assumptions -- targeting:
    - Tabular data
    - Collections of tabular data
  - Workflows considered:
    - (Generalizing) flow chart
    - The Split-transform-combine DT pattern, \[HW1\]
    - Reshaping

### Reshaping of data -- detailed examples

- Long form (aka "narrow format"):
  - Using long form vs not using long form
  - Programmatic use
  - Relation to sparse matrices 
   
- Wide form (aka "wide format")
  - As an inversion of long form
  - Typical usage
  
- Cross tabulation
  - Relation to wide form
  - The different missions and mind-share of cross tabulation and wide form

### Basic operations and joins

- Basic operations
    - Data load
    - Column selection
    - Row filtering
    - Summarization
        - Ways to summarize data
        - "Global" summary
        - Summarization per group and per column
        - Summarization vs Cross tabulation

- Joins 
    - Types of joins
    - Inner joins
    - Left joins
    - Semi-joins

### Additional topics

- Example combinations with ML workflows
    - Making a recommender system
    - Making a classifier

## Visual aids

Here is a flow chart that encompasses a large fraction of typical tabular data transformation workflows:

![TabularDataTransformationWorkflow](https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/raw/master/Part-2-Monadic-Workflows/Diagrams/Tabular-data-transformation-workflows/Tabular-data-transformation-workflows.jpg) 

---
 
This call of 
[`ToDataQueryWorkflow`](https://github.com/antononcube/Raku-DSL-English-DataQueryWorkflows)
through
[`ExternalParsersHookUp`](https://github.com/antononcube/ConversationalAgents/blob/master/Packages/WL/ExternalParsersHookup.m), \[AAp2\],
over a sequence of natural commands:

```mathematica
ToDataQueryWorkflowCode["use dfTitanic; 
      filter with passengerSurvival is 'survived';
      rename passengerClass, passengerSex as class and sex;
      cross tabulate class and sex", "Execute" -> False]
```
generates this WL code:

```mathematica
Hold[obj = dfTitanic; 
 obj = Select[obj, #1["passengerSurvival"] == "survived" &]; 
 obj = (Join[KeyDrop[#1, {"passengerClass", "passengerSex"}], Association["class" -> #1["passengerClass"], "sex" -> #1["passengerSex"]]] &) /@ obj; 
 obj = ResourceFunction["CrossTabulate"][({#1["class"], #1["sex"]} &) /@ obj]]
```
which when executed gives the dataset:

```mathematica
Dataset[<|
"1st" -> <|"female" -> 139, "male" -> 61|>, 
"2nd" -> <|"female" -> 94, "male" -> 25|>, 
"3rd" -> <|"female" -> 106, "male" -> 75|>|>, 
 TypeSystem`Assoc[TypeSystem`Atom[String], TypeSystem`Struct[{"female", "male"}, {TypeSystem`Atom[Integer], TypeSystem`Atom[Integer]}], 3], 
 <|"ID" -> 177940708079520|>]
```

## References

### Articles

\[HW1\] Hadley Wickham, 
["The Split-Apply-Combine Strategy for Data Analysis"](https://www.jstatsoft.org/article/view/v040i01),
(2011),
Journal of Statistical Software.

\[AA1\] Anton Antonov,
["Contingency tables creation examples"](https://mathematicaforprediction.wordpress.com/2016/10/04/contingency-tables-creation-examples/),
(2016),
[MathematicaForPrediction at WordPress](https://mathematicaforprediction.wordpress.com).

\[AA2\] Anton Antonov,
["Pareto principle adherence examples"](https://mathematicaforprediction.wordpress.com/2016/11/17/pareto-principle-adherence-examples/),
(2016),
[MathematicaForPrediction at WordPress](https://mathematicaforprediction.wordpress.com).

 
### Packages

\[AAp1\] Anton Antonov, 
[DSL::English::DataQueryWorkflows Raku package](https://github.com/antononcube/Raku-DSL-English-DataQueryWorkflows), 
(2020), 
[GitHub/antononcube](https://github.com/antononcube).

\[AAp2\] Anton Antonov, 
[External Parsers Hookup Mathematica package](https://github.com/antononcube/ConversationalAgents/blob/master/Packages/WL/ExternalParsersHookup.m), 
(2020), 
[ConversationalAgents at GitHub](https://github.com/antononcube/ConversationalAgents).

\[AAp3\] Anton Antonov,
[Cross tabulation implementation in Mathematica](https://github.com/antononcube/MathematicaForPrediction/blob/master/CrossTabulate.m), 
(2017),
[MathematicaForPrediction at GitHub](https://github.com/antononcube/MathematicaForPrediction).

\[AAp4\] Anton Antonov,
[Data reshaping Mathematica package](https://github.com/antononcube/MathematicaForPrediction/blob/master/DataReshape.m), 
(2018),
[MathematicaForPrediction at GitHub](https://github.com/antononcube/MathematicaForPrediction).

### Wolfram Function Repository functions

Anton Antonov, [`CrossTabulate`](https://resources.wolframcloud.com/FunctionRepository/resources/CrossTabulate).

Anton Antonov, [`ExampleDataset`](https://www.wolframcloud.com/obj/antononcube/DeployedResources/Function/ExampleDataset). 
*(Submitted)*

Anton Antonov, [`ParetoPrinciplePlot`](https://resources.wolframcloud.com/FunctionRepository/resources/ParetoPrinciplePlot).

Anton Antonov, [`RecordsSummary`](https://resources.wolframcloud.com/FunctionRepository/resources/RecordsSummary).

Anton Antonov, [`ToLongForm`](https://www.wolframcloud.com/obj/antononcube/DeployedResources/Function/ToLongForm). 
*(Submitted)*

Anton Antonov, [`ToWideForm`](https://www.wolframcloud.com/obj/antononcube/DeployedResources/Function/ToWideForm). 
*(Submitted)*

Seth Chandler, [`ResetDataset`](https://resources.wolframcloud.com/FunctionRepository/resources/ResetDataset).
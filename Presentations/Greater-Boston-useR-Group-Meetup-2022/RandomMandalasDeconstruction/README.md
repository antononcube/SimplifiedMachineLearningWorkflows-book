# Random mandalas deconstruction with R, Python, and Mathematica

***Presented by Anton Antonov***   
***[Boston useR Meetup](https://www.meetup.com/Boston-useR/events/284045968/)***   
***2022-02-28***   

**Abstract:** In this presentation we discuss the application of different dimension reduction algorithms over collections of random mandalas. 
We discuss and compare the derived image bases and show how those bases explain the underlying collection structure. 
The presented techniques and insights (1) are applicable to any collection of images, and (2) can be included in larger, 
more complicated machine learning workflows. The former is demonstrated with a handwritten digits recognition application; 
the latter with the generation of random Bethlehem stars. The (parallel) walk-through of the core demonstration is in 
all three programming languages: Mathematica, Python, and R.

**Speaker Bio:** Anton is an applied mathematician (Ph.D.) with 30+ years of experience in algorithm development, 
scientific computing, mathematical modeling, natural language processing, combinatorial optimization, research and development programming, 
machine learning, and data mining. In the last ten years, he focused on developing machine learning algorithms and workflows for 
different industries (music, movies, recruiting, healthcare.)

------

## Random mandalas generation

Here is a link that generates collages of random mandalas via Wolfram Cloud:

```
https://www.wolframcloud.com/obj/8691f810-4c70-484e-a325-eda565ce0185?n=12&colorFunction=GrayTones&edgeOpacity=0.4
```

![*Random mandalas collage via WolframCloud*](https://www.wolframcloud.com/obj/8691f810-4c70-484e-a325-eda565ce0185?n=12&colorFunction=GrayTones&edgeOpacity=0.4)

------

## References

### Articles

[AA1] Anton Antonov, 
["Comparison of dimension reduction algorithms over mandala images generation"](https://mathematicaforprediction.wordpress.com/2017/02/10/comparison-of-dimension-reduction-algorithms-over-mandala-images-generation/), 
(2017),
[MathematicaForPrediction at WordPress](https://mathematicaforprediction.wordpress.com).

[AA2] Anton Antonov,
["Handwritten digits recognition by matrix factorization"](https://mathematicaforprediction.wordpress.com/2016/11/12/handwritten-digits-recognition-by-matrix-factorization/),
(2016),
[MathematicaForPrediction at WordPress](https://mathematicaforprediction.wordpress.com).


### Mathematica packages and repository functions

[AAp1] Anton Antonov, 
[Monadic Latent Semantic Analysis Mathematica package](https://github.com/antononcube/MathematicaForPrediction/blob/master/MonadicProgramming/MonadicLatentSemanticAnalysis.m), 
(2017), 
[MathematicaForPrediction at GitHub/antononcube](https://github.com/antononcube/MathematicaForPrediction).

[AAf1] Anton Antonov,
[NonNegativeMatrixFactorization](https://resources.wolframcloud.com/FunctionRepository/resources/NonNegativeMatrixFactorization),
(2019),
[Wolfram Function Repository](https://resources.wolframcloud.com).

[AAf2] Anton Antonov,
[IndependentComponentAnalysis](https://resources.wolframcloud.com/FunctionRepository/resources/IndependentComponentAnalysis),
(2019),
[Wolfram Function Repository](https://resources.wolframcloud.com).

[AAf3] Anton Antonov,
[RandomMandala](https://resources.wolframcloud.com/FunctionRepository/resources/RandomMandala),
(2019),
[Wolfram Function Repository](https://resources.wolframcloud.com).


### Python packages 

[AAp2] Anton Antonov,
[LatentSemanticAnalyzer Python package](https://pypi.org/project/LatentSemanticAnalyzer)
(2021),
[PyPI.org](https://pypi.org/).

[AAp3] Anton Antonov,
[Random Mandala Python package](https://pypi.org/project/RandomMandala),
(2021),
[PyPI.org](https://pypi.org/).


### R packages

[AAp4] Anton Antonov,
[Latent Semantic Analysis Monad R package](https://github.com/antononcube/R-packages/tree/master/LSAMon-R),
(2019),
[R-packages at GitHub/antononcube](https://github.com/antononcube/R-packages).



<style type="text/css">
.main-container {
  max-width: 1800px;
  margin-left: auto;
  margin-right: auto;
}
</style>

# Data

In this directory is placed most of the data used in this book.

## Reading the chapters of "The Idiot"

### R

```r
library(jsonlite)
temp <- tempfile()
download.file("https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/raw/master/Data/Dostoyevsky-The-Idiot-Russian-chapters.json.zip",temp)
jsonRes <- jsonlite::fromJSON(unz(temp, "Dostoyevsky-The-Idiot-Russian-chapters.json"))
length(jsonRes)
# [1] 50
```


### WL

Here is WL code to read the chapters of the Dostoevsky's novel "The Idiot" (in Russian):

```mathematica
url = "https://github.com/antononcube/SimplifiedMachineLearningWorkflows-book/raw/master/Data/Dostoyevsky-The-Idiot-Russian-chapters.json.zip";
str = Import[url, "String"];
filename = First@Import[StringToStream[str], "ZIP"];

aURLIdiotRussianChapters = Association[Import[StringToStream[str], {"ZIP", filename, "JSON"}]];
Length[aURLIdiotRussianChapters]
(* 50 *)
```

## rstudio::conf 2019 abstracts

The 
[rstudio::conf](https://rstudio.com/conference/) 
2019 abstracts were taken from the Markdown file
[sessions.md](https://github.com/rstudio/rstudio-conf/blob/master/2019/sessions.md)
from the GitHub repository 
[rstudio-conf](https://github.com/rstudio/rstudio-conf).

That Markdown files was parsed in order to produce 
[the corresponding JSON records](./RStudio-conf-2019-abstracts.json) and
[the corresponding CSV file](./RStudio-conf-2019-abstracts.csv).

 
## Wolfram Technology Conference (WTC) abstracts

The abstracts of 
[WTC-2019](https://www.wolfram.com/events/technology-conference/2019)
were taken from 
https://wtc19.pathable.com/meetings.html 
and parsed in order to produce
[the corresponding JSON records](./Wolfram-Technology-Conference-2019-abstracts.json).

Using additional WTC presentation notebooks from past years a 
[CSV file](./Wolfram-Technology-Conference-2016-to-2019-abstracts.csv) 
was produced with WTC abstracts for the years 2016 to 2019.  


## Data in other, related repositories

### [MathematicaVsR at GitHub](https://github.com/antononcube/MathematicaVsR)

See [MathematicaVsR's data folder](https://github.com/antononcube/MathematicaVsR/tree/master/Data).

- [Shakespeare's play "Hamlet" (1604)](https://github.com/antononcube/MathematicaVsR/blob/master/Data/MathematicaVsR-Data-Hamlet.csv).

- [USA presidential speeches](https://github.com/antononcube/MathematicaVsR/blob/master/Data/MathematicaVsR-Data-StateOfUnionSpeeches.JSON.zip).
  
- [Mushroom dataset](https://github.com/antononcube/MathematicaVsR/blob/master/Data/MathematicaVsR-Data-Mushroom.csv).

- [Titanic dataset](https://github.com/antononcube/MathematicaVsR/blob/master/Data/MathematicaVsR-Data-Titanic.csv).

- [Wine quality data](https://github.com/antononcube/MathematicaVsR/blob/master/Data/MathematicaVsR-Data-WineQuality.csv). 


## R data packages

Here is related R data package: [MathematicaVsRData](https://github.com/antononcube/R-packages/tree/master/MathematicaVsRData).  
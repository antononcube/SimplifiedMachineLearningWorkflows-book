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
Length[aULRIdiotRussianChapters]
(* 50 *)
```

## rstudio::conf 2019 abstracts

The rstudio::conf 2019 abstracts were taken from the Markdown file
[sessions.md](https://github.com/rstudio/rstudio-conf/blob/master/2019/sessions.md)
from the GitHub repository 
[rstudio-conf](https://github.com/rstudio/rstudio-conf).

That Markdown files was parsed in order to produce 
[the corresponding JSON records](./RStudio-conf-2019-abstracts.json).  
 
## Wolfram Technology Conference 2019 abstracts

The abstracts were taken from 
https://wtc19.pathable.com/meetings.html 
and parsed in order to produce
[the corresponding JSON records](./Wolfram-Technology-Conference-2019-abstracts.json).  
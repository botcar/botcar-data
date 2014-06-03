# Optimizing

## Tree (top down approach)

![datasetRework](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Document%20Revisions%20-%20draft%201.png)

When first dealing with the botcar datasets, I was trying to normalize the collections and indicies. This required restructuring the datasets to avoid redundancy and  We had several groups of files containing our data:

1. [Images](https://github.com/botcar/botcar-data/tree/master/images): [image data](https://github.com/botcar/botcar-data/tree/master/images/imagedata) was stored in a folder with .csv's for each manuscript in the form: image urn, label, liscence. A [collection folder](https://github.com/botcar/botcar-data/tree/master/images/collections) housed a .csv file that had general image urn for a given collection, a description of said collection, and its path.
2. [Collections](https://github.com/botcar/botcar-data/tree/master/collections): information about the formation of each manuscript was stored in one of the Catesby**#.csv files, information about labels was in botcarLabels.csv, information about specimens was is catesbySpecimen.csv, and information about each taxonomic level was in its respective .csv.
3. [Indicies](https://github.com/botcar/botcar-data/tree/master/indices): some .tsv files with relationships between entities such as image-folio, specimen-label, and species-genus.

This set up promted me to attempt to refine a few aspects by relating information based on some 'hierarchical organization'. The result was the green set of files in the image above and the tree below:

![outline1](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Data%20Outline%20-%20draft%201.png)

# Optimizing

## Tree

When first dealing with the botcar datasets, I was trying to normalize the collections and indicies. Normalization requires restructuring the datasets to avoid redundancy and ensure that the relations among entities are logical.

![datasetRework](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Document%20Revisions%20-%20draft%201.png)

These files came from a few groups of files containing all of our data:

1. [Images](https://github.com/botcar/botcar-data/tree/master/images): [image data](https://github.com/botcar/botcar-data/tree/master/images/imagedata) was stored in a folder with .csv's for each manuscript in the form: image urn, label, liscence. A [collection folder](https://github.com/botcar/botcar-data/tree/master/images/collections) housed a .csv file that had general image urn for a given collection, a description of said collection, and its path.
2. [Collections](https://github.com/botcar/botcar-data/tree/master/collections): information about the formation of each manuscript was stored in one of the Catesby**#.csv files, information about labels was in botcarLabels.csv, information about specimens was is catesbySpecimen.csv, and information about each taxonomic level was in its respective .csv.
3. [Indicies](https://github.com/botcar/botcar-data/tree/master/indices): some .tsv files with relationships between entities such as image-folio, specimen-label, and species-genus.

First I attempted to refine a few datasets by relating information based on some general 'hierarchical organization'. The result is the green set of files in the image above and the tree below:

![outline1](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Data%20Outline%20-%20draft%201.png)

This new structure had many benefits over the old:

- No more redundant data between differing 'hierarchical levels', such as with manuscripts and folios. Instead of having information about a manuscript copied with each folio, the two distinct ideas are divided with a symbolic link of sorts between the manuscript and its group of folios.
- General formating of datasets so that each file can hold all information about a urn, AKA no long divided by manuscripts.
- Semantic and logical ideas are still represented in collections, i.e. each data set still makes sense.

However, there are still some issues with this design:

- What is an index/how do we distinguish indicies and collections?
- What is the order of idicies? (do we link everything to everything or are we specific: image-folio, folio-label || folio-image, image-label)
- How do we deal with complex junctures?



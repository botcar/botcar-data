# Datasets

When first dealing with the botcar datasets I was trying to normalize the collections and indicies. Normalization requires restructuring the datasets to avoid redundancy and ensure that the relations among entities are logical.

## Tree

I began with trying to restructure the data by taking our current files and refining a few datasets by relating information based on some general 'hierarchical organization'. This is a top down approach to the dealing with the data and in effect creates a tree for our relations.

![datasetRework](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Document%20Revisions%20-%20draft%201.png)

Those files above in blue came from a few groups of files containing all of our data:

1. [Images](https://github.com/botcar/botcar-data/tree/master/images): [image data](https://github.com/botcar/botcar-data/tree/master/images/imagedata) was stored in a folder with .csv's for each manuscript in the form: image urn, label, liscence. A [collection folder](https://github.com/botcar/botcar-data/tree/master/images/collections) housed a .csv file that had each general image urn for a given collection, a description of said collection, and its path.
2. [Collections](https://github.com/botcar/botcar-data/tree/master/collections): information about the formation of each manuscript was stored in one of the Catesby**#.csv files, information about labels was in botcarLabels.csv, information about specimens was is catesbySpecimen.csv, and information about each taxonomic level was in its respective .csv.
3. [Indicies](https://github.com/botcar/botcar-data/tree/master/indices): some .tsv files with relationships between entities such as image-folio, specimen-label, and species-genus.

The result of my hierachichal organization is the green set of files in the image above and the relationships are represented in the tree below:

![outline1](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Data%20Outline%20-%20draft%201.png)

This new structure had many benefits over the old:

- No more redundant data between differing 'hierarchical levels', such as with manuscripts and folios. Instead of having information about a manuscript copied with each folio, the two distinct ideas are divided with a symbolic link of sorts between the manuscript and its group of folios.
- General formating of datasets so that each file can hold all information about a urn, AKA no long divided by manuscripts.
- Semantic and logical ideas are still represented in collections, i.e. each data set still makes sense.

However, there are still some issues with this design:

- What is an index/how do we distinguish indicies and collections?
- What is the order of idicies? (do we link everything to everything or are we specific: image-folio, folio-label || folio-image, image-label)
- How do we deal with complex junctures?

## Web

To solve these problems, and to make dataset formation general and extensible, I stopped looking at our data as a tree and began to look at it as a web. In a tree each node or bit of information has nodes it is related to above it (parents), and nodes that are related to it below (children). In a web you also have nodes and vertices, but they can be linked however you please. The result is this:

![outline3](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/BotCar%20Data%20Outline%20-%20draft%203.png)

### Normal Forms

To deal with the first two issues I tried to get our data set into third normal form (3NF). Before we get into that, lets look at each normal form:

###### First Normal Form (1NF)

To accomplish this level a dataset must not have duplicative columns from the same table, there must be separate tables for each group of related data in which each row is identifiable with a unique column (the primary key). This is exptremely basic and both of these requirements were met with our original dataset setup.

###### Second Normal Form (2NF)

To get to this level a dataset must meet all the requirements of the first normal form, remove all subsets of data that apply to multiple rows of a table and place them in separate tables, and must create relationships between these new tables and their predecessors through the use of foreign keys. This was accomplished with my first revisions when creating a tree, the manuscripts redundant data in folios was abstracted away yet still related through a urn.

###### Third Normal Form (3NF)

3NF goes one step further by meeting all the requirements of the second normal form as well as removing columns that are not dependent upon the primary key. To get here I set up some simple guidelines for how datasets should be formed:

- Indicies are only to be used to define the relationships between urns (1-1)
- Collections do not contain a urn other than the primary

This effectively strips the datasets to only have information that is dependent on eachother.

### Triple-of-Triples

A so-called 'triple-of-triples' solves our final problem of grouping complex relationships. For botcar, we created an AoIDurn (Act of Identification) which links any of the forms of IDing a specimen (label, taxonomy, possibly later ROI) to the specimenurn without cluttering a collection and breaking my 2nd rule from above, and without creating to many index files.

## Summary

These datasets are used to hold information in a way that the computer and ourselves can read. If in the future we create our datasets with these guidelines and ideas in mind and with an eye towards the core ideas of normalization, our data could be faster to act on, more logically setup, and more easily extensible.

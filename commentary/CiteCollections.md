# Cite Collections

![Cite .rng schema diagram](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Optimizing%20Images/Cite%20Collection%20Schema.png)

The cite structure revolves around the idea that the world is divided into two things, text and objects. It is used to express the latter, while cts is used with texts. The 5 .rng schema files that define cite collections allow us to group cite objects together based on similar properties.

1. CiteObject: The lowest level in the collection hierarchy - a citeurn and a list of properties.
2. CiteCollection: A collection is an ordered or unordered list of related CiteObjects.
3. CiteCollectionInventory (collectionService): A group of collections.
4. CiteIndexInventory (indexInventory): A group of indicies.
   - Indicies are one to one relations.
5. src: The source file of a collection or index.

# Cite Collections

![Cite .rng schema diagram](https://raw.githubusercontent.com/botcar/botcar-data/master/commentary/Images/Cite%20Collection%20Schema.png)

The cite structure revolves around the idea that the world is divided into two things, text and objects, and it is used to represent the latter. The 3 .rng schema files that define cite collections allow us to group cite objects together based on similar properties.

1. [CiteObject](https://github.com/botcar/botcar-data/blob/master/collections/CiteObject.rng): The lowest level in the collection hierarchy - a citeurn and a list of properties.
2. [CiteCollection](https://github.com/botcar/botcar-data/blob/master/collections/CiteCollection.rng): A collection is an ordered or unordered list of related CiteObjects.
3. [CiteCollectionInventory](https://github.com/botcar/botcar-data/blob/master/collections/CiteCollectionInventory.rng) (collectionService): A group of collections.

The last two schema files define indicies (rather, an inventory of indicies but the indicies are implied) and source files.

- [CiteIndexInventory](https://github.com/botcar/botcar-data/blob/master/indices/CiteIndexInventory.rng) (indexInventory): A group of indicies.
   - Indicies are one to one relations.
- [src](https://github.com/botcar/botcar-data/blob/master/collections/src.rng): The source file of a collection or index.

We use these definitions to define a format for our datasets ([inventory.xml](https://github.com/botcar/botcar-data/blob/master/collections/inventory.xml) or [indicies.xml](https://github.com/botcar/botcar-data/blob/master/indices/indices.xml)).
These plus ctsurns and the cts structure allows us to talk about definite objects (cite), abstract representations of knowledge (cts), as well as any possible relations between them (indicies).

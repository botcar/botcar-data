
package edu.furman.folio.botcardata

import edu.harvard.chs.cite.CiteUrn
import edu.harvard.chs.cite.CtsUrn

/**  A class for working with data instantiating the basic
* HMT project data model in archival storage formats.
*/
class Testudinate {
    def tei = new groovy.xml.Namespace("http://www.tei-c.org/ns/1.0")

/*
    def indexStructs = [
        "textUrnToFolio": ["cts", "appearsOn", "cite"] ,
        "folioToOverviewImage" : ["cite","hasDefaultImage","cite"],
        "folioToImage": ["cite", "illustratedBy", "cite"],
        "criticalsignToText": ["cite", "annotates", "cts"],
        "criticalsignToFolio": ["cite", "appearsOn", "cite"],
        "scholiaToIliad": ["cts","commentsOn","cts"]
    ]
*/

    /** Directory with index files. Any files .txt files in
    * this directory should also appear as keys in the indexVerbs
    * map, above.
    */
    File indexList = new File("IndexStructures.txt")
    File indexDirectory = new File("Indices")
    File taxonomyList = new File("TaxonomyIndices.txt")
    def exemplarIndex = "specimen-species"

    /** List of directories with scholia inventories */
    // def scholinvDirectories = ['textinventories/VenetusA', 'textinventories/Escorial-Upsilon-1-1']

    /** Single directory with one or more .txt files listing 
    * navigation sequences.
    * (Verb is always 'next' for navigation relations)
    */
    File navigationDirectory

    /** Writable file for resulting turtle-formatted triplets. */
    File turtleOutput

    Testudinate(File turtle) {
        this.turtleOutput =  turtle
    }


    /** 
    * main() method expects two arguments: a writable output file name,
    * and a directory where files with navigation data can be found.
    */
    public static void main(String[] args) 
    throws Exception {

        switch (args.size()) {
            case 0:
                throw new Exception("main method requires name of output file.")
            System.exit(-1)
            break
            case 1:
                try {
                File outFile = new File(args[0])
                Testudinate ttl = new Testudinate(outFile)
                ttl.generateTurtle()
            } catch (Exception e) {
                throw e
            }
            break
            // extraneous args ignored:
            default:
                try {
                File outFile = new File(args[0])
                Testudinate ttl = new Testudinate(outFile)
                ttl.navigationDirectory = new File(args[1])
                ttl.generateTurtle()
            } catch (Exception e) {
                throw e
            }
            break
        }
    }


    void generateTurtle() {
        def prefixes = "@prefix botcar: <http://folio.furman.edu/botcar/rdfverbs/> . \n@prefix hmt: <http://chs.harvard.edu/ctsns/rdfverbs> . \n\n"
	this.turtleOutput.write("")
        this.turtleOutput.append(prefixes)

		def nsTriples = '<http://chs.harvard.edu/ctsns/greekLit> hmt:abbreviatedBy "greekLit" . \n<http://www.homermultitext.org/datans/> hmt:abbreviatedBy "hmt" . \n<http://folio.furman.edu/botcar/rdfverbs> hmt:abbreviatedBy "botcar" . \n\n'

		this.turtleOutput.append(nsTriples)

		// Generate relations from nav files:
		tabulateFolioNavigation()
		tabulateIndices()
		tabulateTaxonomy()
	    }


		void tabulateFolioNavigation() {
			this.navigationDirectory.eachFileMatch (~/^.*txt$/) { f ->
				String prevUrn = null
				f.eachLine {
					def cols = it.split(/\t/)
					if (cols.length == 2){
						this.turtleOutput.append("<${cols[0]}>\thmt:seq\t<${cols[1]}> . \n")
						if (prevUrn != null){
							this.turtleOutput.append("<${cols[0]}>\thmt:prev\t<${prevUrn}> . \n")
							this.turtleOutput.append("<${prevUrn}>\thmt:next\t<${cols[0]}> . \n")
						}
					}
					prevUrn = cols[0]
				}		
			}
		}
		
		void tabulateIndices() {
			this.indexList.eachLine { f ->
				def commentPattern = ~/^#.+$/
				if (!(commentPattern.matcher( f ).matches())){
					def cols = f.split(/\t/)
					if (cols.length == 3){
						def indexName = cols[0]
						def thisVerb = cols[1]
						def thisInverseVerb = cols[2]
						def thisIndexFile = new File("${indexDirectory}/${indexName}.txt")
						println "${indexName}"
						thisIndexFile.eachLine { ln ->
							def indexItems = ln.split(/\t/)
							if (indexItems.length == 2){
								def subURN = indexItems[0]
								def objURN = indexItems[1]
								this.turtleOutput.append("<${subURN}>\t${thisVerb}\t<${objURN}> .\n")
								this.turtleOutput.append("<${objURN}>\t${thisInverseVerb}\t<${subURN}> .\n")
							}
						}
					}
				}
			}
		}

		void tabulateTaxonomy(){
			println "taxonomy goes here."
			File gf = new File("Indices/tax-genus-family.txt")
			File sg = new File("Indices/tax-species-genus.txt")
			File ss = new File("Indices/tax-specimen-species.txt")
			List familyGenus = []
			List genusSpecies = []
			List speciesSpecimen = []
			println "Assembling familyGenus"
			gf.eachLine { ll ->
				def cols  = ll.split("\t")
				familyGenus.push("${cols[1]}\t${cols[0]}")
			}
			println "Assembling genusSpecies"
			sg.eachLine { ll ->
				def cols = ll.split("\t")
				genusSpecies.push("${cols[1]}\t${cols[0]}")
			}
			println "Assembling speciesSpecimen"
			ss.eachLine { ll ->
				def cols = ll.split("\t")
				speciesSpecimen.push("${cols[1]}\t${cols[0]}")
			}
			// each Family, get each Genus, get each Species, get each Specimen
			familyGenus.each {
				def cols = it.split("\t")
				def thisFamily = cols[0]
				def thisGenus = cols[1]
				def allSpecies = genusSpecies.findAll {
					def pattern = ~"^${thisGenus}.+\$"
					it =~ pattern
				}
				allSpecies.each {
					cols = it.split("\t")
					def thisSpecies = cols[1]
				    def allSpecimens = speciesSpecimen.findAll {
							def pattern = ~"^${thisSpecies}.+\$"
							it =~ pattern
					}
					allSpecimens.each { 
						def thisSpecimen = it.split("\t")[1]	
					    this.turtleOutput.append("<${thisFamily}>\tbotcar:hasMember\t<${thisGenus}> . \n")
					    this.turtleOutput.append("<${thisFamily}>\tbotcar:hasMember\t<${thisSpecies}> . \n")
					    this.turtleOutput.append("<${thisFamily}>\tbotcar:hasExemplar\t<${thisSpecimen}> . \n")
					    this.turtleOutput.append("<${thisGenus}>\tbotcar:hasMember\t<${thisSpecies}> . \n")
					    this.turtleOutput.append("<${thisGenus}>\tbotcar:hasExemplar\t<${thisSpecimen}> . \n")
					    this.turtleOutput.append("<${thisSpecies}>\tbotcar:hasExemplar\t<${thisSpecimen}> . \n")
					    this.turtleOutput.append("<${thisGenus}>\tbotcar:isMemberOf\t<${thisFamily}> . \n")
					    this.turtleOutput.append("<${thisSpecies}>\tbotcar:isMemberOf\t<${thisFamily}> . \n")
					    this.turtleOutput.append("<${thisSpecimen}>\tbotcar:isExemplarOf\t<${thisFamily}> . \n")
					    this.turtleOutput.append("<${thisSpecies}>\tbotcar:isMemberOf\t<${thisGenus}> . \n")
					    this.turtleOutput.append("<${thisSpecimen}>\tbotcar:isExemplarOf\t<${thisGenus}> . \n")
					    this.turtleOutput.append("<${thisSpecimen}>\tbotcar:isExemplarOf\t<${thisSpecies}> . \n")
				      }
				}
		    }
			//make family-genus, genus-species, species-specimen Lists
			//each line of family-genus
				//grab family
					//grab genus
						//go ahead and make family-hasMember-genus and inverse
						//in genus-species list, findAll genus
							//for each found-genus, get species
									//for each species...
											//make genus-hasMember-species, family-hasMember-genus, family-hasMember-species (and inverse)
											//in species-specimen, findAll species
												//make family, genus, species hasExemplar->specimen (and inverse)
		}
}

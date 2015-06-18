
//println "Integrating…"

/*
	Get Test Data
*/

def testFileName = "/cite/proj/bc-data/prod/collections/Specimens-Lord.tsv"
File testFile = new File(testFileName)

testData = []
testProps = []

testFile.eachWithIndex{ l, i ->
	if( i == 0){
	   testProps = l.tokenize('\t')
	} else {
		def newData = new Expando()
		def tl = l.tokenize('\t')
		testProps.eachWithIndex{ p, j ->
			//println "${p}, ${j}"
			newData.setProperty(p,tl[j])
		}
		testData[i-1] = newData
		//println testData[i-1]
	}
}

// At this point, testData contains an array of our tsv data

/* 
	Get Spcies Data:
*/

def speciesFileName = "/cite/proj/bc-data/prod/collections/species.tsv"
File speciesFile = new File(speciesFileName)

speciesData = []
speciesProps = []

speciesFile.eachWithIndex{ l, i ->
	if( i == 0){
	   speciesProps = l.tokenize('\t')
	} else {
		def newData = new Expando()
		def tl = l.tokenize('\t')
		speciesProps.eachWithIndex{ p, j ->
			//println "${p}, ${j}"
			newData.setProperty(p,tl[j])
		}
		speciesData[i-1] = newData
		//println speciesData[i-1]
	}
}

// At this point, speciesData contains an array of our tsv Spcecies data

/* Assing tsnIDs for specimens */

def ts = "urn:cite:botcar:species.Lycopodiellaappressa"

def foundThing = speciesData.find{ it."speciesURN" == ts}

testData.each{ l ->
	def ws = l["speciesURN"]
	def foundTSN = speciesData.find{ it."speciesURN" == ws }
	if (foundTSN){
	l["tsnID"] = foundTSN["tsn"]
	} else {
	l["tsnID"] = "indet."
	}
//	println l["tsnID"]
}

/* write out new specimen file */

testData[0].properties.each{ p, v ->
	print "${p}\t"
}
print "\n"

testData.each{ l ->
	l.properties.each{ p, v ->
		print "${v}\t"
	}
	print "\n"
}


//println foundThing["tsn"]

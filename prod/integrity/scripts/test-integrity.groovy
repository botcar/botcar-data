def citedUrnsFile = new File('../test-data/urns-cited.txt')
def ctsUrnsFile = new File('../test-data/cts-urns.txt')
def citeUrnsFile = new File('../test-data/cite-urns.txt')

//Make a list of all valid cts-urns
def ctsUrns = ctsUrnsFile.collect {it}
//Make a list of all valid cite-urns
def citeUrns = citeUrnsFile.collect {it}

println(citeUrns.getClass())

def checkUrn = ""
def tempLine = ""
citedUrnsFile.eachLine { l ->
	//First let's remove any sub-refs from URNs
	if ( l.indexOf("@") > 0){
		tempLine = l.split("@")[0] + ">"	
	} else {
		tempLine = l
	}
	checkUrn = l
    if ( citeUrns.indexOf(tempLine) < 0 ){
		if (ctsUrns.indexOf(tempLine) < 0 ){
			println(l)	
		}
	}
}


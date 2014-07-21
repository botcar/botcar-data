import csv
import re

CatesbyHS212 = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/CatesbyHS212.csv'
CatesbyHS232 = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/CatesbyHS232.csv'
CatesbyNH1 = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/CatesbyNH1.csv'
CatesbyNH2 = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/CatesbyNH2.csv'
catesbySpecimens = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/catesbySpecimens.csv'
botcarLabels = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/botcarLabels.csv'
imgcollections = '/Users/Sam Hill/Documents/botcar/botcar-data/images/collections/imgcollections.csv'
CatesbyHSimg = '/Users/Sam Hill/Documents/botcar/botcar-data/images/imagedata/CatesbyHSimg.csv'
CatesbyNHimg = '/Users/Sam Hill/Documents/botcar/botcar-data/images/imagedata/CatesbyNHimg.csv'
families = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/families.csv'
genera = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/genera.csv'
species = '/Users/Sam Hill/Documents/botcar/botcar-data/collections/species.csv'

Specimens = '/Users/Sam Hill/Desktop/BotCar/Specimens.csv'
Labels = '/Users/Sam Hill/Desktop/BotCar/Labels.csv'
Folios = '/Users/Sam Hill/Desktop/BotCar/Folios.csv'

# Folios.csv line 245 is the last line of HS

imageDict = []

file = open(CatesbyNHimg, "rU")
reader = csv.reader(file)
for row in reader:
	ImageURN = row[0]
	imageDict.append(ImageURN)
file.close()

file = open(Folios, "rU")
reader = csv.reader(file)
rownum = 0
for row in reader:
	if rownum > 246:
		FolioURN = row[0]
		Sequence = row[1]
		RectoVerso = row[2]
		breakdown = FolioURN.split(':')[3].split('.')
		HSnum1 = breakdown[0][9:]
		folio1 = breakdown[1]
		ImageURNList = []
		for ImageURN in imageDict:
			stuff = ImageURN.split('_')
			HSnum2 = stuff[0][45:]
			folio2 = stuff[2]
			if folio1 == folio2 and HSnum1 == HSnum2:
				ImageURNList.append(ImageURN)
			ImageURNListString = ",".join(ImageURNList)
		print '%s,%s,%s,"%s"' % (FolioURN, Sequence, RectoVerso, ImageURNListString)
	rownum += 1
import csv
import re

#OLD
#CatesbyHS212 = '/Users/SamHill/Documents/botcar/botcar-data/collections/CatesbyHS212.csv'
#CatesbyHS232 = '/Users/SamHill/Documents/botcar/botcar-data/collections/CatesbyHS232.csv'
#CatesbyNH1 = '/Users/SamHill/Documents/botcar/botcar-data/collections/CatesbyNH1.csv'
#CatesbyNH2 = '/Users/SamHill/Documents/botcar/botcar-data/collections/CatesbyNH2.csv'
#catesbySpecimens = '/Users/SamHill/Documents/botcar/botcar-data/collections/catesbySpecimens.csv'
#botcarLabels = '/Users/SamHill/Documents/botcar/botcar-data/collections/botcarLabels.csv'
# Lord stuff
lordFolio = '/Users/SamHill/Documents/botcar/botcar-data/collections/LordFolio.csv'
lordLabel = '/Users/SamHill/Documents/botcar/botcar-data/collections/LordLabelCollection.csv'
lordSpecimens = '/Users/SamHill/Documents/botcar/botcar-data/collections/LordSpecimens.csv'
# Images
imgcollections = '/Users/SamHill/Documents/botcar/botcar-data/images/collections/imgcollections.csv'
CatesbyHSimg = '/Users/SamHill/Documents/botcar/botcar-data/images/imagedata/CatesbyHSimg.csv'
CatesbyNHimg = '/Users/SamHill/Documents/botcar/botcar-data/images/imagedata/CatesbyNHimg.csv'
# Texts
NH1_eng = '/Users/SamHill/Documents/botcar/botcar-data/texts-unformatted/NH1-eng.txt'
NH1_fra = '/Users/SamHill/Documents/botcar/botcar-data/texts-unformatted/NH1-fra.txt'
NH2_eng = '/Users/SamHill/Documents/botcar/botcar-data/texts-unformatted/NH2-eng.txt'
NH2_fra = '/Users/SamHill/Documents/botcar/botcar-data/texts-unformatted/NH2-fra.txt'
OUT_NH1 = '/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/NH1.xml'
OUT_NH2 = '/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/NH2.xml'

#print "Starting folios..."
#folioEdit = open('/Users/SamHill/Documents/botcar/botcar-data/collections/folios.csv', "rU")
#OUT_folio = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/collections/folio.csv', 'wb')
#OUT_image_folio = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/image-folio.tsv', 'wb')
#folio_reader = csv.reader(folioEdit)
#for row in folio_reader:
#	OUT_folio.write('"%s","%s",%s\n' % (row[0], row[1], row[2]))
#	if row[3] is not '':
#		for img in row[3].split(','):
#			OUT_image_folio.write('%s\t%s\n' % (img, row[0]))
#folioEdit.close()
#OUT_folio.close()
#OUT_image_folio.close()
#print "Finished folios!"

#print "Grabbing tsns..."
#tsn_Name = '/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/itisMySQL043014/longnames'
#tsn_list = []
#with open(tsn_Name) as f:
#    lines = f.readlines()
#for tsn_pair in lines:
#	tsn_list.append(tsn_pair.split('|'))

#print "Starting families..."
#families = open('/Users/SamHill/Documents/botcar/botcar-data/collections/families.csv', "rU")
#OUT_families = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/collections/families.csv', 'wb')
#families_reader = csv.reader(families)
#for row in families_reader:
#	id = 'tsn'
#	# IGNORE HEADER
#	if row[0] != 'familyURN':
#		for tsn in tsn_list:
#			# rstrip() removes trailing characters
#			if tsn[1].rstrip() == row[1]:
#				id = tsn[0]
#				break
#			else:
#				id = 'to be added'
#	OUT_families.write('"%s","%s",%s\n' % (row[0], row[1], id))
#families.close()
#OUT_families.close()
#print "Finished families!"

#print "Starting genera..."
#genera = open('/Users/SamHill/Documents/botcar/botcar-data/collections/genera.csv', "rU")
#OUT_genera = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/collections/genera.csv', 'wb')
#genera_reader = csv.reader(genera)
#for row in genera_reader:
#	id = 'tsn'
#	# IGNORE HEADER
#	if row[0] != 'genusURN':
#		for tsn in tsn_list:
#			if tsn[1].rstrip() == row[1]:
#				id = tsn[0]
#				break
#			else:
#				id = 'to be added'
#	OUT_genera.write('"%s","%s",%s\n' % (row[0], row[1], id))
#genera.close()
#OUT_genera.close()
#print "Finished genera!"

#print "Starting species..."
#species = open('/Users/SamHill/Documents/botcar/botcar-data/collections/species.csv', "rU")
#OUT_species = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/collections/species.csv', 'wb')
#species_reader = csv.reader(species)
#for row in species_reader:
#	id = 'tsn'
#	# ONLY SEARCH FIRST TWO WORDS IGNORING HEADER
#	if row[0] != 'speciesURN':
#		row1 = row[1].split(' ')
#		search_text = row1[0] + ' ' + row1[1]
#		for tsn in tsn_list:
#			if tsn[1].rstrip() == search_text:
#				id = tsn[0]
#				break
#			else:
#				id = 'to be added'
#	OUT_species.write('"%s","%s",%s\n' % (row[0], row[1], id))
#species.close()
#OUT_species.close()
#print "Finished species!"

#print "Starting specimen..."
#specimenEdit = open('/Users/SamHill/Documents/botcar/botcar-data/collections/specimen.csv', "rU")
#OUT_specimen = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/collections/specimen.csv', 'wb')
#OUT_specimen_species = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/specimen-species.tsv', 'wb')
#OUT_image_specimen = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/image-specimen.tsv', 'wb')
#specimen_reader = csv.reader(specimenEdit)
#for row in specimen_reader:
#	if row[2] != '':
#		OUT_specimen_species.write('%s\t%s\n' % (row[0], row[2]))
#	if row[3] != '':
#		OUT_image_specimen.write('%s\t%s\n' % (row[0], row[3]))
#	if row[4] != '':
#		OUT_image_specimen.write('%s\t%s\n' % (row[0], row[4]))
#	OUT_specimen.write('"%s","%s"\n' % (row[0], row[1]))
#specimenEdit.close()
#OUT_specimen.close()
#OUT_specimen_species.close()
#OUT_image_specimen.close()
#print "Finished specimen!"

print "Starting labels..."
#botcarLabels = open('/Users/SamHill/Documents/botcar/botcar-data/collections/botcarLabels.csv', "rU") # URN,folioURN,imgURN,specimenURN,text,Contributer,Date
#OUT_label_folio = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/label-folio.tsv', 'wb')
#label_reader = csv.reader(botcarLabels)
#for row in label_reader:
#	OUT_label_folio.write('%s\t%s\n' % (row[0], row[1]))
#botcarLabels.close()
#OUT_label_folio.close()
labelsEdit = open('/Users/SamHill/Documents/botcar/botcar-data/collections/labels.csv', "rU") # labelURN,text,specimenURN,imageURN,ROI
OUT_image_label = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/image-label.tsv', 'wb')
OUT_label_specimen = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/indices/label-specimen.tsv', 'wb')
OUT_label_penLabel = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/penLabel.xml', 'wb')
OUT_label_penLabel.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">\n\t<teiHeader>\n\t\t<fileDesc>\n\t\t\t<titleStmt>\n\t\t\t\t<title>Catesby: Labels on Specimens in the Sloane Herbarium</title>\n\t\t\t</titleStmt>\n\t\t\t<publicationStmt>\n\t\t\t\t<p>Transcribed by Amy Hackney Blackwell, 2014. From digital imagery taken at the Sloane Herbarium, 2012.</p>\n\t\t\t</publicationStmt>\n\t\t\t<sourceDesc>\n\t\t\t\t<p>Catesby\'s labels on specimens.</p>\n\t\t\t</sourceDesc>\n\t\t</fileDesc>\n\t</teiHeader>\n\t<text>\n\t\t<body>\n')
OUT_label_penOnPage = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/penOnPage.xml', 'wb')
OUT_label_penOnPage.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">\n\t<teiHeader>\n\t\t<fileDesc>\n\t\t\t<titleStmt>\n\t\t\t\t<title>Catesby: Labels on Specimens in the Sloane Herbarium</title>\n\t\t\t</titleStmt>\n\t\t\t<publicationStmt>\n\t\t\t\t<p>Transcribed by Amy Hackney Blackwell, 2014. From digital imagery taken at the Sloane Herbarium, 2012.</p>\n\t\t\t</publicationStmt>\n\t\t\t<sourceDesc>\n\t\t\t\t<p>Catesby\'s labels on specimens.</p>\n\t\t\t</sourceDesc>\n\t\t</fileDesc>\n\t</teiHeader>\n\t<text>\n\t\t<body>\n')
OUT_label_pencilOnPage = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/pencilOnPage.xml', 'wb')
OUT_label_pencilOnPage.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">\n\t<teiHeader>\n\t\t<fileDesc>\n\t\t\t<titleStmt>\n\t\t\t\t<title>Catesby: Labels on Specimens in the Sloane Herbarium</title>\n\t\t\t</titleStmt>\n\t\t\t<publicationStmt>\n\t\t\t\t<p>Transcribed by Amy Hackney Blackwell, 2014. From digital imagery taken at the Sloane Herbarium, 2012.</p>\n\t\t\t</publicationStmt>\n\t\t\t<sourceDesc>\n\t\t\t\t<p>Catesby\'s labels on specimens.</p>\n\t\t\t</sourceDesc>\n\t\t</fileDesc>\n\t</teiHeader>\n\t<text>\n\t\t<body>\n')
OUT_label_typedLabel = open('/Users/SamHill/Documents/botcar/botcar-data/TMP_Reworking/texts/typedLabel.xml', 'wb')
OUT_label_typedLabel.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" schematypens="http://relaxng.org/ns/structure/1.0"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">\n\t<teiHeader>\n\t\t<fileDesc>\n\t\t\t<titleStmt>\n\t\t\t\t<title>Catesby: Labels on Specimens in the Sloane Herbarium</title>\n\t\t\t</titleStmt>\n\t\t\t<publicationStmt>\n\t\t\t\t<p>Transcribed by Amy Hackney Blackwell, 2014. From digital imagery taken at the Sloane Herbarium, 2012.</p>\n\t\t\t</publicationStmt>\n\t\t\t<sourceDesc>\n\t\t\t\t<p>Catesby\'s labels on specimens.</p>\n\t\t\t</sourceDesc>\n\t\t</fileDesc>\n\t</teiHeader>\n\t<text>\n\t\t<body>\n')
label_reader = csv.reader(labelsEdit)
for row in label_reader:
#	OUT_image_label.write('%s\t%s\n' % (row[0], row[3]))
#	OUT_label_specimen.write('%s\t%s\n' % (row[0], row[2]))
	if row[0] != 'labelURN':
		split_row = row[0].split('.')
		first_four = split_row[1][:4]
		if first_four == 'penL':
			OUT_label_penLabel.write('\t\t\t<div n="' + split_row[1][8:] + '">\n' + '\t\t\t\t<p n="' + split_row[2] + '">' + row[1].replace('&', '&amp;') + '</p>\n' + '\t\t\t</div>\n')
		elif first_four == 'penO':
			OUT_label_penOnPage.write('\t\t\t<div n="' + split_row[1][9:] + '">\n' + '\t\t\t\t<p n="' + split_row[2] + '">' + row[1].replace('&', '&amp;') + '</p>\n' + '\t\t\t</div>\n')
		elif first_four == 'penc':
			OUT_label_pencilOnPage.write('\t\t\t<div n="' + split_row[1][12:] + '">\n' + '\t\t\t\t<p n="' + split_row[2] + '">' + row[1].replace('&', '&amp;') + '</p>\n' + '\t\t\t</div>\n')
		elif first_four == 'type':
			OUT_label_typedLabel.write('\t\t\t<div n="' + split_row[1][10:] + '">\n' + '\t\t\t\t<p n="' + split_row[2] + '">' + row[1].replace('&', '&amp;') + '</p>\n' + '\t\t\t</div>\n')
labelsEdit.close()
OUT_image_label.close()
OUT_label_specimen.close()
OUT_label_penLabel.write('\t\t</body>\n\t</text>\n</TEI>')
OUT_label_penLabel.close()
OUT_label_penOnPage.write('\t\t</body>\n\t</text>\n</TEI>')
OUT_label_penOnPage.close()
OUT_label_pencilOnPage.write('\t\t</body>\n\t</text>\n</TEI>')
OUT_label_pencilOnPage.close()
OUT_label_typedLabel.write('\t\t</body>\n\t</text>\n</TEI>')
OUT_label_typedLabel.close()
print "Finished labels!"
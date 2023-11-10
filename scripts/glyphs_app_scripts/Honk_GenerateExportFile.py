#MenuTitle: Honk - Generate Export File
__doc__="""
Generates export file for Honk
"""

import os
from AppKit import NSPoint

#initialise all necessary lists
font = Glyphs.font
allGlyphs = font.glyphs
bgNames = []
shadowNames = []
compNames = []
markNames = []
exporting = [g for g in allGlyphs if g.export]
exportingNames = [g.name for g in exporting]
nonExporting = [g for g in allGlyphs if g.export==False]
for eachGlyph in allGlyphs:
	nameArr = list(eachGlyph.name)
	if len(nameArr)>=2:
		if nameArr[0]=='b' and nameArr[1]=='g':
			bgNames.append(eachGlyph.name)
	if len(nameArr)>=6:
		if nameArr[0]=='s' and nameArr[1]=='h' and nameArr[2]=='a' and nameArr[3]=='d' and nameArr[4]=='o' and nameArr[5]=='w':
			shadowNames.append(eachGlyph.name)
	if len(nameArr)>=4:
		if nameArr[0]=='C' and nameArr[1]=='o' and nameArr[2]=='m' and nameArr[3]=='p':
			compNames.append(eachGlyph.name)
	if len(nameArr)>=4:
		if nameArr[0]=='M' and nameArr[1]=='a' and nameArr[2]=='r' and nameArr[3]=='k':
			compNames.append(eachGlyph.name)
componentNames = bgNames + shadowNames

#bg
bgs = ['none', 'none', 'none', 'none', 'bgUC1', 'bgUC1a', 'bgUC2b', 'bgUC1', 'bgUC2', 'bgUC2', 'bgUC1', 'bgUC1', 'bg5', 'bgUC2a', 'bgUC1_K', 'bgUC2a', 'bgUC3', 'bgUC1b', 'bgUC1', 'bgUC1', 'bg_Q', 'bgUC1_K', 'bgUC2', 'bgUC1b', 'bgUC1', 'bgUC1', 'bgUC3a', 'bgUC1', 'bgUC1', 'bgUC2', 'bgLC2', 'bgLC1ascender', 'bgLC2b', 'bgLC1ascender_d', 'bgLC2', 'bg4', 'bg1decender', 'bgLC1ascender', 'bg5', 'bg5descender', 'bgLC1_k', 'bg5', 'bgLC3', 'bgLC1', 'bgLC1a', 'bgLC1descender', 'bgLC1descender', 'bgLC1_r', 'bgLC2', 'bg4_t', 'bgLC1', 'bgLC1', 'bgLC3a', 'bgLC1', 'bg1decender', 'bgLC2', 'bgUC2', 'bg5', 'bgUC2', 'bgUC2', 'bgUC1', 'bgUC2', 'bgUC1a', 'bgUC2a', 'bgUC1', 'bgUC1a', 'bg_period', 'bg_comma', 'bg_colon', 'bg_semicolon', 'bg6', 'bg4', 'bg7', 'bg_hyphen', 'bg_hyphen', 'bg_hyphen', 'bg_underscore', 'bg7', 'bg7', 'bg7', 'bg7', 'bg7', 'bg7', 'bg_quote', 'bg_quote', 'bg_quote', 'bg7', 'bgUC9', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC2a', 'bgUC2a', 'bgUC2a', 'bgUC1descender', 'bgUC1', 'bgUC9', 'bgLC1_Thorn', 'bgUC1a', 'bgUC1b', 'bgLC9', 'bgUC1_bar', 'bgUC1_bar', 'bgLC2', 'bgUC1_bar', 'bg_idotless', 'bg_jdotless', 'bgLC1_K', 'bg5', 'bgLC1descender', 'bgLC1a', 'bgLC9', 'bgLC1_thorn', 'bgUC1a', 'bg4_t', 'bg_diac12a', 'bg_symbolsmall', 'bg_symbolsmall', 'bg_symbol', 'bg_symbol', 'bg7', 'bg7', 'bg_semicolon', 'bg4descender', 'none', 'bg_symbolsmall2', 'bg_symbolsmall', 'bg_symbol', 'bg7', 'bg_guillemet', 'bg_guillemet', 'bg_guilsingle', 'bg_guilsingle', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_tm', 'bg_degree', 'bg_quote', 'none', 'bg_symbol', 'bg_symbol', 'bg_symbolwide', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbolwide', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_diac3', 'bg_diac7', 'bg_diac1_flipped', 'bg_diac1', 'bg_diac6', 'bg_diac12', 'bg_diac5', 'bg_diac4', 'bg_diac4', 'bg_diac8', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6_flipped', 'bg_diac5', 'bg_diac14', 'bg_diac11', 'bg_diac7_below', 'bg_diac3_below', 'bg_diac14_below', 'bg_diac13_below', 'bg_diac13_below', 'bg_diac5_below', 'bg_diac2_below', 'bg_diac2', 'bg_diac1b_stacked', 'bg_diac1b_stacked_flipped', 'bg_diac1', 'bg_diac3n', 'bg_diac1n_flipped', 'bg_diac1n', 'bg_diac5', 'bg_diac4', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6', 'bg_diac13_below', 'bg_diac2_below', 'bg_diac3', 'bg_diac7_stacked', 'bg_diac1a_stacked', 'bg_diac1a_stacked_flipped', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac1_stacked', 'bg_diac1_stacked_flipped', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac2_stacked', 'bg_diac11a', 'bg_diac11a', 'none', 'bg_diac11b', 'bg_diac3_stacked', 'bg_diac1a_stacked', 'bg_diac1_stacked', 'bg_diac3_stacked', 'bg_diac2_stacked', 'bg_diac1_stacked', 'bg_diac5', 'bg_diac2_below', 'bg_diac5', 'bg_flag5', 'bg_flag3', 'bg_flag5', 'bg_flag3', 'bg_flag12', 'bg_flag5', 'bg_flag12', 'bg_flag10', 'bg_flag4', 'bg_flag6', 'bg_flag8', 'bg_flag7', 'bg_flag9', 'bg_flag4', 'bg_flag1', 'bg_flag8', 'bg_flag11', 'bg_flag5', 'bg_flag2', 'bg_flag3', 'bg_flag7', 'bg_flag3', 'bg_flag6', 'bg_flag10', 'bg_flag10', 'bg_flag4', 'bg_flag3', 'bg_flag2', 'bg_flag7', 'bg_flag11', 'bg_flag7', 'bg_okHand', 'bg_thumbsUpSign', 'none', 'bg_handWithFingersSplayed', 'bg_middleFinger', 'bg_foldedHands', 'bg_signOfTheHorns', 'bg_crossedFingers', 'bg_iLoveYouHandSign', 'none', 'none', 'bg_indexPointingRight', 'none', 'bg_raisedfist', 'bg_victoryHand', 'bg_u1FAF0', 'bg_eye', 'bg_symbol', 'bg_skull', 'bg_crossbones']

bgdecomp = ["p", "four", "endash", "emdash", "bar", "lslash", "one", "dieresiscomb.narrow", "gravecomb.narrow", "acutecomb.narrow", "circumflexcomb.narrow", "brevecomb.narrow", "tildecomb.narrow", "macroncomb.narrow", "hookabovecomb.narrow", "dblgravecomb.narrow", "ogonekcomb.narrow", "macronbelowcomb.narrow", "ordfeminine", "ordmasculine", "bullet", "asterisk", "indexPointingLeft", "thumbsDown", "indexPointingDown"]

#values
values = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for g in exporting]

values[exporting.index(allGlyphs["endash"])] = [32, 36, 80, 38, 36, 36, 36, 38, 32, 26]
values[exporting.index(allGlyphs["emdash"])] = [56, 62, 115, 65, 100, 62, 62, 64, 58, 50]
values[exporting.index(allGlyphs["bar"])] = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
values[exporting.index(allGlyphs["dieresiscomb.narrow"])] = [15, 20, 47, 18, 26, 15, 15, 15, 18, 28]
values[exporting.index(allGlyphs["acutecomb.narrow"])] = [22, 35, 50, 35, 38, 15, 18, 17, 22, 23]
values[exporting.index(allGlyphs["gravecomb.narrow"])] = [22, 35, 50, 35, 38, 15, 18, 17, 22, 23]
values[exporting.index(allGlyphs["dblgravecomb.narrow"])] = [24, 18, 50, 16, 28, 22, 20, 24, 31, 36]
values[exporting.index(allGlyphs["macroncomb.narrow"])] = [0, 12, 40, 7, 0, 0, 0, 0, 0, 12]
values[exporting.index(allGlyphs["macronbelowcomb.narrow"])] = [0, 12, 40, 7, 0, 14, 22, 16, 22, 20]
values[exporting.index(allGlyphs["tildecomb.narrow"])] = [20, 18, 50, 17, 20, 18, 20, 20, 25, 20]
values[exporting.index(allGlyphs["circumflexcomb.narrow"])] = [28, 23, 50, 16, 28, 20, 20, 18, 26, 38]
values[exporting.index(allGlyphs["invertedbrevecomb.narrow"])] = [20, 22, 50, 18, 14, 18, 18, 18, 26, 28]
values[exporting.index(allGlyphs["brevecomb.narrow"])] = [20, 22, 52, 18, 20, 22, 22, 20, 24, 30]
values[exporting.index(allGlyphs["dieresisacutecomb.narrow"])] = [22, 20, 50, 16, 20, 16, 20, 20, 20, 26]
values[exporting.index(allGlyphs["lslash"])] = [35, 30, 55, 30, 54, 34, 32, 32, 30, 22]
values[exporting.index(allGlyphs["one"])] = [35, 30, 55, 30, 54, 34, 32, 32, 30, 22]
values[exporting.index(allGlyphs["question"])] = [0, 0, 27, 0, 0, 0, 0, 0, 0, 0]

#factors
factorX = [0 for g in exporting]
factorY = [0 for g in exporting]
incW = ["endash", "emdash", "lslash", "one"]
decW = ["question", "bar", "dblgravecomb.narrow", "macroncomb.narrow", "macronbelowcomb.narrow", "tildecomb.narrow", "circumflexcomb.narrow", "invertedbrevecomb.narrow", "brevecomb.narrow", "hookabovecomb.narrow", "dieresisacutecomb.narrow"]
for g in exporting:
	i = exporting.index(g)
	if g.name in incW:
		factorX[i] = 1
	if g.name in decW:
		factorX[i] = -1

#is flip?
flipV = ["p", "four", "dblgravecomb.narrow"]
isFlipV = [False for g in exporting]
for g in exporting:
	i = exporting.index(g)
	if g.name in flipV:
		isFlipV[i] = True

#diacritics lists
diacriticGlyphs = ['Aacute', 'Abreve', 'Abreveacute', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Acircumflex', 'Acircumflexacute', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Adblgrave', 'Adieresis', 'Adotbelow', 'Agrave', 'Ahookabove', 'Ainvertedbreve', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AEacute', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'Dcaron', 'Ddotbelow', 'Dmacronbelow', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'Ecircumflexacute', 'Ecircumflexgrave', 'Ecircumflexhookabove', 'Ecircumflextilde', 'Edblgrave', 'Edieresis', 'Edotaccent', 'Edotbelow', 'Egrave', 'Ehookabove', 'Einvertedbreve', 'Emacron', 'Emacronacute', 'Emacrongrave', 'Eogonek', 'Etilde', 'Gbreve', 'Gcaron', 'Gcircumflex', 'Gcommaaccent', 'Gdotaccent', 'Gmacron', 'Hbrevebelow', 'Hcircumflex', 'Hdotbelow', 'Idotaccent', 'Idotbelow', 'Jacute', 'Jcircumflex', 'Kcommaaccent', 'Lacute', 'Lcommaaccent', 'Ldotbelow', 'Lmacronbelow', 'Mdotbelow', 'Nacute', 'Ncaron', 'Ncommaaccent', 'Ndotaccent', 'Ndotbelow', 'Nmacronbelow', 'Ntilde', 'Oacute', 'Obreve', 'Ocircumflex', 'Ocircumflexacute', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Odblgrave', 'Odieresis', 'Odieresismacron', 'Odotaccentmacron', 'Odotbelow', 'Ograve', 'Ohookabove', 'Ohungarumlaut', 'Oinvertedbreve', 'Omacron', 'Omacronacute', 'Omacrongrave', 'Oogonek', 'Otilde', 'Otildeacute', 'Otildedieresis', 'Otildemacron', 'Racute', 'Rcaron', 'Rcommaaccent', 'Rdblgrave', 'Rdotbelow', 'Rinvertedbreve', 'Rmacronbelow', 'Sacute', 'Sacutedotaccent', 'Scaron', 'Scarondotaccent', 'Scedilla', 'Scircumflex', 'Scommaaccent', 'Sdotaccent', 'Sdotbelow', 'Tcaron', 'Tcedilla', 'Tcommaaccent', 'Tdotbelow', 'Tmacronbelow', 'Uacute', 'Ubreve', 'Ucircumflex', 'Udblgrave', 'Udieresis', 'Udotbelow', 'Ugrave', 'Uhookabove', 'Uhungarumlaut', 'Uinvertedbreve', 'Umacron', 'Umacrondieresis', 'Uogonek', 'Uring', 'Utilde', 'Utildeacute', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'Yacute', 'Ycircumflex', 'Ydieresis', 'Ydotaccent', 'Ydotbelow', 'Ygrave', 'Yhookabove', 'Ymacron', 'Ytilde', 'Zacute', 'Zcaron', 'Zdotaccent', 'Zdotbelow', 'aacute', 'abreve', 'abreveacute', 'abrevegrave', 'abrevehookabove', 'abrevetilde', 'acircumflex', 'acircumflexacute', 'acircumflexgrave', 'acircumflexhookabove', 'acircumflextilde', 'adblgrave', 'adieresis', 'adotbelow', 'agrave', 'ahookabove', 'ainvertedbreve', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'aeacute', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'ddotbelow', 'dmacronbelow', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'ecircumflexacute', 'ecircumflexgrave', 'ecircumflexhookabove', 'ecircumflextilde', 'edblgrave', 'edieresis', 'edotaccent', 'edotbelow', 'egrave', 'einvertedbreve', 'emacron', 'emacronacute', 'emacrongrave', 'eogonek', 'etilde', 'gbreve', 'gcaron', 'gcircumflex', 'gcommaaccent', 'gdotaccent', 'gmacron', 'hbrevebelow', 'hdotbelow', 'idotbelow', 'kcommaaccent', 'lacute', 'lcommaaccent', 'ldotbelow', 'mdotbelow', 'nacute', 'ncaron', 'ncommaaccent', 'ndotaccent', 'ndotbelow', 'nmacronbelow', 'ntilde', 'oacute', 'obreve', 'ocircumflex', 'ocircumflexacute', 'ocircumflexgrave', 'ocircumflexhookabove', 'ocircumflextilde', 'odblgrave', 'odieresis', 'odieresismacron', 'odotaccentmacron', 'odotbelow', 'ograve', 'ohookabove', 'ohungarumlaut', 'oinvertedbreve', 'omacron', 'omacronacute', 'omacrongrave', 'oogonek', 'otilde', 'otildeacute', 'otildedieresis', 'otildemacron', 'racute', 'rcaron', 'rcommaaccent', 'rdblgrave', 'rdotbelow', 'rinvertedbreve', 'rmacronbelow', 'sacute', 'sacutedotaccent', 'scaron', 'scarondotaccent', 'scedilla', 'scircumflex', 'scommaaccent', 'sdotaccent', 'sdotbelow', 'tcedilla', 'tcommaaccent', 'tdotbelow', 'tmacronbelow', 'uacute', 'ubreve', 'ucircumflex', 'udblgrave', 'udieresis', 'udotbelow', 'ugrave', 'uhookabove', 'uhungarumlaut', 'uinvertedbreve', 'umacron', 'umacrondieresis', 'uogonek', 'uring', 'utilde', 'utildeacute', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'yacute', 'ycircumflex', 'ydieresis', 'ydotaccent', 'ydotbelow', 'ygrave', 'yhookabove', 'ymacron', 'ytilde', 'zacute', 'zcaron', 'zdotaccent', 'zdotbelow', 'Iacute', 'Ibreve', 'Icircumflex', 'Idblgrave', 'Idieresis', 'Idieresisacute', 'Igrave', 'Ihookabove', 'Iinvertedbreve', 'Imacron', 'Iogonek', 'Itilde', 'iacute', 'ibreve', 'icircumflex', 'idblgrave', 'idieresis', 'idieresisacute', 'igrave', 'ihookabove', 'iinvertedbreve', 'imacron', 'iogonek', 'itilde', 'jacute', 'jcircumflex', 'lmacronbelow', 'tdieresis', 'Ohorn', 'Ohornacute', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Uhorn', 'Uhornacute', 'Uhorngrave', 'Uhornhookabove', 'Uhorntilde', 'ohorn', 'ohornacute', 'ohorngrave', 'ohornhookabove', 'ohorntilde', 'uhorn', 'uhornacute', 'Ohorndotbelow', 'Uhorndotbelow', 'ohorndotbelow', 'uhorndotbelow', 'Oslashacute', 'oslashacute']
rightalign = ["Ohorn", "Ohornacute", "Ohorngrave", "Ohornhookabove", "Ohorntilde", "Uhorn", "Uhornacute", "Uhorngrave", "Uhornhookabove", "Uhorntilde", "ohorn","ohornacute", "ohorngrave", "ohornhookabove", "ohorntilde", "uhorn", "uhornacute"]
narrow = ["Iacute", "Ibreve", "Icircumflex", "Idblgrave", "Idieresis", "Idieresisacute", "Igrave", "Ihookabove", "Iinvertedbreve", "Imacron", "Iogonek", "Itilde", "iacute", "ibreve", "icircumflex", "idblgrave", "idieresis", "idieresisacute", "igrave", "ihookabove", "iinvertedbreve", "imacron", "iogonek", "itilde", "jacute", "jcircumflex", "lacute", "lmacronbelow", "tdieresis"]
below = ["dotbelowcomb", "dieresisbelowcomb", "commaaccentcomb", "cedillacomb", "ogonekcomb", "brevebelowcomb", "macronbelowcomb", "ogonekcomb.narrow", "macronbelowcomb.narrow", "macronbelowcomb.R"]
hornEx = ["Ohorndotbelow", "Uhorndotbelow", "ohorndotbelow", "uhorndotbelow"]
caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "l", "t", "AE", "Oslash"]
capmove = [204, 204, 204, 204, 204, 204, 204, 204, 244, 244]
dblDiacritics = ["Abrevedotbelow", "Acircumflexdotbelow", "Ccedillaacute", "Ecedillabreve", "Ecircumflexdotbelow", "Ocircumflexdotbelow", "Sdotbelowdotaccent", "abrevedotbelow", "acircumflexdotbelow", "ccedillaacute", "ecedillabreve", "ecircumflexdotbelow", "ocircumflexdotbelow", "sdotbelowdotaccent"]
otherGlyphs = ["DZ", "Dz", "LJ", "Lj", "NJ", "Nj", "dz", "lj", "nj", "fi", "fl", "DZcaron", "Dzcaron", "dzcaron", "dcaron", "lcaron", "IJ", "ij", "ldot", "quotedbl", "quotedblleft", "quotedblright", "quotedblbase", "second"]
diacritics2 = ['dieresis', 'grave', 'acute', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'hungarumlaut', 'dotaccent']

def addBg(glyphname, compname, values, factorX, factorY, isFlipV):
	thisGlyph = exporting[exporting.index(allGlyphs[glyphname])]
	myLayers = thisGlyph.layers
	i = 0
	for thisLayer in myLayers:
		newComponent = GSComponent(compname)
		thisLayer.components.append(newComponent)
		nComp = len(thisLayer.components)-1
		element = thisLayer.components[nComp]
		percentage = values[i] / 100.0
		scaleX = element.scale.x + factorX * percentage
		scaleY = element.scale.y + factorY * percentage
		element.scale = NSPoint(scaleX, scaleY)
		lsb = allGlyphs[element.name].layers[i].LSB
		m = round(lsb * percentage)
		element.x += -m * factorX
		bounds = element.bounds
		if isFlipV:
			mid = bounds[0].x + bounds[1].width / 2
			x = element.bounds[0].x - element.x
			element.x = mid + (mid - element.x)
			element.scale = (-element.scale[0], element.scale[1])
		i += 1

def genDiacritics(): #generates all the necessary diacritic glyphs for extended Latin support
	i = 0
	while i < len(diacriticGlyphs):
		newGlyph = GSGlyph(diacriticGlyphs[i])
		allGlyphs.append(newGlyph)
		thisGlyph = allGlyphs[diacriticGlyphs[i]]
		
		if thisGlyph.name in hornEx:
			letter = list(thisGlyph.name)[0] + 'horn'
		elif thisGlyph.name in ['AEacute', 'aeacute']:
			letter = list(thisGlyph.name)[0] + list(thisGlyph.name)[1]
		elif thisGlyph.name in ['Oslashacute', 'oslashacute']:
			letter = list(thisGlyph.name)[0] + 'slash'
		else:
			letter = list(thisGlyph.name)[0]
		a,diacritic = thisGlyph.name.split(letter, 1)

		if letter in ["i", "j"]:
			if diacritic not in ["dotbelow", "ogonek"]:
				letter += "dotless"

		if thisGlyph.name in narrow:
			diacritic += 'comb.narrow'
		else:
			diacritic += 'comb'

		if thisGlyph.name in ['gcommaaccent']:
			diacritic = 'commaturnedabovecomb'

		if thisGlyph.name in ['Wdieresis', 'wdieresis']:
			diacritic = "dieresiscomb.w"
		
		if thisGlyph.name in ['AEacute', 'aeacute']:
			diacritic = "acutecomb.ae"
		
		if thisGlyph.name=="rinvertedbreve":
			diacritic = "invertedbrevecomb.r"
		
		if thisGlyph.name=="Rmacronbelow":
			diacritic = "macronbelowcomb.R"
		
		for thisLayer in thisGlyph.layers:
			lComp = GSComponent(letter)
			dComp = GSComponent(diacritic)
			thisLayer.components.append(lComp)
			thisLayer.width = allGlyphs[letter].layers[thisGlyph.layers.index(thisLayer)].width
			thisLayer.components.append(dComp)
			n = len(thisLayer.components)-1
			element = thisLayer.components[n]
			bounds = thisLayer.bounds
			center = thisLayer.bounds.origin.x + allGlyphs[letter].layers[thisGlyph.layers.index(thisLayer)].bounds.size.width/2
			if thisGlyph.name in rightalign:
				x = element.bounds.origin.x - element.x
				element.x = allGlyphs[letter].layers[thisGlyph.layers.index(thisLayer)].width - element.bounds.size.width - x - allGlyphs[letter].layers[thisGlyph.layers.index(thisLayer)].RSB
			elif thisGlyph.name=="tdieresis":
				element.x -= element.bounds.origin.x - thisLayer.LSB
			else:
				x = element.bounds.origin.x - element.x
				element.x = center - element.bounds.size.width/2 - x
			if letter in caps:
				if diacritic not in below:
					element.y += capmove[thisGlyph.layers.index(thisLayer)]
			if thisGlyph.name in ["ydotbelow"]:
				element.y -= capmove[thisGlyph.layers.index(thisLayer)]
		i += 1

	#double diacritics where one is above and one is below
	k = 0
	while k < len(dblDiacritics):
		newGlyph = GSGlyph(dblDiacritics[k])
		allGlyphs.append(newGlyph)
		thisGlyph = allGlyphs[dblDiacritics[k]]

		letter = list(thisGlyph.name)[0]
		a, dfull = thisGlyph.name.split(letter, 1)
		dlist = list(dfull)
		f = dfull.find('dotbelow')
		d1, d2 = '', ''
		if f!=-1:
			d1 = 'dotbelow'
			d2 = dfull.replace(d1, '')
		else:
			d1 = 'cedilla'
			d2 = dfull.replace(d1, '')
		d1 += 'comb'
		d2 += 'comb'

		for thisLayer in thisGlyph.layers:
			comp = GSComponent(letter)
			comp1 = GSComponent(d1)
			comp2 = GSComponent(d2)
			thisLayer.components.append(comp)
			thisLayer.width = allGlyphs[letter].layers[thisGlyph.layers.index(thisLayer)].width
			thisLayer.components.append(comp1)
			thisLayer.components.append(comp2)
			n1 = len(thisLayer.components)-2 
			n2 = len(thisLayer.components)-1
			element1 = thisLayer.components[n1]
			element2 = thisLayer.components[n2]
			bounds = thisLayer.bounds
			center = thisLayer.bounds.origin.x + thisLayer.bounds.size.width/2
			x1 = element1.bounds.origin.x - element1.x
			element1.x = center - element1.bounds.size.width/2 - x1
			x2 = element2.bounds.origin.x - element2.x
			element2.x = center - element2.bounds.size.width/2 - x2
			if letter in caps:
				if d1 not in below:
					element1.y += capmove[thisGlyph.layers.index(thisLayer)]
				if d2 not in below:
					element2.y += capmove[thisGlyph.layers.index(thisLayer)]
		k+=1
	
	#non-break space and idotaccent
	allGlyphs["space"].duplicate("nbspace")
	allGlyphs["i"].duplicate("idotaccent")
	allGlyphs["Eth"].duplicate("Dcroat")
	allGlyphs["periodcentered"].duplicate("periodcentered.loclCAT")
	allGlyphs["comma"].duplicate("quotesinglbase")
	allGlyphs["increment"].duplicate("Delta")
	allGlyphs["Delta"].unicode = "0394"
	allGlyphs["Delta"].script = "greek"
	allGlyphs["Delta"].category = "Letter"
	allGlyphs["Ohm"].duplicate("Omega")
	allGlyphs["Omega"].unicode = "03A9"
	allGlyphs["Omega"].script = "greek"
	allGlyphs["Omega"].category = "Letter"

	#other glyphs
	j = 0
	while j < len(otherGlyphs):
		newGlyph = GSGlyph(otherGlyphs[j])
		allGlyphs.append(newGlyph)
		thisGlyph = allGlyphs[otherGlyphs[j]]
		glyph1 = list(thisGlyph.name)[0]
		a,glyph2 = thisGlyph.name.split(glyph1, 1)
		if glyph2 == 'caron':
			glyph2 = 'caroncomb.alt'
		if glyph2 == 'dot':
			glyph2 = 'periodcentered'
		if thisGlyph.name=="quotedbl":
			glyph1 = "quotesingle"
			glyph2 = "quotesingle"
		if thisGlyph.name=="quotedblleft":
			glyph1 = "quoteleft"
			glyph2 = "quoteleft"
		if thisGlyph.name=="quotedblright":
			glyph1 = "quoteright"
			glyph2 = "quoteright"
		if thisGlyph.name=="quotedblbase":
			glyph1 = "quotesinglbase"
			glyph2 = "quotesinglbase"
		if thisGlyph.name=="second":
			glyph1 = "minute"
			glyph2 = "minute"
		for thisLayer in thisGlyph.layers:
			comp1 = GSComponent(glyph1)
			comp2 = GSComponent(glyph2)
			thisLayer.components.append(comp1)
			thisLayer.components.append(comp2)
			n = len(thisLayer.components)-1
			element = thisLayer.components[n]
			element.x += allGlyphs[glyph1].layers[thisGlyph.layers.index(thisLayer)].width
			thisLayer.width = allGlyphs[glyph1].layers[thisGlyph.layers.index(thisLayer)].width + allGlyphs[glyph2].layers[thisGlyph.layers.index(thisLayer)].width
		j += 1

	#diacritic duplicates
	v = 0
	while v < len(diacritics2):
		newGlyph = GSGlyph(diacritics2[v])
		allGlyphs.append(newGlyph)
		thisGlyph = allGlyphs[diacritics2[v]]
		compname = thisGlyph.name + 'comb'
		for thisLayer in thisGlyph.layers:
			comp = GSComponent(compname)
			thisLayer.components.append(comp)
			thisLayer.width = allGlyphs[compname].layers[thisGlyph.layers.index(thisLayer)].width
		v+=1
	
	#ellipsis
	newGlyph = GSGlyph("ellipsis")
	allGlyphs.append(newGlyph)
	thisGlyph = allGlyphs["ellipsis"]
	compname = "period"
	for thisLayer in thisGlyph.layers:
		comp1 = GSComponent(compname)
		thisLayer.components.append(comp1)
		comp2 = GSComponent(compname)
		thisLayer.components.append(comp2)
		n = len(thisLayer.components)-1
		element = thisLayer.components[n]
		element.x += allGlyphs[glyph1].layers[thisGlyph.layers.index(thisLayer)].width
		comp3 = GSComponent(compname)
		thisLayer.components.append(comp3)
		n = len(thisLayer.components)-1
		element = thisLayer.components[n]
		element.x += (allGlyphs[glyph1].layers[thisGlyph.layers.index(thisLayer)].width)*2
		thisLayer.width = (allGlyphs[glyph1].layers[thisGlyph.layers.index(thisLayer)].width)*3	

def swapBG(thisGlyph): #swaps every layer of input glyph with its bg
	for eachLayer in thisGlyph.layers:
		eachLayer.swapForegroundWithBackground()

def decomposeExporting(myGlyphs): #goes through all the glyphs in the input list and decomposes any components inside it that are exporting glyphs
	for thisGlyph in myGlyphs:
		for eachLayer in thisGlyph.layers:
			allComponents = eachLayer.components
			nComp = len(allComponents)-1
			if nComp >= 0:
				nc = 0
				while nc <= nComp:
					myComponent = allComponents[nc]
					if myComponent.name in exportingNames:
						myComponent.decompose()
						nComp = len(allComponents)-1
					else:
						nc += 1
				

def addColorLayers(myGlyphs): #adds necessary color layers to all glyphs in the input list

	Glyphs.clearLog()

	CPAL = None
	parameterName = "Color Palettes"

	for m in font.masters:
		mID = m.id
		CPAL = m.customParameters[parameterName]

		if not CPAL:
			CPAL = font.customParameters[parameterName]

		if CPAL:
			paletteSize = len(CPAL[0])
			for thisGlyph in myGlyphs:
				print("\n🔠 %s" % thisGlyph.name)
				newLayer = thisGlyph.layers[mID].copy()
				newLayer.setColorPaletteLayer_(1)
				newLayer.setAttribute_forKey_(0, "colorPalette")
				thisGlyph.layers.append(newLayer)
				print("✅ Added: " + thisGlyph.layers[mID].name + " Color %i" % 0)
				newLayer = thisGlyph.layers[mID].copy()
				newLayer.setColorPaletteLayer_(1)
				newLayer.setAttribute_forKey_(2, "colorPalette")
				thisGlyph.layers.append(newLayer)
				print("✅ Added: " + thisGlyph.layers[mID].name + " Color %i" % 0)
				newLayer = thisGlyph.layers[mID].copy()
				newLayer.setColorPaletteLayer_(1)
				newLayer.setAttribute_forKey_(0, "colorPalette")
				thisGlyph.layers.append(newLayer)
				print("✅ Added: " + thisGlyph.layers[mID].name + " Color %i" % 0)
		else:
			Message(
				title="No Palette Found",
				message="No ‘Color Palettes’ parameter found in Font Info > Font or Font Info > Masters. Please add the parameter and try again.",
				OKButton=None,
				)   

def distribute(myGlyphs): #goes through all glyphs in the input list and distributes components across the color layers
	for thisGlyph in myGlyphs:
		if thisGlyph.export:
			numberOfLayers = len(thisGlyph.layers)
			i = 0
			while i < numberOfLayers:
				eachLayer = thisGlyph.layers[i]
				if((i==11) or (i==14) or (i==17) or (i==20) or (i==23) or (i==26) or (i==29) or (i==32) or (i==35) or (i==38) or (i==10) or (i==13) or (i==16) or (i==19) or (i==22) or (i==25) or (i==28) or (i==31) or (i==34) or (i==37)):
					for m in range(len(eachLayer.shapes)-1, -1, -1):
						path = eachLayer.shapes[m]
						if isinstance(path, GSPath):
							del(eachLayer.shapes[m])
				#color1: keep only bg
				if (i==11) or (i==14) or (i==17) or (i==20) or (i==23) or (i==26) or (i==29) or (i==32) or (i==35) or (i==38):
					theseComponents = eachLayer.components
					numberOfComponents = len(theseComponents)
					j = 0
					while j < numberOfComponents:
						thisComponent = theseComponents[j]
						if thisComponent.componentName in bgNames:
							j += 1
						else:
							index = eachLayer.shapes.index(thisComponent)
							del (eachLayer.shapes[index])
							numberOfComponents -= 1
					numberOfShapes = len(eachLayer.shapes)
					if numberOfShapes > 0:
						for m in range(len(eachLayer.shapes)-1, -1, -1):
							path = eachLayer.shapes[m]
							if isinstance(path, GSPath):
								del thisLayer.shapes[m]
					if (thisGlyph.name in bgdecomp) or (thisGlyph.name in narrow):
						nc = len(eachLayer.components)
						while nc>0:
							c = eachLayer.components[nc-1]
							c.decompose()
							nc -= 1
				#first color0: keep only shadow
				elif (i==10) or (i==13) or (i==16) or (i==19) or (i==22) or (i==25) or (i==28) or (i==31) or (i==34) or (i==37):
					theseComponents = eachLayer.components
					numberOfComponents = len(theseComponents)
					j = 0
					while j < numberOfComponents:
						thisComponent = theseComponents[j]
						if thisComponent.componentName in shadowNames:
							j += 1
						else:
							index = eachLayer.shapes.index(thisComponent)
							del (eachLayer.shapes[index])
							numberOfComponents -= 1
					numberOfShapes = len(eachLayer.shapes)
					if numberOfShapes > 0:
						for m in range(len(eachLayer.shapes)-1, -1, -1):
							path = eachLayer.shapes[m]
							if isinstance(path, GSPath):
								del thisLayer.shapes[m]
				#base layer and second color0: delete bg and shadow
				else:
					theseComponents = eachLayer.components
					numberOfComponents = len(theseComponents)
					j = 0
					while j < numberOfComponents:
						thisComponent = theseComponents[j]
						if thisComponent.componentName in componentNames:
							index = eachLayer.shapes.index(thisComponent)
							del(eachLayer.shapes[index])
							numberOfComponents -= 1
						else:
							j += 1
				i += 1

#calling all the functions
#add bgs
for thisGlyph in exporting:
	ind = exporting.index(thisGlyph)
	if bgs[ind]=="none":
		pass
	else:
		addBg(thisGlyph.name, bgs[ind], values[ind], factorX[ind], factorY[ind], isFlipV[ind])

for thisGlyph in allGlyphs:
	if thisGlyph.name in compNames:
		for eachLayer in thisGlyph.layers:
			theseComponents = eachLayer.components
			numberOfComponents = len(theseComponents)
			while numberOfComponents > 0:
				thisComponent = theseComponents[0]
				thisComponent.decompose()
				numberOfComponents = len(eachLayer.components)
#generate all necessary diacritic glyphs, update exporting
genDiacritics()
exporting = [g for g in allGlyphs if g.export]
exportingNames = [g.name for g in exporting]
#swap shadow glyphs with background
for thisGlyph in allGlyphs:
	if thisGlyph.name in shadowNames:
		swapBG(thisGlyph)
#decompose glyphs that contain components that are exporting
decomposeExporting(allGlyphs)
#add color layers to all exporting glyphs
addColorLayers(exporting)
#distributes components across color layers
distribute(exporting)
#make a copy of the glyphs file and saves it
dst = os.path.join(os.path.dirname(font.filepath), "HonkExportFile.glyphs")
#duplicate masters to generate Shadow masters
for master in font.masters:
	masterCopy = master.copy()
	font.masters.append(masterCopy)
	font.copyInfoFrom_sourceFontMasterID_targetFontMasterID_(font, master.id, masterCopy.id)
i = 10
numberOfMasters = len(font.masters)
#edit name of duplicated masters and set shadow axis value to maximum
while i < numberOfMasters:
	thisMaster = font.masters[i]
	thisMaster.name = thisMaster.name + " Shadow"
	thisMaster.axes[1] = 100
	shadowValue = {
	"Axis": "Shadow",
	"Location": 100
	}
	thisMaster.customParameters["Axis Location"][1] = shadowValue
	#swaps shadow glyphs with the background only in the shadow masters
	for glyph in font.glyphs:
		if glyph.name in shadowNames:
			glyph.layers[i].swapForegroundWithBackground()
	i += 1
#clears background of all glyphs
for thisGlyph in allGlyphs:
	for thisLayer in thisGlyph.layers:
		thisLayer.swapForegroundWithBackground()
		thisLayer.clear()
		thisLayer.swapForegroundWithBackground()
	#makes comp glyphs exporting
	if (thisGlyph.name in compNames) or (thisGlyph.name in markNames) or (thisGlyph.name in componentNames) or (thisGlyph.name=='symbol'):
		thisGlyph.export = True
#deletes all instances except Regular
exports = Glyphs.font.instances
i = 0
l = len(exports)
while i < l:
	e = exports[i]
	if e.name=='Regular':
		i += 1
	else:
		exports.remove(e)
		l -= 1
font.save(dst)
print("done!")

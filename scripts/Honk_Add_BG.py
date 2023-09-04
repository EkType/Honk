#MenuTitle: Honk - Add BG
__doc__="""
Adds BG components to all glyphs and modifies the components as needed
"""

from AppKit import NSPoint

allGlyphs = Glyphs.font.glyphs
exp = [g for g in allGlyphs if g.export]

def addBg(glyphname, compname, values, factorX, factorY, isFlipH, isFlipV):
	thisGlyph = exp[exp.index(allGlyphs[glyphname])]
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
		if glyphname in ["semicolon", "exclamdown"]:
			element.y = element.y + 100
		if isFlipH:
			mid = bounds[0].y + bounds[1].height / 2
			y = element.bounds[0].y - element.y
			element.y = mid + (mid - element.y)
			element.scale = (element.scale[0], -element.scale[1])
		elif isFlipV:
			mid = bounds[0].x + bounds[1].width / 2
			x = element.bounds[0].x - element.x
			element.x = mid + (mid - element.x)
			element.scale = (-element.scale[0], element.scale[1])
		i += 1

#values
values = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for g in exp]

values[exp.index(allGlyphs["N"])] = [0, 0, 0, 0, 20, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["T"])] = [0, 0, 0, 0, 20, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["Tbar"])] = [0, 0, 0, 0, 20, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["B"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["six"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["nine"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["E"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["S"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["Z"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["zero"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["two"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["three"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["five"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["F"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["J"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["L"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["seven"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["C"])] = [6, 6, 6, 6, 28, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["c"])] = [6, 6, 6, 6, 28, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["o"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["a"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["e"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["s"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["z"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["guilsinglleft"])] = [28, 0, 34, 16, 35, 30, 10, 28, 20, 20]
values[exp.index(allGlyphs["guilsinglright"])] = [28, 0, 34, 16, 35, 30, 10, 28, 20, 20]
values[exp.index(allGlyphs["guillemetleft"])] = [125, 95, 138, 113, 138, 130, 100, 128, 128, 113]
values[exp.index(allGlyphs["guillemetright"])] = [125, 95, 138, 113, 138, 130, 100, 128, 128, 113]
values[exp.index(allGlyphs["semicolon"])] = [66, 66, 66, 66, 66, 66, 66, 66, 70, 66]
values[exp.index(allGlyphs["exclamdown"])] = [66, 66, 66, 66, 66, 66, 66, 66, 70, 66]
values[exp.index(allGlyphs["endash"])] = [32, 36, 80, 38, 36, 36, 36, 38, 32, 26]
values[exp.index(allGlyphs["emdash"])] = [56, 62, 115, 65, 100, 62, 62, 64, 58, 50]
values[exp.index(allGlyphs["bar"])] = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
values[exp.index(allGlyphs["dieresiscomb.narrow"])] = [15, 20, 47, 18, 20, 15, 15, 15, 18, 28]
values[exp.index(allGlyphs["acutecomb.narrow"])] = [22, 35, 50, 35, 38, 15, 18, 17, 22, 23]
values[exp.index(allGlyphs["gravecomb.narrow"])] = [22, 35, 50, 35, 38, 15, 18, 17, 22, 23]
values[exp.index(allGlyphs["dblgravecomb.narrow"])] = [24, 18, 50, 16, 20, 22, 20, 24, 39, 36]
values[exp.index(allGlyphs["macroncomb.narrow"])] = [0, 12, 40, 7, 0, 0, 0, 0, 0, 12]
values[exp.index(allGlyphs["macronbelowcomb.narrow"])] = [0, 12, 40, 7, 0, 0, 0, 0, 0, 12]
values[exp.index(allGlyphs["tildecomb.narrow"])] = [20, 18, 50, 17, 20, 18, 20, 20, 25, 20]
values[exp.index(allGlyphs["circumflexcomb.narrow"])] = [28, 26, 50, 16, 18, 20, 28, 18, 26, 38]
values[exp.index(allGlyphs["invertedbrevecomb.narrow"])] = [20, 22, 50, 18, 14, 18, 18, 18, 26, 28]
values[exp.index(allGlyphs["brevecomb.narrow"])] = [20, 22, 52, 18, 20, 22, 22, 20, 24, 30]
values[exp.index(allGlyphs["dieresisacutecomb.narrow"])] = [22, 20, 50, 16, 20, 16, 20, 20, 20, 26]
values[exp.index(allGlyphs["Lcaron"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["Ldot"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["Lslash"])] = [6, 6, 6, 6, 0, 6, 6, 6, 6, 6]
values[exp.index(allGlyphs["Germandbls"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["germandbls"])] = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["Tbar"])] = [0, 0, 0, 0, 20, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["schwa"])] = [6, 6, 6, 6, 18, 6, 6, 6, 6, 6] 
values[exp.index(allGlyphs["question"])] = [0, 0, 27, 0, 0, 0, 0, 0, 0, 0]
values[exp.index(allGlyphs["tbar"])] = [0, 0, 3, 0, 0, 2, 2, 0, 0, 5]
values[exp.index(allGlyphs["lslash"])] = [35, 30, 55, 30, 54, 34, 32, 32, 30, 22]
values[exp.index(allGlyphs["numero"])] = [22, 22, 22, 22, 22, 12, 12, 6, 12, 22]
values[exp.index(allGlyphs["peseta"])] = [22, 22, 22, 22, 22, 12, 12, 6, 12, 22]
values[exp.index(allGlyphs["idotless"])] = [44, 56, 14, 28, 16, 52, 28, 42, 40, 36]

#factors
factorX = [0 for g in exp]
factorY = [0 for g in exp]
incH = ["semicolon", "exclamdown"]
incW = ["N", "T", "guilsinglleft", "guilsinglright", "guillemetleft", "guillemetright", "endash", "emdash", "Tbar", "tbar", "lslash", "numero", "peseta", "idotless"]
decW = ["B", "six", "nine", "E", "S", "Z", "zero", "two", "three", "five", "F", "J", "L", "seven", "C", "c", "o", "a", "e", "s", "z", "r", "bar", "dieresiscomb.narrow", "acutecomb.narrow", "gravecomb.narrow", "dblgravecomb.narrow", "macroncomb.narrow", "tildecomb.narrow", "Mark_tilde_stacked_forHorn", "circumflexcomb.narrow", "invertedbrevecomb.narrow", "brevecomb.narrow", "hookabovecomb.narrow", "dieresisacutecomb.narrow", "horntildecomb", "Lcaron", "Ldot", "Lslash", "Germandbls", "germandbls", "schwa", "question"]
for g in exp:
	i = exp.index(g)
	if g.name in incH:
		factorY[i] = 1
	if g.name in incW:
		factorX[i] = 1
	if g.name in decW:
		factorX[i] = -1

#is flip?
flipH = ["W", "w"]
flipV = ["four", "d", "q", "gravecomb", "gravecomb.narrow", "dblgravecomb", "dblgravecomb.narrow", "macrongravecomb", "circumflexgravecomb", "brevegravecomb", "eng"]
isFlipH = [False for g in exp]
isFlipV = [False for g in exp]
for g in exp:
	i = exp.index(g)
	if g.name in flipH:
		isFlipH[i] = True
	if g.name in flipV:
		isFlipV[i] = True

#calling
bgs = ['none', 'none', 'none', 'none', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bg5', 'bgUC1', 'bgUC1_K', 'bgUC1', 'bgUC3', 'bgUC1', 'bgUC1', 'bgUC1', 'bg_Q', 'bgUC1_K', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC3', 'bgUC1', 'bgUC1', 'bgUC1', 'bgLC1', 'bgLC1ascender', 'bgLC1', 'bgLC1ascender', 'bgLC1', 'bg4', 'bg1decender', 'bgLC1ascender', 'bg5', 'bg5descender', 'bgLC1_k', 'bg5', 'bgLC3', 'bgLC1', 'bgLC1', 'bgLC1descender', 'bgLC1descender', 'bgLC1_r', 'bgLC1', 'bg4_t', 'bgLC1', 'bgLC1', 'bgLC3', 'bgLC1', 'bg1decender', 'bgLC1', 'bgUC1', 'bg5', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bg_period', 'bg_comma', 'bg_colon', 'bg_comma', 'none', 'bg6', 'bg4', 'bg7', 'bg_hyphen', 'bg_hyphen', 'bg_hyphen', 'none', 'bg7', 'bg7', 'none', 'bg7', 'bg7', 'bg7', 'none', 'none', 'bg_quote', 'bg_quote', 'none', 'bg_quote', 'bg7', 'bgUC9', 'bgUC1', 'none', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC1descender', 'bgUC1_Oslash', 'bgUC9', 'bgLC1_Thorn', 'bgUC1', 'bgUC1', 'bgLC9', 'bgUC1_bar', 'bgUC1_bar', 'bgLC1', 'bgUC1_bar', 'bg_colon', 'bg_jdotless', 'bgLC1_K', 'none', 'bg5', 'bgLC1descender', 'bgLC_oslash', 'bgLC9', 'bgLC1_thorn', 'bgUC1', 'bg4_t', 'bg_diac12a', 'bg_symbolsmall', 'bg_symbolsmall', 'none', 'none', 'bg_symbol', 'bg_symbol', 'bg7', 'bg7', 'bg_comma', 'bg4descender', 'none', 'none', 'bg_symbolsmall', 'bg_symbol', 'bg7', 'none', 'none', 'none', 'bg_colon', 'bg_colon', 'bg_colon', 'bg_colon', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_tm', 'bg_degree', 'bg_quote', 'none', 'none', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_diac3', 'bg_diac7', 'bg_diac1', 'bg_diac1', 'bg_diac6', 'bg_diac12', 'bg_diac5', 'bg_diac4', 'bg_diac4', 'bg_diac8', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6', 'bg_diac5', 'bg_diac14', 'bg_diac11', 'bg_diac7_below', 'bg_diac3_below', 'bg_diac14_below', 'bg_diac13_below', 'bg_diac13_below', 'bg_diac5_below', 'bg_diac2_below', 'bg_diac2', 'bg_diac1b_stacked', 'bg_diac1b_stacked', 'bg_diac1', 'bg_diac3', 'bg_diac1', 'bg_diac1', 'bg_diac5', 'bg_diac4', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6', 'bg_diac13_below', 'bg_diac2_below', 'bg_diac3', 'bg_diac7_stacked', 'bg_diac1a_stacked', 'bg_diac1a_stacked', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac1_stacked', 'bg_diac1_stacked', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac2_stacked', 'bg_diac11a', 'bg_diac11a', 'none', 'bg_diac11b', 'bg_diac3_stacked', 'bg_diac1a_stacked', 'bg_diac1_stacked', 'bg_diac3_stacked', 'bg_diac2_stacked', 'bg_diac1_stacked', 'bg_diac5']

for thisGlyph in exp:
	ind = exp.index(thisGlyph)
	if bgs[ind]=="none":
		pass
	else:
		addBg(thisGlyph.name, bgs[ind], values[ind], factorX[ind], factorY[ind], isFlipH[ind], isFlipV[ind])
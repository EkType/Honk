#MenuTitle: Honk - Add Backgrounds
__doc__="""
Adds BG components to all glyphs and modifies the components as needed
"""

from AppKit import NSPoint

allGlyphs = Glyphs.font.glyphs
exporting = [g for g in allGlyphs if g.export]

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
values[exporting.index(allGlyphs["macronbelowcomb.narrow"])] = [0, 12, 40, 7, 0, 0, 0, 0, 0, 12]
values[exporting.index(allGlyphs["tildecomb.narrow"])] = [20, 18, 50, 17, 20, 18, 20, 20, 25, 20]
values[exporting.index(allGlyphs["circumflexcomb.narrow"])] = [28, 23, 50, 16, 28, 20, 20, 18, 26, 38]
values[exporting.index(allGlyphs["invertedbrevecomb.narrow"])] = [20, 22, 50, 18, 14, 18, 18, 18, 26, 28]
values[exporting.index(allGlyphs["brevecomb.narrow"])] = [20, 22, 52, 18, 20, 22, 22, 20, 24, 30]
values[exporting.index(allGlyphs["dieresisacutecomb.narrow"])] = [22, 20, 50, 16, 20, 16, 20, 20, 20, 26]
values[exporting.index(allGlyphs["lslash"])] = [35, 30, 55, 30, 54, 34, 32, 32, 30, 22]
values[exporting.index(allGlyphs["question"])] = [0, 0, 27, 0, 0, 0, 0, 0, 0, 0]

#factors
factorX = [0 for g in exporting]
factorY = [0 for g in exporting]
incW = ["endash", "emdash", "lslash"]
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

#calling
bgs = ['none', 'none', 'none', 'none', 'bgUC1', 'bgUC1a', 'bgUC2b', 'bgUC1', 'bgUC2', 'bgUC2', 'bgUC1', 'bgUC1', 'bg5', 'bgUC2a', 'bgUC1_K', 'bgUC2a', 'bgUC3', 'bgUC1b', 'bgUC1', 'bgUC1', 'bg_Q', 'bgUC1_K', 'bgUC2', 'bgUC1b', 'bgUC1', 'bgUC1', 'bgUC3a', 'bgUC1', 'bgUC1', 'bgUC2', 'bgLC2', 'bgLC1ascender', 'bgLC2b', 'bgLC1ascender_d', 'bgLC2', 'bg4', 'bg1decender', 'bgLC1ascender', 'bg5', 'bg5descender', 'bgLC1_k', 'bg5', 'bgLC3', 'bgLC1', 'bgLC1a', 'bgLC1descender', 'bgLC1descender', 'bgLC1_r', 'bgLC2', 'bg4_t', 'bgLC1', 'bgLC1', 'bgLC3a', 'bgLC1', 'bg1decender', 'bgLC2', 'bgUC2', 'bg5', 'bgUC2', 'bgUC2', 'bgUC1', 'bgUC2', 'bgUC1a', 'bgUC2a', 'bgUC1', 'bgUC1a', 'bg_period', 'bg_comma', 'bg_colon', 'bg_semicolon', 'bg6', 'bg4', 'bg7', 'bg_hyphen', 'bg_hyphen', 'bg_hyphen', 'none', 'bg7', 'bg7', 'bg7', 'bg7', 'bg7', 'bg7', 'bg_quote', 'bg_quote', 'bg_quote', 'bg7', 'bgUC9', 'bgUC1', 'bgUC1', 'bgUC1', 'bgUC2a', 'bgUC2a', 'bgUC2a', 'bgUC1descender', 'bgUC1', 'bgUC9', 'bgLC1_Thorn', 'bgUC1a', 'bgUC1b', 'bgLC9', 'bgUC1_bar', 'bgUC1_bar', 'bgLC2', 'bgUC1_bar', 'bg_idotless', 'bg_jdotless', 'bgLC1_K', 'bg5', 'bgLC1descender', 'bgLC1a', 'bgLC9', 'bgLC1_thorn', 'bgUC1a', 'bg4_t', 'bg_diac12a', 'bg_symbolsmall', 'bg_symbolsmall', 'bg_symbol', 'bg_symbol', 'bg7', 'bg7', 'bg_semicolon', 'bg4descender', 'none', 'bg_symbolsmall2', 'bg_symbolsmall', 'bg_symbol', 'bg7', 'bg_guillemet', 'bg_guillemet', 'bg_guilsingle', 'bg_guilsingle', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_tm', 'bg_degree', 'bg_quote', 'none', 'bg_symbol', 'bg_symbol', 'bg_symbolwide', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbolwide', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_symbol', 'bg_diac3', 'bg_diac7', 'bg_diac1_flipped', 'bg_diac1', 'bg_diac6', 'bg_diac12', 'bg_diac5', 'bg_diac4', 'bg_diac4', 'bg_diac8', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6_flipped', 'bg_diac5', 'bg_diac14', 'bg_diac11', 'bg_diac7_below', 'bg_diac3_below', 'bg_diac14_below', 'bg_diac13_below', 'bg_diac13_below', 'bg_diac5_below', 'bg_diac2_below', 'bg_diac2', 'bg_diac1b_stacked', 'bg_diac1b_stacked_flipped', 'bg_diac1', 'bg_diac3n', 'bg_diac1n_flipped', 'bg_diac1n', 'bg_diac5', 'bg_diac4', 'bg_diac9', 'bg_diac2', 'bg_diac10', 'bg_diac6', 'bg_diac13_below', 'bg_diac2_below', 'bg_diac3', 'bg_diac7_stacked', 'bg_diac1a_stacked', 'bg_diac1a_stacked_flipped', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac1_stacked', 'bg_diac1_stacked_flipped', 'bg_diac10_stacked', 'bg_diac9_stacked', 'none', 'bg_diac2_stacked', 'bg_diac11a', 'bg_diac11a', 'none', 'bg_diac11b', 'bg_diac3_stacked', 'bg_diac1a_stacked', 'bg_diac1_stacked', 'bg_diac3_stacked', 'bg_diac2_stacked', 'bg_diac1_stacked', 'bg_diac5', 'bg_diac2_below', 'bg_diac5', 'bg_flag5', 'bg_flag3', 'bg_flag5', 'bg_flag3', 'bg_flag12', 'bg_flag5', 'bg_flag12', 'bg_flag10', 'bg_flag4', 'bg_flag6', 'bg_flag8', 'bg_flag7', 'bg_flag9', 'bg_flag4', 'bg_flag1', 'bg_flag8', 'bg_flag11', 'bg_flag5', 'bg_flag2', 'bg_flag3', 'bg_flag7', 'bg_flag3', 'bg_flag6', 'bg_flag10', 'bg_flag10', 'bg_flag4', 'bg_flag3', 'bg_flag2', 'bg_flag7', 'bg_flag11', 'bg_flag7', 'bg_okHand', 'bg_thumbsUpSign', 'none', 'bg_handWithFingersSplayed', 'bg_middleFinger', 'bg_foldedHands', 'bg_signOfTheHorns', 'bg_crossedFingers', 'bg_iLoveYouHandSign', 'none', 'none', 'bg_indexPointingRight', 'none', 'bg_raisedfist', 'bg_victoryHand', 'bg_u1FAF0', 'bg_eye', 'bg_symbol', 'bg_skull', 'bg_crossbones']

for thisGlyph in exporting:
	ind = exporting.index(thisGlyph)
	if bgs[ind]=="none":
		pass
	else:
		addBg(thisGlyph.name, bgs[ind], values[ind], factorX[ind], factorY[ind], isFlipV[ind])
#MenuTitle: Honk - Generate BG Array
__doc__="""
Prints array that contains corresponding bgGlyph name for each exporting glyph
"""

allGlyphs = Glyphs.font.glyphs

def usedAsComp(bgArr):
	bgs = ["none" for g in allGlyphs if g.export]
	for each in bgArr:
		i = 0
		for thisGlyph in allGlyphs:
			if thisGlyph.export:
				myComps = thisGlyph.layers[0].components
				if len(myComps)>0:
					for c in myComps:
						if c.componentName==each.name:
							bgs[i] = each.name
							break
				i += 1
	return bgs

bgGlyphs = [] #array of all the bg glyphs
for eachGlyph in allGlyphs:
	nameArr = list(eachGlyph.name)
	if len(nameArr)>=2:
		if nameArr[0]=='b' and nameArr[1]=='g':
			bgGlyphs.append(eachGlyph)

bgs = usedAsComp(bgGlyphs)
print(bgs)
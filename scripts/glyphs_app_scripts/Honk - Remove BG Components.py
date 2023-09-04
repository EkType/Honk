#MenuTitle: Honk - Remove BG Components
__doc__="""
Removes BG components from all exporting glyphs in the file
"""

allGlyphs = Glyphs.font.glyphs
exp = [g for g in allGlyphs if g.export]

def removeComponentFromGlyph(compname, thisGlyph):
	for thisLayer in thisGlyph.layers:
		theseComponents = thisLayer.components
		numberOfComponents = len(theseComponents)
		if numberOfComponents > 0:
			for i in range(numberOfComponents)[::-1]:
				thisComponent = theseComponents[i]
				if compname==thisComponent.componentName:
					index = thisLayer.shapes.index(thisComponent)
					del (thisLayer.shapes[index])
					
def removeComponentsFromAllGlyphs(bgGlyphs):
	for each in bgGlyphs:
		for thisGlyph in exp:
			removeComponentFromGlyph(each.name, thisGlyph)

bgGlyphs = [] #array of all the bg glyphs
for eachGlyph in allGlyphs:
	nameArr = list(eachGlyph.name)
	if len(nameArr)>=2:
		if nameArr[0]=='b' and nameArr[1]=='g':
			bgGlyphs.append(eachGlyph)

removeComponentsFromAllGlyphs(bgGlyphs)
#MenuTitle: Swap With Background in all masters
__doc__="""
Swaps the selected glyphs with the background layer in all masters/layers
"""

myLayers = Glyphs.font.selectedLayers
for thisLayer in myLayers:
	thisGlyph = thisLayer.parent
	for eachLayer in thisGlyph.layers:
		eachLayer.swapForegroundWithBackground()
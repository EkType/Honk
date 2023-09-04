#MenuTitle: Honk - Centre Align Symbols
__doc__="""
Aligns all symbol glyphs to the centre, horizontally and vertically
"""

symbols = ["mu", "pi", "numbersign", "florin", "baht", "at", "ampersand", "paragraph", "section", "copyright", "registered", "dagger", "daggerdbl", "cedi", "cent", "colonsign", "currency", "dollar", "dong", "euro", "franc", "guarani", "lira", "liraTurkish", "manat", "naira", "peso", "ruble", "rupeeIndian", "sterling", "uni20AA", "won", "yen", "commercialMinusSign", "divisionslash", "plus", "minus", "multiply", "divide", "equal", "notequal", "greater", "less", "greaterequal", "lessequal", "plusminus", "approxequal", "asciitilde", "logicalnot", "asciicircum", "infinity", "emptyset", "integral", "Ohm", "increment", "product", "summation", "radical", "percent", "perthousand", "upArrow", "northEastArrow", "rightArrow", "southEastArrow", "downArrow", "southWestArrow", "leftArrow", "northWestArrow", "lozenge", "heart"]
test = ["percent"]
myGlyphs = Glyphs.font.glyphs
for g in myGlyphs:
	if g.name in symbols:
		for layer in g.layers:
			wc = layer.width/2
			hc = [570, 570, 587, 574, 586, 586, 540, 586, 606, 595]
			#hc = myGlyphs["symbol"].layers[g.layers.index(layer)].paths[0].bounds.size.height/2
			lpx = 10000
			hpx = -10000
			lpy = 10000
			hpy = -10000
			for path in layer.paths:
				if len(layer.paths)<=1:
					lpx = path.bounds.origin.x
					hpx = path.bounds.origin.x + path.bounds.size.width
					lpy = path.bounds.origin.y
					hpy = path.bounds.origin.y + path.bounds.size.height
				else:
					if path.bounds.origin.x<=lpx:
						lpx = path.bounds.origin.x
					if (path.bounds.origin.x + path.bounds.size.width)>=hpx:
						hpx = path.bounds.origin.x + path.bounds.size.width
					if path.bounds.origin.y<=lpy:
						lpy = path.bounds.origin.y
					if (path.bounds.origin.y + path.bounds.size.height)>=hpy:
						hpy = path.bounds.origin.y + path.bounds.size.height
			pathCenterH = (lpx+hpx)/2
			pathCenterV = (lpy+hpy)/2
			shiftX = wc - pathCenterH
			shiftY = hc[g.layers.index(layer)] - pathCenterV
			#shiftY = hc - pathCenterV
			for path in layer.paths:
				for node in path.nodes:
					node.x += shiftX
					node.y += shiftY
	
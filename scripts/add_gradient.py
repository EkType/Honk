from fontTools.ttLib import getTableModule
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables as ot
from fontTools.colorLib import builder

import os
import pprint
import sys

def color(hex: str):
    return getTableModule("CPAL").Color.fromHex(hex)

def buildLinearGradient(pt0, pt1, pt2, colorLine, extend="pad"):
    return {
        "Format": ot.PaintFormat.PaintLinearGradient,
        "ColorLine": {
            "ColorStop": colorLine,
            "Extend": extend,  
        },
        "x0": pt0[0],
        "y0": pt0[1],
        "x1": pt1[0],
        "y1": pt1[1],
        "x2": pt2[0],
        "y2": pt2[1],
    }

def buildSolid(colorIndex):
    return {
        "Format": ot.PaintFormat.PaintSolid,
        "PaletteIndex": colorIndex,
        "Alpha": 1.0,
    }
    

assert len(sys.argv) == 2, "Filename is required"

font = TTFont(sys.argv[1])

colr0 = font["COLR"]
assert colr0.version == 0, "COLR table version must be 0"


cpal = font["CPAL"]
assert cpal.palettes == [
    [color("#000000FF"), color("#000000FF"), color("#FFFFFFFF"), color("#FFF33BFF"), color("#FDAA0CFF"), color("#F3705BFF"), color("#E9579EFF"), color("#FF45FFFF")], 
    [color("#000040FF"), color("#605FA0FF"), color("#FFFFFFFF"), color("#FFFFFFFF"), color("#F6CBDBFF"), color("#F6CBDBFF"), color("#605FA0FF"), color("#605FA0FF")], 
    [color("#000040FF"), color("#000000FF"), color("#EE1E2CFF"), color("#FF7F00FF"), color("#FFCA00FF"), color("#37DB52FF"), color("#00A7DDFF"), color("#AD60E0FF")], 
    [color("#FFFFFFFF"), color("#FFFFFFFF"), color("#202C88FF"), color("#2B4AB5FF"), color("#1C75BCFF"), color("#279DE1FF"), color("#00A7C5FF"), color("#00A79DFF")], 
    [color("#000000FF"), color("#000000FF"), color("#CCCCCCFF"), color("#CCCCCCFF"), color("#666666FF"), color("#333333FF"), color("#666666FF"), color("#CCCCCCFF")], 
    [color("#000080FF"), color("#2B97E0FF"), color("#FF7733FF"), color("#FF7733FF"), color("#FFFFFFFF"), color("#FFFFFFFF"), color("#339966FF"), color("#339966FF")],
    [color("#FFFFFFFF"), color("#FFFFFFFF"), color("#CCCCCC00"), color("#CCCCCC00"), color("#CCCCCC66"), color("#CCCCCC99"), color("#CCCCCCFF"), color("#CCCCCCFF")]
], "Colour Palettes do not match, check the font"


bg2 = 0
bg1 = 1
c1 = 2
c2 = 3
c3 = 4
c4 = 5
c5 = 6
c6 = 7

cpal.numPaletteEntries = len(cpal.palettes[0])

colrv1_map = {}

for glyph_name, layers in colr0.ColorLayers.items():

    v1_layers = []
    colrv1_map[glyph_name] = (ot.PaintFormat.PaintColrLayers, v1_layers)

    for layer in layers:
        if layer.colorID > 0:
            fill = buildLinearGradient((0, 0), (0, 1000), (200, 0), [(0.0, c6), (0.2, c5), (0.4,c4), (0.6,c3), (0.8, c2), (1.0, c1)], "pad")
        else:
            fill = buildLinearGradient((0, 0), (0, 1000), (200, 0), [(0.0, bg2), (1.0, bg1)], "pad")
            #fill = buildSolid(0)

        v1_layers.append({
            "Format": ot.PaintFormat.PaintGlyph,
            "Paint": fill,
            "Glyph": layer.name,
        })

    if len(v1_layers) == 1:
        colrv1_map[glyph_name] = v1_layers[0]
    else:
        colrv1_map[glyph_name] = (ot.PaintFormat.PaintColrLayers, v1_layers)

pprint.PrettyPrinter(indent=2).pprint(colrv1_map)

colr = builder.buildCOLR(colrv1_map)

font["COLR"] = colr

out_file = "Honk[SHDW,STYL].ttf"
font.save(out_file)

print(f"Wrote {out_file}")
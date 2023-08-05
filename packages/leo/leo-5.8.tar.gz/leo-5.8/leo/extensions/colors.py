#@+leo-ver=4-thin
#@+node:bob.20071231111744:@thin colors.py
#@@language python
#@@tabwidth -4


#@<< docstring >>
#@+node:bob.20071231115213:<< docstring >>
""" Colors module provides a colors names database and functions to access it.

The database is a python dictionary with reduced colornames as keys and
color data in the form '#RRGGBB' as values.

The reudced color names are common color names with spaces and capitalization removed.

Functions to access the data base are:

    getColor(name, default=None)
    ----------------------------
    This function will convert `name` and return it in '#RRGGBB' format
    if possible otherwise it will do the sme for `default`.

    If default can not be converted, None will be returned.

    `name` and `default` are reduced by removing spaces and capitalization
    before looking them up in the database.


    getColorRGB(name, default=None)
    -------------------------------
    This function will first call getColor to convert `name` (or `default`)
    to '#RRGGBB' format, then it will convert this and return it as a python
    tuple in the form  (0-255, 0-255, 0-255).

    Returns None if anything goes wrong.

"""



#@-node:bob.20071231115213:<< docstring >>
#@nl

import re

__revision__ = re.sub(r'^\D+([\d\.]+)\D+$', r'\1', "$Revision: 1.1 $")

__version__ = '%s'% __revision__

#@<< version history >>
#@+node:bob.20071231115213.1:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 plumloco: initial version
# 0.2 plumloco:
# - leofied file adding docstring and verison info
# - fixed getColor to return #... strings unmodified
# - fixed getColor to convert default color if it is returned.
#@-at
#@-node:bob.20071231115213.1:<< version history >>
#@nl

#@+others
#@+node:bob.20071231111744.1:colors declarations
colors = {

    # leo colors
    "leoblue": "#F0F8FF", #alice blue
    "leoyellow": "#ffffec",
    "leopink":  "#FFE4E1", # misty rose

    "aliceblue": "#F0F8FF",
    "antiquewhite": "#FAEBD7",
    "antiquewhite1": "#FFEFDB",
    "antiquewhite2": "#EEDFCC",
    "antiquewhite3": "#CDC0B0",
    "antiquewhite4": "#8B8378",
    "aquamarine": "#7FFFD4",
    "aquamarine1": "#7FFFD4",
    "aquamarine2": "#76EEC6",
    "aquamarine3": "#66CDAA",
    "aquamarine4": "#458B74",
    "azure": "#F0FFFF",
    "azure1": "#F0FFFF",
    "azure2": "#E0EEEE",
    "azure3": "#C1CDCD",
    "azure4": "#838B8B",
    "beige": "#F5F5DC",
    "bisque": "#FFE4C4",
    "bisque1": "#FFE4C4",
    "bisque2": "#EED5B7",
    "bisque3": "#CDB79E",
    "bisque4": "#8B7D6B",
    "black": "#000000",
    "blanchedalmond": "#FFEBCD",
    "blue": "#0000FF",
    "blue1": "#0000FF",
    "blue2": "#0000EE",
    "blue3": "#0000CD",
    "blue4": "#00008B",
    "blueviolet": "#8A2BE2",
    "brown": "#A52A2A",
    "brown1": "#FF4040",
    "brown2": "#EE3B3B",
    "brown3": "#CD3333",
    "brown4": "#8B2323",
    "burlywood": "#DEB887",
    "burlywood1": "#FFD39B",
    "burlywood2": "#EEC591",
    "burlywood3": "#CDAA7D",
    "burlywood4": "#8B7355",
    "cadetblue": "#5F9EA0",
    "cadetblue1": "#98F5FF",
    "cadetblue2": "#8EE5EE",
    "cadetblue3": "#7AC5CD",
    "cadetblue4": "#53868B",
    "chartreuse": "#7FFF00",
    "chartreuse1": "#7FFF00",
    "chartreuse2": "#76EE00",
    "chartreuse3": "#66CD00",
    "chartreuse4": "#458B00",
    "chocolate": "#D2691E",
    "chocolate1": "#FF7F24",
    "chocolate2": "#EE7621",
    "chocolate3": "#CD661D",
    "chocolate4": "#8B4513",
    "coral": "#FF7F50",
    "coral1": "#FF7256",
    "coral2": "#EE6A50",
    "coral3": "#CD5B45",
    "coral4": "#8B3E2F",
    "cornflowerblue": "#6495ED",
    "cornsilk": "#FFF8DC",
    "cornsilk1": "#FFF8DC",
    "cornsilk2": "#EEE8CD",
    "cornsilk3": "#CDC8B1",
    "cornsilk4": "#8B8878",
    "cyan": "#00FFFF",
    "cyan1": "#00FFFF",
    "cyan2": "#00EEEE",
    "cyan3": "#00CDCD",
    "cyan4": "#008B8B",
    "darkblue": "#00008B",
    "darkcyan": "#008B8B",
    "darkgoldenrod": "#B8860B",
    "darkgoldenrod1": "#FFB90F",
    "darkgoldenrod2": "#EEAD0E",
    "darkgoldenrod3": "#CD950C",
    "darkgoldenrod4": "#8B6508",
    "darkgray": "#A9A9A9",
    "darkgreen": "#006400",
    "darkgrey": "#A9A9A9",
    "darkkhaki": "#BDB76B",
    "darkmagenta": "#8B008B",
    "darkolivegreen": "#556B2F",
    "darkolivegreen1": "#CAFF70",
    "darkolivegreen2": "#BCEE68",
    "darkolivegreen3": "#A2CD5A",
    "darkolivegreen4": "#6E8B3D",
    "darkorange": "#FF8C00",
    "darkorange1": "#FF7F00",
    "darkorange2": "#EE7600",
    "darkorange3": "#CD6600",
    "darkorange4": "#8B4500",
    "darkorchid": "#9932CC",
    "darkorchid1": "#BF3EFF",
    "darkorchid2": "#B23AEE",
    "darkorchid3": "#9A32CD",
    "darkorchid4": "#68228B",
    "darkred": "#8B0000",
    "darksalmon": "#E9967A",
    "darkseagreen": "#8FBC8F",
    "darkseagreen1": "#C1FFC1",
    "darkseagreen2": "#B4EEB4",
    "darkseagreen3": "#9BCD9B",
    "darkseagreen4": "#698B69",
    "darkslateblue": "#483D8B",
    "darkslategray": "#2F4F4F",
    "darkslategray1": "#97FFFF",
    "darkslategray2": "#8DEEEE",
    "darkslategray3": "#79CDCD",
    "darkslategray4": "#528B8B",
    "darkslategrey": "#2F4F4F",
    "darkturquoise": "#00CED1",
    "darkviolet": "#9400D3",
    "deeppink": "#FF1493",
    "deeppink1": "#FF1493",
    "deeppink2": "#EE1289",
    "deeppink3": "#CD1076",
    "deeppink4": "#8B0A50",
    "deepskyblue": "#00BFFF",
    "deepskyblue1": "#00BFFF",
    "deepskyblue2": "#00B2EE",
    "deepskyblue3": "#009ACD",
    "deepskyblue4": "#00688B",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1E90FF",
    "dodgerblue1": "#1E90FF",
    "dodgerblue2": "#1C86EE",
    "dodgerblue3": "#1874CD",
    "dodgerblue4": "#104E8B",
    "firebrick": "#B22222",
    "firebrick1": "#FF3030",
    "firebrick2": "#EE2C2C",
    "firebrick3": "#CD2626",
    "firebrick4": "#8B1A1A",
    "floralwhite": "#FFFAF0",
    "forestgreen": "#228B22",
    "gainsboro": "#DCDCDC",
    "ghostwhite": "#F8F8FF",
    "gold": "#FFD700",
    "gold1": "#FFD700",
    "gold2": "#EEC900",
    "gold3": "#CDAD00",
    "gold4": "#8B7500",
    "goldenrod": "#DAA520",
    "goldenrod1": "#FFC125",
    "goldenrod2": "#EEB422",
    "goldenrod3": "#CD9B1D",
    "goldenrod4": "#8B6914",
    "gray": "#BEBEBE",
    "gray0": "#000000",
    "gray1": "#030303",
    "gray10": "#1A1A1A",
    "gray100": "#FFFFFF",
    "gray11": "#1C1C1C",
    "gray12": "#1F1F1F",
    "gray13": "#212121",
    "gray14": "#242424",
    "gray15": "#262626",
    "gray16": "#292929",
    "gray17": "#2B2B2B",
    "gray18": "#2E2E2E",
    "gray19": "#303030",
    "gray2": "#050505",
    "gray20": "#333333",
    "gray21": "#363636",
    "gray22": "#383838",
    "gray23": "#3B3B3B",
    "gray24": "#3D3D3D",
    "gray25": "#404040",
    "gray26": "#424242",
    "gray27": "#454545",
    "gray28": "#474747",
    "gray29": "#4A4A4A",
    "gray3": "#080808",
    "gray30": "#4D4D4D",
    "gray31": "#4F4F4F",
    "gray32": "#525252",
    "gray33": "#545454",
    "gray34": "#575757",
    "gray35": "#595959",
    "gray36": "#5C5C5C",
    "gray37": "#5E5E5E",
    "gray38": "#616161",
    "gray39": "#636363",
    "gray4": "#0A0A0A",
    "gray40": "#666666",
    "gray41": "#696969",
    "gray42": "#6B6B6B",
    "gray43": "#6E6E6E",
    "gray44": "#707070",
    "gray45": "#737373",
    "gray46": "#757575",
    "gray47": "#787878",
    "gray48": "#7A7A7A",
    "gray49": "#7D7D7D",
    "gray5": "#0D0D0D",
    "gray50": "#7F7F7F",
    "gray51": "#828282",
    "gray52": "#858585",
    "gray53": "#878787",
    "gray54": "#8A8A8A",
    "gray55": "#8C8C8C",
    "gray56": "#8F8F8F",
    "gray57": "#919191",
    "gray58": "#949494",
    "gray59": "#969696",
    "gray6": "#0F0F0F",
    "gray60": "#999999",
    "gray61": "#9C9C9C",
    "gray62": "#9E9E9E",
    "gray63": "#A1A1A1",
    "gray64": "#A3A3A3",
    "gray65": "#A6A6A6",
    "gray66": "#A8A8A8",
    "gray67": "#ABABAB",
    "gray68": "#ADADAD",
    "gray69": "#B0B0B0",
    "gray7": "#121212",
    "gray70": "#B3B3B3",
    "gray71": "#B5B5B5",
    "gray72": "#B8B8B8",
    "gray73": "#BABABA",
    "gray74": "#BDBDBD",
    "gray75": "#BFBFBF",
    "gray76": "#C2C2C2",
    "gray77": "#C4C4C4",
    "gray78": "#C7C7C7",
    "gray79": "#C9C9C9",
    "gray8": "#141414",
    "gray80": "#CCCCCC",
    "gray81": "#CFCFCF",
    "gray82": "#D1D1D1",
    "gray83": "#D4D4D4",
    "gray84": "#D6D6D6",
    "gray85": "#D9D9D9",
    "gray86": "#DBDBDB",
    "gray87": "#DEDEDE",
    "gray88": "#E0E0E0",
    "gray89": "#E3E3E3",
    "gray9": "#171717",
    "gray90": "#E5E5E5",
    "gray91": "#E8E8E8",
    "gray92": "#EBEBEB",
    "gray93": "#EDEDED",
    "gray94": "#F0F0F0",
    "gray95": "#F2F2F2",
    "gray96": "#F5F5F5",
    "gray97": "#F7F7F7",
    "gray98": "#FAFAFA",
    "gray99": "#FCFCFC",
    "green": "#00FF00",
    "green1": "#00FF00",
    "green2": "#00EE00",
    "green3": "#00CD00",
    "green4": "#008B00",
    "greenyellow": "#ADFF2F",
    "grey": "#BEBEBE",
    "grey0": "#000000",
    "grey1": "#030303",
    "grey10": "#1A1A1A",
    "grey100": "#FFFFFF",
    "grey11": "#1C1C1C",
    "grey12": "#1F1F1F",
    "grey13": "#212121",
    "grey14": "#242424",
    "grey15": "#262626",
    "grey16": "#292929",
    "grey17": "#2B2B2B",
    "grey18": "#2E2E2E",
    "grey19": "#303030",
    "grey2": "#050505",
    "grey20": "#333333",
    "grey21": "#363636",
    "grey22": "#383838",
    "grey23": "#3B3B3B",
    "grey24": "#3D3D3D",
    "grey25": "#404040",
    "grey26": "#424242",
    "grey27": "#454545",
    "grey28": "#474747",
    "grey29": "#4A4A4A",
    "grey3": "#080808",
    "grey30": "#4D4D4D",
    "grey31": "#4F4F4F",
    "grey32": "#525252",
    "grey33": "#545454",
    "grey34": "#575757",
    "grey35": "#595959",
    "grey36": "#5C5C5C",
    "grey37": "#5E5E5E",
    "grey38": "#616161",
    "grey39": "#636363",
    "grey4": "#0A0A0A",
    "grey40": "#666666",
    "grey41": "#696969",
    "grey42": "#6B6B6B",
    "grey43": "#6E6E6E",
    "grey44": "#707070",
    "grey45": "#737373",
    "grey46": "#757575",
    "grey47": "#787878",
    "grey48": "#7A7A7A",
    "grey49": "#7D7D7D",
    "grey5": "#0D0D0D",
    "grey50": "#7F7F7F",
    "grey51": "#828282",
    "grey52": "#858585",
    "grey53": "#878787",
    "grey54": "#8A8A8A",
    "grey55": "#8C8C8C",
    "grey56": "#8F8F8F",
    "grey57": "#919191",
    "grey58": "#949494",
    "grey59": "#969696",
    "grey6": "#0F0F0F",
    "grey60": "#999999",
    "grey61": "#9C9C9C",
    "grey62": "#9E9E9E",
    "grey63": "#A1A1A1",
    "grey64": "#A3A3A3",
    "grey65": "#A6A6A6",
    "grey66": "#A8A8A8",
    "grey67": "#ABABAB",
    "grey68": "#ADADAD",
    "grey69": "#B0B0B0",
    "grey7": "#121212",
    "grey70": "#B3B3B3",
    "grey71": "#B5B5B5",
    "grey72": "#B8B8B8",
    "grey73": "#BABABA",
    "grey74": "#BDBDBD",
    "grey75": "#BFBFBF",
    "grey76": "#C2C2C2",
    "grey77": "#C4C4C4",
    "grey78": "#C7C7C7",
    "grey79": "#C9C9C9",
    "grey8": "#141414",
    "grey80": "#CCCCCC",
    "grey81": "#CFCFCF",
    "grey82": "#D1D1D1",
    "grey83": "#D4D4D4",
    "grey84": "#D6D6D6",
    "grey85": "#D9D9D9",
    "grey86": "#DBDBDB",
    "grey87": "#DEDEDE",
    "grey88": "#E0E0E0",
    "grey89": "#E3E3E3",
    "grey9": "#171717",
    "grey90": "#E5E5E5",
    "grey91": "#E8E8E8",
    "grey92": "#EBEBEB",
    "grey93": "#EDEDED",
    "grey94": "#F0F0F0",
    "grey95": "#F2F2F2",
    "grey96": "#F5F5F5",
    "grey97": "#F7F7F7",
    "grey98": "#FAFAFA",
    "grey99": "#FCFCFC",
    "honeydew": "#F0FFF0",
    "honeydew1": "#F0FFF0",
    "honeydew2": "#E0EEE0",
    "honeydew3": "#C1CDC1",
    "honeydew4": "#838B83",
    "hotpink": "#FF69B4",
    "hotpink1": "#FF6EB4",
    "hotpink2": "#EE6AA7",
    "hotpink3": "#CD6090",
    "hotpink4": "#8B3A62",
    "indianred": "#CD5C5C",
    "indianred1": "#FF6A6A",
    "indianred2": "#EE6363",
    "indianred3": "#CD5555",
    "indianred4": "#8B3A3A",
    "ivory": "#FFFFF0",
    "ivory1": "#FFFFF0",
    "ivory2": "#EEEEE0",
    "ivory3": "#CDCDC1",
    "ivory4": "#8B8B83",
    "khaki": "#F0E68C",
    "khaki1": "#FFF68F",
    "khaki2": "#EEE685",
    "khaki3": "#CDC673",
    "khaki4": "#8B864E",
    "lavender": "#E6E6FA",
    "lavenderblush": "#FFF0F5",
    "lavenderblush1": "#FFF0F5",
    "lavenderblush2": "#EEE0E5",
    "lavenderblush3": "#CDC1C5",
    "lavenderblush4": "#8B8386",
    "lawngreen": "#7CFC00",
    "lemonchiffon": "#FFFACD",
    "lemonchiffon1": "#FFFACD",
    "lemonchiffon2": "#EEE9BF",
    "lemonchiffon3": "#CDC9A5",
    "lemonchiffon4": "#8B8970",
    "lightblue": "#ADD8E6",
    "lightblue1": "#BFEFFF",
    "lightblue2": "#B2DFEE",
    "lightblue3": "#9AC0CD",
    "lightblue4": "#68838B",
    "lightcoral": "#F08080",
    "lightcyan": "#E0FFFF",
    "lightcyan1": "#E0FFFF",
    "lightcyan2": "#D1EEEE",
    "lightcyan3": "#B4CDCD",
    "lightcyan4": "#7A8B8B",
    "lightgoldenrod": "#EEDD82",
    "lightgoldenrod1": "#FFEC8B",
    "lightgoldenrod2": "#EEDC82",
    "lightgoldenrod3": "#CDBE70",
    "lightgoldenrod4": "#8B814C",
    "lightgoldenrodyellow": "#FAFAD2",
    "lightgray": "#D3D3D3",
    "lightgreen": "#90EE90",
    "lightgrey": "#D3D3D3",
    "lightpink": "#FFB6C1",
    "lightpink1": "#FFAEB9",
    "lightpink2": "#EEA2AD",
    "lightpink3": "#CD8C95",
    "lightpink4": "#8B5F65",
    "lightsalmon": "#FFA07A",
    "lightsalmon1": "#FFA07A",
    "lightsalmon2": "#EE9572",
    "lightsalmon3": "#CD8162",
    "lightsalmon4": "#8B5742",
    "lightseagreen": "#20B2AA",
    "lightskyblue": "#87CEFA",
    "lightskyblue1": "#B0E2FF",
    "lightskyblue2": "#A4D3EE",
    "lightskyblue3": "#8DB6CD",
    "lightskyblue4": "#607B8B",
    "lightslateblue": "#8470FF",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#B0C4DE",
    "lightsteelblue1": "#CAE1FF",
    "lightsteelblue2": "#BCD2EE",
    "lightsteelblue3": "#A2B5CD",
    "lightsteelblue4": "#6E7B8B",
    "lightyellow": "#FFFFE0",
    "lightyellow1": "#FFFFE0",
    "lightyellow2": "#EEEED1",
    "lightyellow3": "#CDCDB4",
    "lightyellow4": "#8B8B7A",
    "limegreen": "#32CD32",
    "linen": "#FAF0E6",
    "magenta": "#FF00FF",
    "magenta1": "#FF00FF",
    "magenta2": "#EE00EE",
    "magenta3": "#CD00CD",
    "magenta4": "#8B008B",
    "maroon": "#B03060",
    "maroon1": "#FF34B3",
    "maroon2": "#EE30A7",
    "maroon3": "#CD2990",
    "maroon4": "#8B1C62",
    "mediumaquamarine": "#66CDAA",
    "mediumblue": "#0000CD",
    "mediumorchid": "#BA55D3",
    "mediumorchid1": "#E066FF",
    "mediumorchid2": "#D15FEE",
    "mediumorchid3": "#B452CD",
    "mediumorchid4": "#7A378B",
    "mediumpurple": "#9370DB",
    "mediumpurple1": "#AB82FF",
    "mediumpurple2": "#9F79EE",
    "mediumpurple3": "#8968CD",
    "mediumpurple4": "#5D478B",
    "mediumseagreen": "#3CB371",
    "mediumslateblue": "#7B68EE",
    "mediumspringgreen": "#00FA9A",
    "mediumturquoise": "#48D1CC",
    "mediumvioletred": "#C71585",
    "midnightblue": "#191970",
    "mintcream": "#F5FFFA",
    "mistyrose": "#FFE4E1",
    "mistyrose1": "#FFE4E1",
    "mistyrose2": "#EED5D2",
    "mistyrose3": "#CDB7B5",
    "mistyrose4": "#8B7D7B",
    "moccasin": "#FFE4B5",
    "navajowhite": "#FFDEAD",
    "navajowhite1": "#FFDEAD",
    "navajowhite2": "#EECFA1",
    "navajowhite3": "#CDB38B",
    "navajowhite4": "#8B795E",
    "navy": "#000080",
    "navyblue": "#000080",
    "oldlace": "#FDF5E6",
    "olivedrab": "#6B8E23",
    "olivedrab1": "#C0FF3E",
    "olivedrab2": "#B3EE3A",
    "olivedrab3": "#9ACD32",
    "olivedrab4": "#698B22",
    "orange": "#FFA500",
    "orange1": "#FFA500",
    "orange2": "#EE9A00",
    "orange3": "#CD8500",
    "orange4": "#8B5A00",
    "orangered": "#FF4500",
    "orangered1": "#FF4500",
    "orangered2": "#EE4000",
    "orangered3": "#CD3700",
    "orangered4": "#8B2500",
    "orchid": "#DA70D6",
    "orchid1": "#FF83FA",
    "orchid2": "#EE7AE9",
    "orchid3": "#CD69C9",
    "orchid4": "#8B4789",
    "palegoldenrod": "#EEE8AA",
    "palegreen": "#98FB98",
    "palegreen1": "#9AFF9A",
    "palegreen2": "#90EE90",
    "palegreen3": "#7CCD7C",
    "palegreen4": "#548B54",
    "paleturquoise": "#AFEEEE",
    "paleturquoise1": "#BBFFFF",
    "paleturquoise2": "#AEEEEE",
    "paleturquoise3": "#96CDCD",
    "paleturquoise4": "#668B8B",
    "palevioletred": "#DB7093",
    "palevioletred1": "#FF82AB",
    "palevioletred2": "#EE799F",
    "palevioletred3": "#CD6889",
    "palevioletred4": "#8B475D",
    "papayawhip": "#FFEFD5",
    "peachpuff": "#FFDAB9",
    "peachpuff1": "#FFDAB9",
    "peachpuff2": "#EECBAD",
    "peachpuff3": "#CDAF95",
    "peachpuff4": "#8B7765",
    "peru": "#CD853F",
    "pink": "#FFC0CB",
    "pink1": "#FFB5C5",
    "pink2": "#EEA9B8",
    "pink3": "#CD919E",
    "pink4": "#8B636C",
    "plum": "#DDA0DD",
    "plum1": "#FFBBFF",
    "plum2": "#EEAEEE",
    "plum3": "#CD96CD",
    "plum4": "#8B668B",
    "powderblue": "#B0E0E6",
    "purple": "#A020F0",
    "purple1": "#9B30FF",
    "purple2": "#912CEE",
    "purple3": "#7D26CD",
    "purple4": "#551A8B",
    "red": "#FF0000",
    "red1": "#FF0000",
    "red2": "#EE0000",
    "red3": "#CD0000",
    "red4": "#8B0000",
    "rosybrown": "#BC8F8F",
    "rosybrown1": "#FFC1C1",
    "rosybrown2": "#EEB4B4",
    "rosybrown3": "#CD9B9B",
    "rosybrown4": "#8B6969",
    "royalblue": "#4169E1",
    "royalblue1": "#4876FF",
    "royalblue2": "#436EEE",
    "royalblue3": "#3A5FCD",
    "royalblue4": "#27408B",
    "saddlebrown": "#8B4513",
    "salmon": "#FA8072",
    "salmon1": "#FF8C69",
    "salmon2": "#EE8262",
    "salmon3": "#CD7054",
    "salmon4": "#8B4C39",
    "sandybrown": "#F4A460",
    "seagreen": "#2E8B57",
    "seagreen1": "#54FF9F",
    "seagreen2": "#4EEE94",
    "seagreen3": "#43CD80",
    "seagreen4": "#2E8B57",
    "seashell": "#FFF5EE",
    "seashell1": "#FFF5EE",
    "seashell2": "#EEE5DE",
    "seashell3": "#CDC5BF",
    "seashell4": "#8B8682",
    "sienna": "#A0522D",
    "sienna1": "#FF8247",
    "sienna2": "#EE7942",
    "sienna3": "#CD6839",
    "sienna4": "#8B4726",
    "skyblue": "#87CEEB",
    "skyblue1": "#87CEFF",
    "skyblue2": "#7EC0EE",
    "skyblue3": "#6CA6CD",
    "skyblue4": "#4A708B",
    "slateblue": "#6A5ACD",
    "slateblue1": "#836FFF",
    "slateblue2": "#7A67EE",
    "slateblue3": "#6959CD",
    "slateblue4": "#473C8B",
    "slategray": "#708090",
    "slategray1": "#C6E2FF",
    "slategray2": "#B9D3EE",
    "slategray3": "#9FB6CD",
    "slategray4": "#6C7B8B",
    "slategrey": "#708090",
    "snow": "#FFFAFA",
    "snow1": "#FFFAFA",
    "snow2": "#EEE9E9",
    "snow3": "#CDC9C9",
    "snow4": "#8B8989",
    "springgreen": "#00FF7F",
    "springgreen1": "#00FF7F",
    "springgreen2": "#00EE76",
    "springgreen3": "#00CD66",
    "springgreen4": "#008B45",
    "steelblue": "#4682B4",
    "steelblue1": "#63B8FF",
    "steelblue2": "#5CACEE",
    "steelblue3": "#4F94CD",
    "steelblue4": "#36648B",
    "tan": "#D2B48C",
    "tan1": "#FFA54F",
    "tan2": "#EE9A49",
    "tan3": "#CD853F",
    "tan4": "#8B5A2B",
    "thistle": "#D8BFD8",
    "thistle1": "#FFE1FF",
    "thistle2": "#EED2EE",
    "thistle3": "#CDB5CD",
    "thistle4": "#8B7B8B",
    "tomato": "#FF6347",
    "tomato1": "#FF6347",
    "tomato2": "#EE5C42",
    "tomato3": "#CD4F39",
    "tomato4": "#8B3626",
    "turquoise": "#40E0D0",
    "turquoise1": "#00F5FF",
    "turquoise2": "#00E5EE",
    "turquoise3": "#00C5CD",
    "turquoise4": "#00868B",
    "violet": "#EE82EE",
    "violetred": "#D02090",
    "violetred1": "#FF3E96",
    "violetred2": "#EE3A8C",
    "violetred3": "#CD3278",
    "violetred4": "#8B2252",
    "wheat": "#F5DEB3",
    "wheat1": "#FFE7BA",
    "wheat2": "#EED8AE",
    "wheat3": "#CDBA96",
    "wheat4": "#8B7E66",
    "white": "#FFFFFF",
    "whitesmoke": "#F5F5F5",
    "yellow": "#FFFF00",
    "yellow1": "#FFFF00",
    "yellow2": "#EEEE00",
    "yellow3": "#CDCD00",
    "yellow4": "#8B8B00",
    "yellowgreen": "#9ACD32"
}

#@-node:bob.20071231111744.1:colors declarations
#@+node:bob.20071231111744.2:getColor
def getColor(name, default=None):

    #print 'getColor', name, default

    if name[0] == '#':
        return name

    name = name.replace(' ', '').lower()

    if name in colors:
        return colors[name]

    if default:
        return getColor(default, default=None)

    return None


#@-node:bob.20071231111744.2:getColor
#@+node:bob.20071231111744.3:getColorRGB
def getColorRGB(name, default=None):

    s = getColor(name, default)

    try:
        color = int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
    except:
        color = None

    return color
#@-node:bob.20071231111744.3:getColorRGB
#@-others
#@nonl
#@-node:bob.20071231111744:@thin colors.py
#@-leo

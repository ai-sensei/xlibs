"""
Vi Digraphs.
This is a list of special characters that can be inserted in Vi insert mode by
pressing Control-K followed by to normal characters.

Taken from Neovim and translated to Python:
https://raw.githubusercontent.com/neovim/neovim/master/src/nvim/digraph.c
"""
from typing import Dict, Tuple

__all__ = [
    "DIGRAPHS",
]

# digraphs for Unicode from RFC1345
# (also work for ISO-8859-1 aka latin1)
DIGRAPHS: Dict[Tuple[str, str], int] = {
    ("N", "U"): 0x00,
    ("S", "H"): 0x01,
    ("S", "X"): 0x02,
    ("E", "X"): 0x03,
    ("E", "T"): 0x04,
    ("E", "Q"): 0x05,
    ("A", "K"): 0x06,
    ("B", "L"): 0x07,
    ("B", "S"): 0x08,
    ("H", "T"): 0x09,
    ("L", "F"): 0x0A,
    ("V", "T"): 0x0B,
    ("F", "F"): 0x0C,
    ("C", "R"): 0x0D,
    ("S", "O"): 0x0E,
    ("S", "I"): 0x0F,
    ("D", "L"): 0x10,
    ("D", "1"): 0x11,
    ("D", "2"): 0x12,
    ("D", "3"): 0x13,
    ("D", "4"): 0x14,
    ("N", "K"): 0x15,
    ("S", "Y"): 0x16,
    ("E", "B"): 0x17,
    ("C", "N"): 0x18,
    ("E", "M"): 0x19,
    ("S", "B"): 0x1A,
    ("E", "C"): 0x1B,
    ("F", "S"): 0x1C,
    ("G", "S"): 0x1D,
    ("R", "S"): 0x1E,
    ("U", "S"): 0x1F,
    ("S", "P"): 0x20,
    ("N", "b"): 0x23,
    ("D", "O"): 0x24,
    ("A", "t"): 0x40,
    ("<", "("): 0x5B,
    ("/", "/"): 0x5C,
    (")", ">"): 0x5D,
    ("'", ">"): 0x5E,
    ("'", "!"): 0x60,
    ("(", "!"): 0x7B,
    ("!", "!"): 0x7C,
    ("!", ")"): 0x7D,
    ("'", "?"): 0x7E,
    ("D", "T"): 0x7F,
    ("P", "A"): 0x80,
    ("H", "O"): 0x81,
    ("B", "H"): 0x82,
    ("N", "H"): 0x83,
    ("I", "N"): 0x84,
    ("N", "L"): 0x85,
    ("S", "A"): 0x86,
    ("E", "S"): 0x87,
    ("H", "S"): 0x88,
    ("H", "J"): 0x89,
    ("V", "S"): 0x8A,
    ("P", "D"): 0x8B,
    ("P", "U"): 0x8C,
    ("R", "I"): 0x8D,
    ("S", "2"): 0x8E,
    ("S", "3"): 0x8F,
    ("D", "C"): 0x90,
    ("P", "1"): 0x91,
    ("P", "2"): 0x92,
    ("T", "S"): 0x93,
    ("C", "C"): 0x94,
    ("M", "W"): 0x95,
    ("S", "G"): 0x96,
    ("E", "G"): 0x97,
    ("S", "S"): 0x98,
    ("G", "C"): 0x99,
    ("S", "C"): 0x9A,
    ("C", "I"): 0x9B,
    ("S", "T"): 0x9C,
    ("O", "C"): 0x9D,
    ("P", "M"): 0x9E,
    ("A", "C"): 0x9F,
    ("N", "S"): 0xA0,
    ("!", "I"): 0xA1,
    ("C", "t"): 0xA2,
    ("P", "d"): 0xA3,
    ("C", "u"): 0xA4,
    ("Y", "e"): 0xA5,
    ("B", "B"): 0xA6,
    ("S", "E"): 0xA7,
    ("'", ":"): 0xA8,
    ("C", "o"): 0xA9,
    ("-", "a"): 0xAA,
    ("<", "<"): 0xAB,
    ("N", "O"): 0xAC,
    ("-", "-"): 0xAD,
    ("R", "g"): 0xAE,
    ("'", "m"): 0xAF,
    ("D", "G"): 0xB0,
    ("+", "-"): 0xB1,
    ("2", "S"): 0xB2,
    ("3", "S"): 0xB3,
    ("'", "'"): 0xB4,
    ("M", "y"): 0xB5,
    ("P", "I"): 0xB6,
    (".", "M"): 0xB7,
    ("'", ","): 0xB8,
    ("1", "S"): 0xB9,
    ("-", "o"): 0xBA,
    (">", ">"): 0xBB,
    ("1", "4"): 0xBC,
    ("1", "2"): 0xBD,
    ("3", "4"): 0xBE,
    ("?", "I"): 0xBF,
    ("A", "!"): 0xC0,
    ("A", "'"): 0xC1,
    ("A", ">"): 0xC2,
    ("A", "?"): 0xC3,
    ("A", ":"): 0xC4,
    ("A", "A"): 0xC5,
    ("A", "E"): 0xC6,
    ("C", ","): 0xC7,
    ("E", "!"): 0xC8,
    ("E", "'"): 0xC9,
    ("E", ">"): 0xCA,
    ("E", ":"): 0xCB,
    ("I", "!"): 0xCC,
    ("I", "'"): 0xCD,
    ("I", ">"): 0xCE,
    ("I", ":"): 0xCF,
    ("D", "-"): 0xD0,
    ("N", "?"): 0xD1,
    ("O", "!"): 0xD2,
    ("O", "'"): 0xD3,
    ("O", ">"): 0xD4,
    ("O", "?"): 0xD5,
    ("O", ":"): 0xD6,
    ("*", "X"): 0xD7,
    ("O", "/"): 0xD8,
    ("U", "!"): 0xD9,
    ("U", "'"): 0xDA,
    ("U", ">"): 0xDB,
    ("U", ":"): 0xDC,
    ("Y", "'"): 0xDD,
    ("T", "H"): 0xDE,
    ("s", "s"): 0xDF,
    ("a", "!"): 0xE0,
    ("a", "'"): 0xE1,
    ("a", ">"): 0xE2,
    ("a", "?"): 0xE3,
    ("a", ":"): 0xE4,
    ("a", "a"): 0xE5,
    ("a", "e"): 0xE6,
    ("c", ","): 0xE7,
    ("e", "!"): 0xE8,
    ("e", "'"): 0xE9,
    ("e", ">"): 0xEA,
    ("e", ":"): 0xEB,
    ("i", "!"): 0xEC,
    ("i", "'"): 0xED,
    ("i", ">"): 0xEE,
    ("i", ":"): 0xEF,
    ("d", "-"): 0xF0,
    ("n", "?"): 0xF1,
    ("o", "!"): 0xF2,
    ("o", "'"): 0xF3,
    ("o", ">"): 0xF4,
    ("o", "?"): 0xF5,
    ("o", ":"): 0xF6,
    ("-", ":"): 0xF7,
    ("o", "/"): 0xF8,
    ("u", "!"): 0xF9,
    ("u", "'"): 0xFA,
    ("u", ">"): 0xFB,
    ("u", ":"): 0xFC,
    ("y", "'"): 0xFD,
    ("t", "h"): 0xFE,
    ("y", ":"): 0xFF,
    ("A", "-"): 0x0100,
    ("a", "-"): 0x0101,
    ("A", "("): 0x0102,
    ("a", "("): 0x0103,
    ("A", ";"): 0x0104,
    ("a", ";"): 0x0105,
    ("C", "'"): 0x0106,
    ("c", "'"): 0x0107,
    ("C", ">"): 0x0108,
    ("c", ">"): 0x0109,
    ("C", "."): 0x010A,
    ("c", "."): 0x010B,
    ("C", "<"): 0x010C,
    ("c", "<"): 0x010D,
    ("D", "<"): 0x010E,
    ("d", "<"): 0x010F,
    ("D", "/"): 0x0110,
    ("d", "/"): 0x0111,
    ("E", "-"): 0x0112,
    ("e", "-"): 0x0113,
    ("E", "("): 0x0114,
    ("e", "("): 0x0115,
    ("E", "."): 0x0116,
    ("e", "."): 0x0117,
    ("E", ";"): 0x0118,
    ("e", ";"): 0x0119,
    ("E", "<"): 0x011A,
    ("e", "<"): 0x011B,
    ("G", ">"): 0x011C,
    ("g", ">"): 0x011D,
    ("G", "("): 0x011E,
    ("g", "("): 0x011F,
    ("G", "."): 0x0120,
    ("g", "."): 0x0121,
    ("G", ","): 0x0122,
    ("g", ","): 0x0123,
    ("H", ">"): 0x0124,
    ("h", ">"): 0x0125,
    ("H", "/"): 0x0126,
    ("h", "/"): 0x0127,
    ("I", "?"): 0x0128,
    ("i", "?"): 0x0129,
    ("I", "-"): 0x012A,
    ("i", "-"): 0x012B,
    ("I", "("): 0x012C,
    ("i", "("): 0x012D,
    ("I", ";"): 0x012E,
    ("i", ";"): 0x012F,
    ("I", "."): 0x0130,
    ("i", "."): 0x0131,
    ("I", "J"): 0x0132,
    ("i", "j"): 0x0133,
    ("J", ">"): 0x0134,
    ("j", ">"): 0x0135,
    ("K", ","): 0x0136,
    ("k", ","): 0x0137,
    ("k", "k"): 0x0138,
    ("L", "'"): 0x0139,
    ("l", "'"): 0x013A,
    ("L", ","): 0x013B,
    ("l", ","): 0x013C,
    ("L", "<"): 0x013D,
    ("l", "<"): 0x013E,
    ("L", "."): 0x013F,
    ("l", "."): 0x0140,
    ("L", "/"): 0x0141,
    ("l", "/"): 0x0142,
    ("N", "'"): 0x0143,
    ("n", "'"): 0x0144,
    ("N", ","): 0x0145,
    ("n", ","): 0x0146,
    ("N", "<"): 0x0147,
    ("n", "<"): 0x0148,
    ("'", "n"): 0x0149,
    ("N", "G"): 0x014A,
    ("n", "g"): 0x014B,
    ("O", "-"): 0x014C,
    ("o", "-"): 0x014D,
    ("O", "("): 0x014E,
    ("o", "("): 0x014F,
    ("O", '"'): 0x0150,
    ("o", '"'): 0x0151,
    ("O", "E"): 0x0152,
    ("o", "e"): 0x0153,
    ("R", "'"): 0x0154,
    ("r", "'"): 0x0155,
    ("R", ","): 0x0156,
    ("r", ","): 0x0157,
    ("R", "<"): 0x0158,
    ("r", "<"): 0x0159,
    ("S", "'"): 0x015A,
    ("s", "'"): 0x015B,
    ("S", ">"): 0x015C,
    ("s", ">"): 0x015D,
    ("S", ","): 0x015E,
    ("s", ","): 0x015F,
    ("S", "<"): 0x0160,
    ("s", "<"): 0x0161,
    ("T", ","): 0x0162,
    ("t", ","): 0x0163,
    ("T", "<"): 0x0164,
    ("t", "<"): 0x0165,
    ("T", "/"): 0x0166,
    ("t", "/"): 0x0167,
    ("U", "?"): 0x0168,
    ("u", "?"): 0x0169,
    ("U", "-"): 0x016A,
    ("u", "-"): 0x016B,
    ("U", "("): 0x016C,
    ("u", "("): 0x016D,
    ("U", "0"): 0x016E,
    ("u", "0"): 0x016F,
    ("U", '"'): 0x0170,
    ("u", '"'): 0x0171,
    ("U", ";"): 0x0172,
    ("u", ";"): 0x0173,
    ("W", ">"): 0x0174,
    ("w", ">"): 0x0175,
    ("Y", ">"): 0x0176,
    ("y", ">"): 0x0177,
    ("Y", ":"): 0x0178,
    ("Z", "'"): 0x0179,
    ("z", "'"): 0x017A,
    ("Z", "."): 0x017B,
    ("z", "."): 0x017C,
    ("Z", "<"): 0x017D,
    ("z", "<"): 0x017E,
    ("O", "9"): 0x01A0,
    ("o", "9"): 0x01A1,
    ("O", "I"): 0x01A2,
    ("o", "i"): 0x01A3,
    ("y", "r"): 0x01A6,
    ("U", "9"): 0x01AF,
    ("u", "9"): 0x01B0,
    ("Z", "/"): 0x01B5,
    ("z", "/"): 0x01B6,
    ("E", "D"): 0x01B7,
    ("A", "<"): 0x01CD,
    ("a", "<"): 0x01CE,
    ("I", "<"): 0x01CF,
    ("i", "<"): 0x01D0,
    ("O", "<"): 0x01D1,
    ("o", "<"): 0x01D2,
    ("U", "<"): 0x01D3,
    ("u", "<"): 0x01D4,
    ("A", "1"): 0x01DE,
    ("a", "1"): 0x01DF,
    ("A", "7"): 0x01E0,
    ("a", "7"): 0x01E1,
    ("A", "3"): 0x01E2,
    ("a", "3"): 0x01E3,
    ("G", "/"): 0x01E4,
    ("g", "/"): 0x01E5,
    ("G", "<"): 0x01E6,
    ("g", "<"): 0x01E7,
    ("K", "<"): 0x01E8,
    ("k", "<"): 0x01E9,
    ("O", ";"): 0x01EA,
    ("o", ";"): 0x01EB,
    ("O", "1"): 0x01EC,
    ("o", "1"): 0x01ED,
    ("E", "Z"): 0x01EE,
    ("e", "z"): 0x01EF,
    ("j", "<"): 0x01F0,
    ("G", "'"): 0x01F4,
    ("g", "'"): 0x01F5,
    (";", "S"): 0x02BF,
    ("'", "<"): 0x02C7,
    ("'", "("): 0x02D8,
    ("'", "."): 0x02D9,
    ("'", "0"): 0x02DA,
    ("'", ";"): 0x02DB,
    ("'", '"'): 0x02DD,
    ("A", "%"): 0x0386,
    ("E", "%"): 0x0388,
    ("Y", "%"): 0x0389,
    ("I", "%"): 0x038A,
    ("O", "%"): 0x038C,
    ("U", "%"): 0x038E,
    ("W", "%"): 0x038F,
    ("i", "3"): 0x0390,
    ("A", "*"): 0x0391,
    ("B", "*"): 0x0392,
    ("G", "*"): 0x0393,
    ("D", "*"): 0x0394,
    ("E", "*"): 0x0395,
    ("Z", "*"): 0x0396,
    ("Y", "*"): 0x0397,
    ("H", "*"): 0x0398,
    ("I", "*"): 0x0399,
    ("K", "*"): 0x039A,
    ("L", "*"): 0x039B,
    ("M", "*"): 0x039C,
    ("N", "*"): 0x039D,
    ("C", "*"): 0x039E,
    ("O", "*"): 0x039F,
    ("P", "*"): 0x03A0,
    ("R", "*"): 0x03A1,
    ("S", "*"): 0x03A3,
    ("T", "*"): 0x03A4,
    ("U", "*"): 0x03A5,
    ("F", "*"): 0x03A6,
    ("X", "*"): 0x03A7,
    ("Q", "*"): 0x03A8,
    ("W", "*"): 0x03A9,
    ("J", "*"): 0x03AA,
    ("V", "*"): 0x03AB,
    ("a", "%"): 0x03AC,
    ("e", "%"): 0x03AD,
    ("y", "%"): 0x03AE,
    ("i", "%"): 0x03AF,
    ("u", "3"): 0x03B0,
    ("a", "*"): 0x03B1,
    ("b", "*"): 0x03B2,
    ("g", "*"): 0x03B3,
    ("d", "*"): 0x03B4,
    ("e", "*"): 0x03B5,
    ("z", "*"): 0x03B6,
    ("y", "*"): 0x03B7,
    ("h", "*"): 0x03B8,
    ("i", "*"): 0x03B9,
    ("k", "*"): 0x03BA,
    ("l", "*"): 0x03BB,
    ("m", "*"): 0x03BC,
    ("n", "*"): 0x03BD,
    ("c", "*"): 0x03BE,
    ("o", "*"): 0x03BF,
    ("p", "*"): 0x03C0,
    ("r", "*"): 0x03C1,
    ("*", "s"): 0x03C2,
    ("s", "*"): 0x03C3,
    ("t", "*"): 0x03C4,
    ("u", "*"): 0x03C5,
    ("f", "*"): 0x03C6,
    ("x", "*"): 0x03C7,
    ("q", "*"): 0x03C8,
    ("w", "*"): 0x03C9,
    ("j", "*"): 0x03CA,
    ("v", "*"): 0x03CB,
    ("o", "%"): 0x03CC,
    ("u", "%"): 0x03CD,
    ("w", "%"): 0x03CE,
    ("'", "G"): 0x03D8,
    (",", "G"): 0x03D9,
    ("T", "3"): 0x03DA,
    ("t", "3"): 0x03DB,
    ("M", "3"): 0x03DC,
    ("m", "3"): 0x03DD,
    ("K", "3"): 0x03DE,
    ("k", "3"): 0x03DF,
    ("P", "3"): 0x03E0,
    ("p", "3"): 0x03E1,
    ("'", "%"): 0x03F4,
    ("j", "3"): 0x03F5,
    ("I", "O"): 0x0401,
    ("D", "%"): 0x0402,
    ("G", "%"): 0x0403,
    ("I", "E"): 0x0404,
    ("D", "S"): 0x0405,
    ("I", "I"): 0x0406,
    ("Y", "I"): 0x0407,
    ("J", "%"): 0x0408,
    ("L", "J"): 0x0409,
    ("N", "J"): 0x040A,
    ("T", "s"): 0x040B,
    ("K", "J"): 0x040C,
    ("V", "%"): 0x040E,
    ("D", "Z"): 0x040F,
    ("A", "="): 0x0410,
    ("B", "="): 0x0411,
    ("V", "="): 0x0412,
    ("G", "="): 0x0413,
    ("D", "="): 0x0414,
    ("E", "="): 0x0415,
    ("Z", "%"): 0x0416,
    ("Z", "="): 0x0417,
    ("I", "="): 0x0418,
    ("J", "="): 0x0419,
    ("K", "="): 0x041A,
    ("L", "="): 0x041B,
    ("M", "="): 0x041C,
    ("N", "="): 0x041D,
    ("O", "="): 0x041E,
    ("P", "="): 0x041F,
    ("R", "="): 0x0420,
    ("S", "="): 0x0421,
    ("T", "="): 0x0422,
    ("U", "="): 0x0423,
    ("F", "="): 0x0424,
    ("H", "="): 0x0425,
    ("C", "="): 0x0426,
    ("C", "%"): 0x0427,
    ("S", "%"): 0x0428,
    ("S", "c"): 0x0429,
    ("=", '"'): 0x042A,
    ("Y", "="): 0x042B,
    ("%", '"'): 0x042C,
    ("J", "E"): 0x042D,
    ("J", "U"): 0x042E,
    ("J", "A"): 0x042F,
    ("a", "="): 0x0430,
    ("b", "="): 0x0431,
    ("v", "="): 0x0432,
    ("g", "="): 0x0433,
    ("d", "="): 0x0434,
    ("e", "="): 0x0435,
    ("z", "%"): 0x0436,
    ("z", "="): 0x0437,
    ("i", "="): 0x0438,
    ("j", "="): 0x0439,
    ("k", "="): 0x043A,
    ("l", "="): 0x043B,
    ("m", "="): 0x043C,
    ("n", "="): 0x043D,
    ("o", "="): 0x043E,
    ("p", "="): 0x043F,
    ("r", "="): 0x0440,
    ("s", "="): 0x0441,
    ("t", "="): 0x0442,
    ("u", "="): 0x0443,
    ("f", "="): 0x0444,
    ("h", "="): 0x0445,
    ("c", "="): 0x0446,
    ("c", "%"): 0x0447,
    ("s", "%"): 0x0448,
    ("s", "c"): 0x0449,
    ("=", "'"): 0x044A,
    ("y", "="): 0x044B,
    ("%", "'"): 0x044C,
    ("j", "e"): 0x044D,
    ("j", "u"): 0x044E,
    ("j", "a"): 0x044F,
    ("i", "o"): 0x0451,
    ("d", "%"): 0x0452,
    ("g", "%"): 0x0453,
    ("i", "e"): 0x0454,
    ("d", "s"): 0x0455,
    ("i", "i"): 0x0456,
    ("y", "i"): 0x0457,
    ("j", "%"): 0x0458,
    ("l", "j"): 0x0459,
    ("n", "j"): 0x045A,
    ("t", "s"): 0x045B,
    ("k", "j"): 0x045C,
    ("v", "%"): 0x045E,
    ("d", "z"): 0x045F,
    ("Y", "3"): 0x0462,
    ("y", "3"): 0x0463,
    ("O", "3"): 0x046A,
    ("o", "3"): 0x046B,
    ("F", "3"): 0x0472,
    ("f", "3"): 0x0473,
    ("V", "3"): 0x0474,
    ("v", "3"): 0x0475,
    ("C", "3"): 0x0480,
    ("c", "3"): 0x0481,
    ("G", "3"): 0x0490,
    ("g", "3"): 0x0491,
    ("A", "+"): 0x05D0,
    ("B", "+"): 0x05D1,
    ("G", "+"): 0x05D2,
    ("D", "+"): 0x05D3,
    ("H", "+"): 0x05D4,
    ("W", "+"): 0x05D5,
    ("Z", "+"): 0x05D6,
    ("X", "+"): 0x05D7,
    ("T", "j"): 0x05D8,
    ("J", "+"): 0x05D9,
    ("K", "%"): 0x05DA,
    ("K", "+"): 0x05DB,
    ("L", "+"): 0x05DC,
    ("M", "%"): 0x05DD,
    ("M", "+"): 0x05DE,
    ("N", "%"): 0x05DF,
    ("N", "+"): 0x05E0,
    ("S", "+"): 0x05E1,
    ("E", "+"): 0x05E2,
    ("P", "%"): 0x05E3,
    ("P", "+"): 0x05E4,
    ("Z", "j"): 0x05E5,
    ("Z", "J"): 0x05E6,
    ("Q", "+"): 0x05E7,
    ("R", "+"): 0x05E8,
    ("S", "h"): 0x05E9,
    ("T", "+"): 0x05EA,
    (",", "+"): 0x060C,
    (";", "+"): 0x061B,
    ("?", "+"): 0x061F,
    ("H", "'"): 0x0621,
    ("a", "M"): 0x0622,
    ("a", "H"): 0x0623,
    ("w", "H"): 0x0624,
    ("a", "h"): 0x0625,
    ("y", "H"): 0x0626,
    ("a", "+"): 0x0627,
    ("b", "+"): 0x0628,
    ("t", "m"): 0x0629,
    ("t", "+"): 0x062A,
    ("t", "k"): 0x062B,
    ("g", "+"): 0x062C,
    ("h", "k"): 0x062D,
    ("x", "+"): 0x062E,
    ("d", "+"): 0x062F,
    ("d", "k"): 0x0630,
    ("r", "+"): 0x0631,
    ("z", "+"): 0x0632,
    ("s", "+"): 0x0633,
    ("s", "n"): 0x0634,
    ("c", "+"): 0x0635,
    ("d", "d"): 0x0636,
    ("t", "j"): 0x0637,
    ("z", "H"): 0x0638,
    ("e", "+"): 0x0639,
    ("i", "+"): 0x063A,
    ("+", "+"): 0x0640,
    ("f", "+"): 0x0641,
    ("q", "+"): 0x0642,
    ("k", "+"): 0x0643,
    ("l", "+"): 0x0644,
    ("m", "+"): 0x0645,
    ("n", "+"): 0x0646,
    ("h", "+"): 0x0647,
    ("w", "+"): 0x0648,
    ("j", "+"): 0x0649,
    ("y", "+"): 0x064A,
    (":", "+"): 0x064B,
    ('"', "+"): 0x064C,
    ("=", "+"): 0x064D,
    ("/", "+"): 0x064E,
    ("'", "+"): 0x064F,
    ("1", "+"): 0x0650,
    ("3", "+"): 0x0651,
    ("0", "+"): 0x0652,
    ("a", "S"): 0x0670,
    ("p", "+"): 0x067E,
    ("v", "+"): 0x06A4,
    ("g", "f"): 0x06AF,
    ("0", "a"): 0x06F0,
    ("1", "a"): 0x06F1,
    ("2", "a"): 0x06F2,
    ("3", "a"): 0x06F3,
    ("4", "a"): 0x06F4,
    ("5", "a"): 0x06F5,
    ("6", "a"): 0x06F6,
    ("7", "a"): 0x06F7,
    ("8", "a"): 0x06F8,
    ("9", "a"): 0x06F9,
    ("B", "."): 0x1E02,
    ("b", "."): 0x1E03,
    ("B", "_"): 0x1E06,
    ("b", "_"): 0x1E07,
    ("D", "."): 0x1E0A,
    ("d", "."): 0x1E0B,
    ("D", "_"): 0x1E0E,
    ("d", "_"): 0x1E0F,
    ("D", ","): 0x1E10,
    ("d", ","): 0x1E11,
    ("F", "."): 0x1E1E,
    ("f", "."): 0x1E1F,
    ("G", "-"): 0x1E20,
    ("g", "-"): 0x1E21,
    ("H", "."): 0x1E22,
    ("h", "."): 0x1E23,
    ("H", ":"): 0x1E26,
    ("h", ":"): 0x1E27,
    ("H", ","): 0x1E28,
    ("h", ","): 0x1E29,
    ("K", "'"): 0x1E30,
    ("k", "'"): 0x1E31,
    ("K", "_"): 0x1E34,
    ("k", "_"): 0x1E35,
    ("L", "_"): 0x1E3A,
    ("l", "_"): 0x1E3B,
    ("M", "'"): 0x1E3E,
    ("m", "'"): 0x1E3F,
    ("M", "."): 0x1E40,
    ("m", "."): 0x1E41,
    ("N", "."): 0x1E44,
    ("n", "."): 0x1E45,
    ("N", "_"): 0x1E48,
    ("n", "_"): 0x1E49,
    ("P", "'"): 0x1E54,
    ("p", "'"): 0x1E55,
    ("P", "."): 0x1E56,
    ("p", "."): 0x1E57,
    ("R", "."): 0x1E58,
    ("r", "."): 0x1E59,
    ("R", "_"): 0x1E5E,
    ("r", "_"): 0x1E5F,
    ("S", "."): 0x1E60,
    ("s", "."): 0x1E61,
    ("T", "."): 0x1E6A,
    ("t", "."): 0x1E6B,
    ("T", "_"): 0x1E6E,
    ("t", "_"): 0x1E6F,
    ("V", "?"): 0x1E7C,
    ("v", "?"): 0x1E7D,
    ("W", "!"): 0x1E80,
    ("w", "!"): 0x1E81,
    ("W", "'"): 0x1E82,
    ("w", "'"): 0x1E83,
    ("W", ":"): 0x1E84,
    ("w", ":"): 0x1E85,
    ("W", "."): 0x1E86,
    ("w", "."): 0x1E87,
    ("X", "."): 0x1E8A,
    ("x", "."): 0x1E8B,
    ("X", ":"): 0x1E8C,
    ("x", ":"): 0x1E8D,
    ("Y", "."): 0x1E8E,
    ("y", "."): 0x1E8F,
    ("Z", ">"): 0x1E90,
    ("z", ">"): 0x1E91,
    ("Z", "_"): 0x1E94,
    ("z", "_"): 0x1E95,
    ("h", "_"): 0x1E96,
    ("t", ":"): 0x1E97,
    ("w", "0"): 0x1E98,
    ("y", "0"): 0x1E99,
    ("A", "2"): 0x1EA2,
    ("a", "2"): 0x1EA3,
    ("E", "2"): 0x1EBA,
    ("e", "2"): 0x1EBB,
    ("E", "?"): 0x1EBC,
    ("e", "?"): 0x1EBD,
    ("I", "2"): 0x1EC8,
    ("i", "2"): 0x1EC9,
    ("O", "2"): 0x1ECE,
    ("o", "2"): 0x1ECF,
    ("U", "2"): 0x1EE6,
    ("u", "2"): 0x1EE7,
    ("Y", "!"): 0x1EF2,
    ("y", "!"): 0x1EF3,
    ("Y", "2"): 0x1EF6,
    ("y", "2"): 0x1EF7,
    ("Y", "?"): 0x1EF8,
    ("y", "?"): 0x1EF9,
    (";", "'"): 0x1F00,
    (",", "'"): 0x1F01,
    (";", "!"): 0x1F02,
    (",", "!"): 0x1F03,
    ("?", ";"): 0x1F04,
    ("?", ","): 0x1F05,
    ("!", ":"): 0x1F06,
    ("?", ":"): 0x1F07,
    ("1", "N"): 0x2002,
    ("1", "M"): 0x2003,
    ("3", "M"): 0x2004,
    ("4", "M"): 0x2005,
    ("6", "M"): 0x2006,
    ("1", "T"): 0x2009,
    ("1", "H"): 0x200A,
    ("-", "1"): 0x2010,
    ("-", "N"): 0x2013,
    ("-", "M"): 0x2014,
    ("-", "3"): 0x2015,
    ("!", "2"): 0x2016,
    ("=", "2"): 0x2017,
    ("'", "6"): 0x2018,
    ("'", "9"): 0x2019,
    (".", "9"): 0x201A,
    ("9", "'"): 0x201B,
    ('"', "6"): 0x201C,
    ('"', "9"): 0x201D,
    (":", "9"): 0x201E,
    ("9", '"'): 0x201F,
    ("/", "-"): 0x2020,
    ("/", "="): 0x2021,
    (".", "."): 0x2025,
    ("%", "0"): 0x2030,
    ("1", "'"): 0x2032,
    ("2", "'"): 0x2033,
    ("3", "'"): 0x2034,
    ("1", '"'): 0x2035,
    ("2", '"'): 0x2036,
    ("3", '"'): 0x2037,
    ("C", "a"): 0x2038,
    ("<", "1"): 0x2039,
    (">", "1"): 0x203A,
    (":", "X"): 0x203B,
    ("'", "-"): 0x203E,
    ("/", "f"): 0x2044,
    ("0", "S"): 0x2070,
    ("4", "S"): 0x2074,
    ("5", "S"): 0x2075,
    ("6", "S"): 0x2076,
    ("7", "S"): 0x2077,
    ("8", "S"): 0x2078,
    ("9", "S"): 0x2079,
    ("+", "S"): 0x207A,
    ("-", "S"): 0x207B,
    ("=", "S"): 0x207C,
    ("(", "S"): 0x207D,
    (")", "S"): 0x207E,
    ("n", "S"): 0x207F,
    ("0", "s"): 0x2080,
    ("1", "s"): 0x2081,
    ("2", "s"): 0x2082,
    ("3", "s"): 0x2083,
    ("4", "s"): 0x2084,
    ("5", "s"): 0x2085,
    ("6", "s"): 0x2086,
    ("7", "s"): 0x2087,
    ("8", "s"): 0x2088,
    ("9", "s"): 0x2089,
    ("+", "s"): 0x208A,
    ("-", "s"): 0x208B,
    ("=", "s"): 0x208C,
    ("(", "s"): 0x208D,
    (")", "s"): 0x208E,
    ("L", "i"): 0x20A4,
    ("P", "t"): 0x20A7,
    ("W", "="): 0x20A9,
    ("=", "e"): 0x20AC,  # euro
    ("E", "u"): 0x20AC,  # euro
    ("=", "R"): 0x20BD,  # rouble
    ("=", "P"): 0x20BD,  # rouble
    ("o", "C"): 0x2103,
    ("c", "o"): 0x2105,
    ("o", "F"): 0x2109,
    ("N", "0"): 0x2116,
    ("P", "O"): 0x2117,
    ("R", "x"): 0x211E,
    ("S", "M"): 0x2120,
    ("T", "M"): 0x2122,
    ("O", "m"): 0x2126,
    ("A", "O"): 0x212B,
    ("1", "3"): 0x2153,
    ("2", "3"): 0x2154,
    ("1", "5"): 0x2155,
    ("2", "5"): 0x2156,
    ("3", "5"): 0x2157,
    ("4", "5"): 0x2158,
    ("1", "6"): 0x2159,
    ("5", "6"): 0x215A,
    ("1", "8"): 0x215B,
    ("3", "8"): 0x215C,
    ("5", "8"): 0x215D,
    ("7", "8"): 0x215E,
    ("1", "R"): 0x2160,
    ("2", "R"): 0x2161,
    ("3", "R"): 0x2162,
    ("4", "R"): 0x2163,
    ("5", "R"): 0x2164,
    ("6", "R"): 0x2165,
    ("7", "R"): 0x2166,
    ("8", "R"): 0x2167,
    ("9", "R"): 0x2168,
    ("a", "R"): 0x2169,
    ("b", "R"): 0x216A,
    ("c", "R"): 0x216B,
    ("1", "r"): 0x2170,
    ("2", "r"): 0x2171,
    ("3", "r"): 0x2172,
    ("4", "r"): 0x2173,
    ("5", "r"): 0x2174,
    ("6", "r"): 0x2175,
    ("7", "r"): 0x2176,
    ("8", "r"): 0x2177,
    ("9", "r"): 0x2178,
    ("a", "r"): 0x2179,
    ("b", "r"): 0x217A,
    ("c", "r"): 0x217B,
    ("<", "-"): 0x2190,
    ("-", "!"): 0x2191,
    ("-", ">"): 0x2192,
    ("-", "v"): 0x2193,
    ("<", ">"): 0x2194,
    ("U", "D"): 0x2195,
    ("<", "="): 0x21D0,
    ("=", ">"): 0x21D2,
    ("=", "="): 0x21D4,
    ("F", "A"): 0x2200,
    ("d", "P"): 0x2202,
    ("T", "E"): 0x2203,
    ("/", "0"): 0x2205,
    ("D", "E"): 0x2206,
    ("N", "B"): 0x2207,
    ("(", "-"): 0x2208,
    ("-", ")"): 0x220B,
    ("*", "P"): 0x220F,
    ("+", "Z"): 0x2211,
    ("-", "2"): 0x2212,
    ("-", "+"): 0x2213,
    ("*", "-"): 0x2217,
    ("O", "b"): 0x2218,
    ("S", "b"): 0x2219,
    ("R", "T"): 0x221A,
    ("0", "("): 0x221D,
    ("0", "0"): 0x221E,
    ("-", "L"): 0x221F,
    ("-", "V"): 0x2220,
    ("P", "P"): 0x2225,
    ("A", "N"): 0x2227,
    ("O", "R"): 0x2228,
    ("(", "U"): 0x2229,
    (")", "U"): 0x222A,
    ("I", "n"): 0x222B,
    ("D", "I"): 0x222C,
    ("I", "o"): 0x222E,
    (".", ":"): 0x2234,
    (":", "."): 0x2235,
    (":", "R"): 0x2236,
    (":", ":"): 0x2237,
    ("?", "1"): 0x223C,
    ("C", "G"): 0x223E,
    ("?", "-"): 0x2243,
    ("?", "="): 0x2245,
    ("?", "2"): 0x2248,
    ("=", "?"): 0x224C,
    ("H", "I"): 0x2253,
    ("!", "="): 0x2260,
    ("=", "3"): 0x2261,
    ("=", "<"): 0x2264,
    (">", "="): 0x2265,
    ("<", "*"): 0x226A,
    ("*", ">"): 0x226B,
    ("!", "<"): 0x226E,
    ("!", ">"): 0x226F,
    ("(", "C"): 0x2282,
    (")", "C"): 0x2283,
    ("(", "_"): 0x2286,
    (")", "_"): 0x2287,
    ("0", "."): 0x2299,
    ("0", "2"): 0x229A,
    ("-", "T"): 0x22A5,
    (".", "P"): 0x22C5,
    (":", "3"): 0x22EE,
    (".", "3"): 0x22EF,
    ("E", "h"): 0x2302,
    ("<", "7"): 0x2308,
    (">", "7"): 0x2309,
    ("7", "<"): 0x230A,
    ("7", ">"): 0x230B,
    ("N", "I"): 0x2310,
    ("(", "A"): 0x2312,
    ("T", "R"): 0x2315,
    ("I", "u"): 0x2320,
    ("I", "l"): 0x2321,
    ("<", "/"): 0x2329,
    ("/", ">"): 0x232A,
    ("V", "s"): 0x2423,
    ("1", "h"): 0x2440,
    ("3", "h"): 0x2441,
    ("2", "h"): 0x2442,
    ("4", "h"): 0x2443,
    ("1", "j"): 0x2446,
    ("2", "j"): 0x2447,
    ("3", "j"): 0x2448,
    ("4", "j"): 0x2449,
    ("1", "."): 0x2488,
    ("2", "."): 0x2489,
    ("3", "."): 0x248A,
    ("4", "."): 0x248B,
    ("5", "."): 0x248C,
    ("6", "."): 0x248D,
    ("7", "."): 0x248E,
    ("8", "."): 0x248F,
    ("9", "."): 0x2490,
    ("h", "h"): 0x2500,
    ("H", "H"): 0x2501,
    ("v", "v"): 0x2502,
    ("V", "V"): 0x2503,
    ("3", "-"): 0x2504,
    ("3", "_"): 0x2505,
    ("3", "!"): 0x2506,
    ("3", "/"): 0x2507,
    ("4", "-"): 0x2508,
    ("4", "_"): 0x2509,
    ("4", "!"): 0x250A,
    ("4", "/"): 0x250B,
    ("d", "r"): 0x250C,
    ("d", "R"): 0x250D,
    ("D", "r"): 0x250E,
    ("D", "R"): 0x250F,
    ("d", "l"): 0x2510,
    ("d", "L"): 0x2511,
    ("D", "l"): 0x2512,
    ("L", "D"): 0x2513,
    ("u", "r"): 0x2514,
    ("u", "R"): 0x2515,
    ("U", "r"): 0x2516,
    ("U", "R"): 0x2517,
    ("u", "l"): 0x2518,
    ("u", "L"): 0x2519,
    ("U", "l"): 0x251A,
    ("U", "L"): 0x251B,
    ("v", "r"): 0x251C,
    ("v", "R"): 0x251D,
    ("V", "r"): 0x2520,
    ("V", "R"): 0x2523,
    ("v", "l"): 0x2524,
    ("v", "L"): 0x2525,
    ("V", "l"): 0x2528,
    ("V", "L"): 0x252B,
    ("d", "h"): 0x252C,
    ("d", "H"): 0x252F,
    ("D", "h"): 0x2530,
    ("D", "H"): 0x2533,
    ("u", "h"): 0x2534,
    ("u", "H"): 0x2537,
    ("U", "h"): 0x2538,
    ("U", "H"): 0x253B,
    ("v", "h"): 0x253C,
    ("v", "H"): 0x253F,
    ("V", "h"): 0x2542,
    ("V", "H"): 0x254B,
    ("F", "D"): 0x2571,
    ("B", "D"): 0x2572,
    ("T", "B"): 0x2580,
    ("L", "B"): 0x2584,
    ("F", "B"): 0x2588,
    ("l", "B"): 0x258C,
    ("R", "B"): 0x2590,
    (".", "S"): 0x2591,
    (":", "S"): 0x2592,
    ("?", "S"): 0x2593,
    ("f", "S"): 0x25A0,
    ("O", "S"): 0x25A1,
    ("R", "O"): 0x25A2,
    ("R", "r"): 0x25A3,
    ("R", "F"): 0x25A4,
    ("R", "Y"): 0x25A5,
    ("R", "H"): 0x25A6,
    ("R", "Z"): 0x25A7,
    ("R", "K"): 0x25A8,
    ("R", "X"): 0x25A9,
    ("s", "B"): 0x25AA,
    ("S", "R"): 0x25AC,
    ("O", "r"): 0x25AD,
    ("U", "T"): 0x25B2,
    ("u", "T"): 0x25B3,
    ("P", "R"): 0x25B6,
    ("T", "r"): 0x25B7,
    ("D", "t"): 0x25BC,
    ("d", "T"): 0x25BD,
    ("P", "L"): 0x25C0,
    ("T", "l"): 0x25C1,
    ("D", "b"): 0x25C6,
    ("D", "w"): 0x25C7,
    ("L", "Z"): 0x25CA,
    ("0", "m"): 0x25CB,
    ("0", "o"): 0x25CE,
    ("0", "M"): 0x25CF,
    ("0", "L"): 0x25D0,
    ("0", "R"): 0x25D1,
    ("S", "n"): 0x25D8,
    ("I", "c"): 0x25D9,
    ("F", "d"): 0x25E2,
    ("B", "d"): 0x25E3,
    ("*", "2"): 0x2605,
    ("*", "1"): 0x2606,
    ("<", "H"): 0x261C,
    (">", "H"): 0x261E,
    ("0", "u"): 0x263A,
    ("0", "U"): 0x263B,
    ("S", "U"): 0x263C,
    ("F", "m"): 0x2640,
    ("M", "l"): 0x2642,
    ("c", "S"): 0x2660,
    ("c", "H"): 0x2661,
    ("c", "D"): 0x2662,
    ("c", "C"): 0x2663,
    ("M", "d"): 0x2669,
    ("M", "8"): 0x266A,
    ("M", "2"): 0x266B,
    ("M", "b"): 0x266D,
    ("M", "x"): 0x266E,
    ("M", "X"): 0x266F,
    ("O", "K"): 0x2713,
    ("X", "X"): 0x2717,
    ("-", "X"): 0x2720,
    ("I", "S"): 0x3000,
    (",", "_"): 0x3001,
    (".", "_"): 0x3002,
    ("+", '"'): 0x3003,
    ("+", "_"): 0x3004,
    ("*", "_"): 0x3005,
    (";", "_"): 0x3006,
    ("0", "_"): 0x3007,
    ("<", "+"): 0x300A,
    (">", "+"): 0x300B,
    ("<", "'"): 0x300C,
    (">", "'"): 0x300D,
    ("<", '"'): 0x300E,
    (">", '"'): 0x300F,
    ("(", '"'): 0x3010,
    (")", '"'): 0x3011,
    ("=", "T"): 0x3012,
    ("=", "_"): 0x3013,
    ("(", "'"): 0x3014,
    (")", "'"): 0x3015,
    ("(", "I"): 0x3016,
    (")", "I"): 0x3017,
    ("-", "?"): 0x301C,
    ("A", "5"): 0x3041,
    ("a", "5"): 0x3042,
    ("I", "5"): 0x3043,
    ("i", "5"): 0x3044,
    ("U", "5"): 0x3045,
    ("u", "5"): 0x3046,
    ("E", "5"): 0x3047,
    ("e", "5"): 0x3048,
    ("O", "5"): 0x3049,
    ("o", "5"): 0x304A,
    ("k", "a"): 0x304B,
    ("g", "a"): 0x304C,
    ("k", "i"): 0x304D,
    ("g", "i"): 0x304E,
    ("k", "u"): 0x304F,
    ("g", "u"): 0x3050,
    ("k", "e"): 0x3051,
    ("g", "e"): 0x3052,
    ("k", "o"): 0x3053,
    ("g", "o"): 0x3054,
    ("s", "a"): 0x3055,
    ("z", "a"): 0x3056,
    ("s", "i"): 0x3057,
    ("z", "i"): 0x3058,
    ("s", "u"): 0x3059,
    ("z", "u"): 0x305A,
    ("s", "e"): 0x305B,
    ("z", "e"): 0x305C,
    ("s", "o"): 0x305D,
    ("z", "o"): 0x305E,
    ("t", "a"): 0x305F,
    ("d", "a"): 0x3060,
    ("t", "i"): 0x3061,
    ("d", "i"): 0x3062,
    ("t", "U"): 0x3063,
    ("t", "u"): 0x3064,
    ("d", "u"): 0x3065,
    ("t", "e"): 0x3066,
    ("d", "e"): 0x3067,
    ("t", "o"): 0x3068,
    ("d", "o"): 0x3069,
    ("n", "a"): 0x306A,
    ("n", "i"): 0x306B,
    ("n", "u"): 0x306C,
    ("n", "e"): 0x306D,
    ("n", "o"): 0x306E,
    ("h", "a"): 0x306F,
    ("b", "a"): 0x3070,
    ("p", "a"): 0x3071,
    ("h", "i"): 0x3072,
    ("b", "i"): 0x3073,
    ("p", "i"): 0x3074,
    ("h", "u"): 0x3075,
    ("b", "u"): 0x3076,
    ("p", "u"): 0x3077,
    ("h", "e"): 0x3078,
    ("b", "e"): 0x3079,
    ("p", "e"): 0x307A,
    ("h", "o"): 0x307B,
    ("b", "o"): 0x307C,
    ("p", "o"): 0x307D,
    ("m", "a"): 0x307E,
    ("m", "i"): 0x307F,
    ("m", "u"): 0x3080,
    ("m", "e"): 0x3081,
    ("m", "o"): 0x3082,
    ("y", "A"): 0x3083,
    ("y", "a"): 0x3084,
    ("y", "U"): 0x3085,
    ("y", "u"): 0x3086,
    ("y", "O"): 0x3087,
    ("y", "o"): 0x3088,
    ("r", "a"): 0x3089,
    ("r", "i"): 0x308A,
    ("r", "u"): 0x308B,
    ("r", "e"): 0x308C,
    ("r", "o"): 0x308D,
    ("w", "A"): 0x308E,
    ("w", "a"): 0x308F,
    ("w", "i"): 0x3090,
    ("w", "e"): 0x3091,
    ("w", "o"): 0x3092,
    ("n", "5"): 0x3093,
    ("v", "u"): 0x3094,
    ('"', "5"): 0x309B,
    ("0", "5"): 0x309C,
    ("*", "5"): 0x309D,
    ("+", "5"): 0x309E,
    ("a", "6"): 0x30A1,
    ("A", "6"): 0x30A2,
    ("i", "6"): 0x30A3,
    ("I", "6"): 0x30A4,
    ("u", "6"): 0x30A5,
    ("U", "6"): 0x30A6,
    ("e", "6"): 0x30A7,
    ("E", "6"): 0x30A8,
    ("o", "6"): 0x30A9,
    ("O", "6"): 0x30AA,
    ("K", "a"): 0x30AB,
    ("G", "a"): 0x30AC,
    ("K", "i"): 0x30AD,
    ("G", "i"): 0x30AE,
    ("K", "u"): 0x30AF,
    ("G", "u"): 0x30B0,
    ("K", "e"): 0x30B1,
    ("G", "e"): 0x30B2,
    ("K", "o"): 0x30B3,
    ("G", "o"): 0x30B4,
    ("S", "a"): 0x30B5,
    ("Z", "a"): 0x30B6,
    ("S", "i"): 0x30B7,
    ("Z", "i"): 0x30B8,
    ("S", "u"): 0x30B9,
    ("Z", "u"): 0x30BA,
    ("S", "e"): 0x30BB,
    ("Z", "e"): 0x30BC,
    ("S", "o"): 0x30BD,
    ("Z", "o"): 0x30BE,
    ("T", "a"): 0x30BF,
    ("D", "a"): 0x30C0,
    ("T", "i"): 0x30C1,
    ("D", "i"): 0x30C2,
    ("T", "U"): 0x30C3,
    ("T", "u"): 0x30C4,
    ("D", "u"): 0x30C5,
    ("T", "e"): 0x30C6,
    ("D", "e"): 0x30C7,
    ("T", "o"): 0x30C8,
    ("D", "o"): 0x30C9,
    ("N", "a"): 0x30CA,
    ("N", "i"): 0x30CB,
    ("N", "u"): 0x30CC,
    ("N", "e"): 0x30CD,
    ("N", "o"): 0x30CE,
    ("H", "a"): 0x30CF,
    ("B", "a"): 0x30D0,
    ("P", "a"): 0x30D1,
    ("H", "i"): 0x30D2,
    ("B", "i"): 0x30D3,
    ("P", "i"): 0x30D4,
    ("H", "u"): 0x30D5,
    ("B", "u"): 0x30D6,
    ("P", "u"): 0x30D7,
    ("H", "e"): 0x30D8,
    ("B", "e"): 0x30D9,
    ("P", "e"): 0x30DA,
    ("H", "o"): 0x30DB,
    ("B", "o"): 0x30DC,
    ("P", "o"): 0x30DD,
    ("M", "a"): 0x30DE,
    ("M", "i"): 0x30DF,
    ("M", "u"): 0x30E0,
    ("M", "e"): 0x30E1,
    ("M", "o"): 0x30E2,
    ("Y", "A"): 0x30E3,
    ("Y", "a"): 0x30E4,
    ("Y", "U"): 0x30E5,
    ("Y", "u"): 0x30E6,
    ("Y", "O"): 0x30E7,
    ("Y", "o"): 0x30E8,
    ("R", "a"): 0x30E9,
    ("R", "i"): 0x30EA,
    ("R", "u"): 0x30EB,
    ("R", "e"): 0x30EC,
    ("R", "o"): 0x30ED,
    ("W", "A"): 0x30EE,
    ("W", "a"): 0x30EF,
    ("W", "i"): 0x30F0,
    ("W", "e"): 0x30F1,
    ("W", "o"): 0x30F2,
    ("N", "6"): 0x30F3,
    ("V", "u"): 0x30F4,
    ("K", "A"): 0x30F5,
    ("K", "E"): 0x30F6,
    ("V", "a"): 0x30F7,
    ("V", "i"): 0x30F8,
    ("V", "e"): 0x30F9,
    ("V", "o"): 0x30FA,
    (".", "6"): 0x30FB,
    ("-", "6"): 0x30FC,
    ("*", "6"): 0x30FD,
    ("+", "6"): 0x30FE,
    ("b", "4"): 0x3105,
    ("p", "4"): 0x3106,
    ("m", "4"): 0x3107,
    ("f", "4"): 0x3108,
    ("d", "4"): 0x3109,
    ("t", "4"): 0x310A,
    ("n", "4"): 0x310B,
    ("l", "4"): 0x310C,
    ("g", "4"): 0x310D,
    ("k", "4"): 0x310E,
    ("h", "4"): 0x310F,
    ("j", "4"): 0x3110,
    ("q", "4"): 0x3111,
    ("x", "4"): 0x3112,
    ("z", "h"): 0x3113,
    ("c", "h"): 0x3114,
    ("s", "h"): 0x3115,
    ("r", "4"): 0x3116,
    ("z", "4"): 0x3117,
    ("c", "4"): 0x3118,
    ("s", "4"): 0x3119,
    ("a", "4"): 0x311A,
    ("o", "4"): 0x311B,
    ("e", "4"): 0x311C,
    ("a", "i"): 0x311E,
    ("e", "i"): 0x311F,
    ("a", "u"): 0x3120,
    ("o", "u"): 0x3121,
    ("a", "n"): 0x3122,
    ("e", "n"): 0x3123,
    ("a", "N"): 0x3124,
    ("e", "N"): 0x3125,
    ("e", "r"): 0x3126,
    ("i", "4"): 0x3127,
    ("u", "4"): 0x3128,
    ("i", "u"): 0x3129,
    ("v", "4"): 0x312A,
    ("n", "G"): 0x312B,
    ("g", "n"): 0x312C,
    ("1", "c"): 0x3220,
    ("2", "c"): 0x3221,
    ("3", "c"): 0x3222,
    ("4", "c"): 0x3223,
    ("5", "c"): 0x3224,
    ("6", "c"): 0x3225,
    ("7", "c"): 0x3226,
    ("8", "c"): 0x3227,
    ("9", "c"): 0x3228,
    # code points 0xe000 - 0xefff excluded, they have no assigned
    # characters, only used in proposals.
    ("f", "f"): 0xFB00,
    ("f", "i"): 0xFB01,
    ("f", "l"): 0xFB02,
    ("f", "t"): 0xFB05,
    ("s", "t"): 0xFB06,
    # Vim 5.x compatible digraphs that don't conflict with the above
    ("~", "!"): 161,
    ("c", "|"): 162,
    ("$", "$"): 163,
    ("o", "x"): 164,  # currency symbol in ISO 8859-1
    ("Y", "-"): 165,
    ("|", "|"): 166,
    ("c", "O"): 169,
    ("-", ","): 172,
    ("-", "="): 175,
    ("~", "o"): 176,
    ("2", "2"): 178,
    ("3", "3"): 179,
    ("p", "p"): 182,
    ("~", "."): 183,
    ("1", "1"): 185,
    ("~", "?"): 191,
    ("A", "`"): 192,
    ("A", "^"): 194,
    ("A", "~"): 195,
    ("A", '"'): 196,
    ("A", "@"): 197,
    ("E", "`"): 200,
    ("E", "^"): 202,
    ("E", '"'): 203,
    ("I", "`"): 204,
    ("I", "^"): 206,
    ("I", '"'): 207,
    ("N", "~"): 209,
    ("O", "`"): 210,
    ("O", "^"): 212,
    ("O", "~"): 213,
    ("/", "\\"): 215,  # multiplication symbol in ISO 8859-1
    ("U", "`"): 217,
    ("U", "^"): 219,
    ("I", "p"): 222,
    ("a", "`"): 224,
    ("a", "^"): 226,
    ("a", "~"): 227,
    ("a", '"'): 228,
    ("a", "@"): 229,
    ("e", "`"): 232,
    ("e", "^"): 234,
    ("e", '"'): 235,
    ("i", "`"): 236,
    ("i", "^"): 238,
    ("n", "~"): 241,
    ("o", "`"): 242,
    ("o", "^"): 244,
    ("o", "~"): 245,
    ("u", "`"): 249,
    ("u", "^"): 251,
    ("y", '"'): 255,
}

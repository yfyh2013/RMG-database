#!/usr/bin/env python
# encoding: utf-8

name = "H2_Loss/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Di-H-ene"], products=["ene1","H2"], ownReverse=False)

reverse = "none"

reversible = True
recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*8'],
    ['BREAK_BOND', '*6', 1, '*7'],
    ['FORM_BOND', '*7', 1, '*8'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*6'],
])

entry(
    index = 0,
    label = "Di-H-ene",
    group = 
"""
1 *1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 *2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 *3 C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4 *4 C u0 p0 c0 {3,S} {5,D} {11,S}
5 *5 C u0 p0 c0 {4,D} {6,S} {12,S}
6 *6 C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
7 R u0 p0 c0 {1,S}
8 R u0 p0 c0 {2,S}
9 R u0 p0 c0 {3,S}
10 *8 H u0 p0 c0 {3,S}
11 R u0 p0 c0 {4,S}
12 R u0 p0 c0 {5,S}
13 *7 H u0 p0 c0 {6,S}
14 R u0 p0 c0 {6,S}
""",
    kinetics = None,
)

tree(
"""
L1: Di-H-ene
"""
)


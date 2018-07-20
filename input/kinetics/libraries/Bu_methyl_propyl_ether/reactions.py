#!/usr/bin/env python
# encoding: utf-8

name = "Bu_MPO"
shortDesc = u""
longDesc = u"""

"""
autoGenerated=False
entry(
    index = 0,
    label = "MPO + O2 <=> MPO1J + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44.91, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether
""",
)

entry(
    index = 1,
    label = "MPO + OH <=> MPO1J + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (935000, 'cm^3/(mol*s)'),
        n = 2.29,
        Ea = (-0.78, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether
""",
)

entry(
    index = 2,
    label = "MPO1J + O2 => MPO1QJ",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether
""",
)

entry(
    index = 3,
    label = "MPO1QJ <=> MPO1Q-1J",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.974e+07, 's^-1'),
        n = 1.34,
        Ea = (13.961, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF: G4 calculations and HID from RMG',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF: G4 calculations and HID from RMG
""",
)

entry(
    index = 4,
    label = "MPO1QJ <=> MPO1Q2J",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(150.5, 's^-1'), n=2.993, Ea=(22.041, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "MPO1QJ <=> MPO1Q3J",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(187400, 's^-1'), n=2.003, Ea=(17.53, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "MPO1QJ <=> MPO1Star + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.034e+10, 's^-1'), n=1.109, Ea=(30.611, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "MPO1Q-1J <=> MPO1-1OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(217200, 's^-1'), n=1.242, Ea=(9.946, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "MPO1Q-1J <=> propanal + CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (113.5, 's^-1'),
        n = 2.693,
        Ea = (6.75, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 9,
    label = "MPO1Q2J <=> MPO12OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.408e+10, 's^-1'),
        n = 0.591,
        Ea = (14.27, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'added',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
added
""",
)

entry(
    index = 10,
    label = "MPO1Q2J <=> MPO1Star + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.728e+11, 's^-1'),
        n = -0.058,
        Ea = (24.54, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 11,
    label = "MPO1Q3J <=> MPO13OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (31610, 's^-1'),
        n = 1.706,
        Ea = (7.488, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 12,
    label = "MPO1Q3J <=> CH3OCHO + C2H4 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (157400, 's^-1'),
        n = 1.509,
        Ea = (17.217, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 13,
    label = "MPO1Q-1J + O2 <=> MPO1Q-1QJ",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether
""",
)

entry(
    index = 14,
    label = "MPO1Q3J + O2 <=> MPO1Q3QJ",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 15,
    label = "MPO1Q-1QJ <=> MPO1O-1Q + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.658e+10, 's^-1'),
        n = 0.13,
        Ea = (14.506, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF: G4 calculations and HID from RMG',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF: G4 calculations and HID from RMG
""",
)

entry(
    index = 16,
    label = "MPO1Q-1QJ <=> MPO1Q2J-1Q",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.552e+08, 's^-1'),
        n = 0.526,
        Ea = (13.985, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 17,
    label = "MPO1Q-1QJ <=> Ozoind1-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.105e+17, 's^-1'),
        n = -1.948,
        Ea = (43.801, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 18,
    label = "MPO1Q3QJ <=> MPO1O3Q + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+10, 's^-1'),
        n = 0.555,
        Ea = (15.724, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 19,
    label = "MPO1Q3QJ <=> MPO1Q2J3Q",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (282200, 's^-1'),
        n = 2.104,
        Ea = (25.626, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 20,
    label = "MPO1Q3QJ <=> MPO1Q2Star + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.132e+13, 's^-1'),
        n = -0.199,
        Ea = (28.052, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 21,
    label = "MPO1Q3QJ <=> Ozoind13 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.81e+16, 's^-1'),
        n = -1.277,
        Ea = (44, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 22,
    label = "MPO1Q2J-1Q <=> MPO1Q2-1OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.382e+15, 's^-1'),
        n = -1.199,
        Ea = (17.561, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 23,
    label = "MPO1Q2J-1Q <=> MPO-1Q12OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.103e+17, 's^-1'),
        n = -1.498,
        Ea = (7.076, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 24,
    label = "MPO1Q2J3Q <=> MPO1Q2Star + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.552e+14, 's^-1'),
        n = -0.356,
        Ea = (18.611, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 25,
    label = "MPO1Q2J3Q <=> MPO1Q23OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.285e+10, 's^-1'),
        n = 1.123,
        Ea = (14.77, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 26,
    label = "MPO1Q2J3Q <=> MPO3Q12OCYC + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.741e+07, 's^-1'),
        n = 1.777,
        Ea = (12.108, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 27,
    label = "MPO1O-1Q <=> MPO1O-1OJ + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (40.5, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed REF:Kaiser, Journal of Physical Chemistry, A 104, No. 35, 8194-8206, 2000 dimethylether
""",
)

entry(
    index = 28,
    label = "MPO1O3Q <=> MPO1O3OJ + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+16, 's^-1'), n=0, Ea=(40.5, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 29,
    label = "MPO1O-1Q <=> MPO_CP1-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.416e+11, 's^-1'),
        n = 0.153,
        Ea = (35.947, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'REF: G4 calculations and HID from RMG',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
REF: G4 calculations and HID from RMG
""",
)

entry(
    index = 30,
    label = "MPO1O-1Q + HCOOH <=> HCOOH + MPO_CP1-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.756, 'cm^3/(mol*s)'),
        n = 1.816,
        Ea = (-3.086, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 31,
    label = "MPO1O-1Q <=> Propionic + OH + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.742e+15, 's^-1'),
        n = -0.392,
        Ea = (45.8, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 32,
    label = "MPO1O-1OJ + O2 <=> MPO1O-1O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2443, 'cm^3/(mol*s)'),
        n = 3.574,
        Ea = (6.051, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 33,
    label = "MPO1O-1OJ <=> Propionic + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.443e+11, 's^-1'),
        n = 0.444,
        Ea = (9.642, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 34,
    label = "MPO1O3Q <=> MPO_CP13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.552e+10, 's^-1'),
        n = -0.334,
        Ea = (11.444, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 35,
    label = "MPO1O3Q + HCOOH <=> HCOOH + MPO_CP13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.065e+10, 'cm^3/(mol*s)'),
        n = -3.325,
        Ea = (-8.34, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 36,
    label = "MPO1O3OJ <=> CH2O + CH2COOCH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.977e+09, 's^-1'), n=1.184, Ea=(13.87, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 37,
    label = "MPO1O3OJ <=> MPO1O3O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.049e+10, 's^-1'),
        n = 1.186,
        Ea = (17.281, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 38,
    label = "MPO1O3OJ + O2 <=> MPO1O3O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2347, 'cm^3/(mol*s)'),
        n = 3.588,
        Ea = (6.305, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed
""",
)

entry(
    index = 39,
    label = "MPO1J <=> propanal + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.90639e+11, 's^-1'),
        n = 0.416984,
        Ea = (24.2665, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'changed CBS-QB3 Sarah Khanniche calculation',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
changed CBS-QB3 Sarah Khanniche calculation
""",
)

entry(
    index = 40,
    label = "CH3O2H + CHO <=> CH2O + CH3O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28353e-07, 'cm^3/(mol*s)'),
        n = 5.50561,
        Ea = (3.3939, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'UCCSD(T)-F12a/cc-pVTZ-F12//UM06-2X/aug-cc-pVTZ rate of H abstraction of methyl peroxide by formyl. Colin Grambow',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
UCCSD(T)-F12a/cc-pVTZ-F12//UM06-2X/aug-cc-pVTZ rate of H abstraction of methyl peroxide by formyl. Colin Grambow
""",
)

entry(
    index = 41,
    label = "MPO <=> CH3OH + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.451, 's^-1'),
        n = 4.024,
        Ea = (55.261, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'G4 calculations and HID from RMG',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
G4 calculations and HID from RMG
""",
)

entry(
    index = 42,
    label = "MPrO-1J <=> CH2O + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.367e+13, 's^-1'), n=-0.167, Ea=(25.178, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 43,
    label = "MPO + H <=> MPrO3J + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (811800, 'cm^3/(mol*s)'),
        n = 2.301,
        Ea = (4.906, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)


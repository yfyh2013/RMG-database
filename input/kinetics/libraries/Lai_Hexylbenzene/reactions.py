#!/usr/bin/env python
# encoding: utf-8

name = "Lai_Hexylbenzene"
shortDesc = u"Reactions for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
In conjunction with the Lai_Hexylbenzene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to Hexylbenzene pyrolysis and supercritical water treatment.

Lai, Lawrence, Gudiyella, Soumya, Liu, Mengjie, Green, William H. "Chemistry of Alkylaromatics Reconsidered". To be submitted to Energy and Fuels, 2017.

Both calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Cantherm.
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were not used.

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation (and therefore the activation energy) by CBS-QB3 calculations to be + or - 2.4kcal/mol 
(http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448). 
"""
entry(
    index = 1,
    label = "butyl + styrene <=> rad1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(236.006, 'cm^3/(mol*s)'), n=2.7878, Ea=(15.4228, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, April 2017, CBS-QB3 level of theory"
)

entry(
    index = 2,
    label = "Hexylbenzene <=> Toluene + 1-Pentene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62907e+07, 's^-1'), n=1.6863, Ea=(309.226, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Max Liu, CBS-QB3 level of theory"
)

entry(
    index = 3,
    label = "Hexylbenzene + H <=> HexylbenzenePlusHSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.76237e+07, 'cm^3/(mol*s)'), n=1.70829, Ea=(25.4744, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Hexylbenzene + H in the substituted position to form CCCCCCC1C=C[CH]C=C1
Level of Theory: CBS-QB3
Number of Rotors included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 4,
    label = "Toluene + H <=> ToluenePlusHOrtho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.02442e+09, 'cm^3/(mol*s)'), n=1.43982, Ea=(18.8871, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the ortho position to form CC1=C[CH]C=CC1
Level of Theory: CBS-QB3
Number of Rotors included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 5,
    label = "Toluene + H <=> ToluenePlusHMeta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.07929e+09, 'cm^3/(mol*s)'), n=1.42903, Ea=(22.7647, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Meta position to form CC1[CH]C=CCC=1
Level of Theory: CBS-QB3
Number of Rotors included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 6,
    label = "Toluene + H <=> ToluenePlusHPara",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1233e+09, 'cm^3/(mol*s)'), n=1.42368, Ea=(22.5731, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Para position to form C[C]1C=CCC=C1
Level of Theory: CBS-QB3
Number of Rotors included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 7,
    label = "Toluene + H <=> ToluenePlusHSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.20433e+08, 'cm^3/(mol*s)'), n=1.56916, Ea=(26.7856, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Substituted position to form CC1C=C[CH]C=C1
Level of Theory: CBS-QB3
Number of Rotors included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 8,
    label = "Toluene + CH3 <=> ToluenePlusCH3Ortho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3383.86, 'cm^3/(mol*s)'), n=2.311, Ea=(37.9756, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Ortho position to form CC1=CC=C[CH]C1C
Level of Theory: CBS-QB3
Number of Rotors included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 9,
    label = "Toluene + CH3 <=> ToluenePlusCH3Meta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3356.39, 'cm^3/(mol*s)'), n=2.32609, Ea=(41.1979, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Meta position to form CC1[CH]C(C)C=CC=1
Level of Theory: CBS-QB3
Number of Rotors included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 10,
    label = "Toluene + CH3 <=> ToluenePlusCH3Para",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3945.69, 'cm^3/(mol*s)'), n=2.31104, Ea=(41.6199, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the Para position to form CC1C=CC(C)[CH]C=1
Level of Theory: CBS-QB3
Number of Rotors included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 11,
    label = "Toluene + CH3 <=> ToluenePlusCH3Sub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144.44, 'cm^3/(mol*s)'), n=2.6469, Ea=(43.8158, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for Toluene + H in the substituted position to form CC1(C)[CH]C=CC=C1
Level of Theory: CBS-QB3
Number of Rotors included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
"""
)

entry(
    index = 12,
    label = "rad4 <=> EthyltetralinRad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29023.5, 's^-1'), n=1.19861, Ea=(27.5998, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for rad4 <=> EthyltetralinRad
Level of Theory: CBS-QB3
Number of Rotors included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/intra_R_Add_Exocyclic
"""
)

entry(
    index = 13,
    label = "rad3 <=> PropylindaneRad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14489047644, 's^-1'), n=1.22276, Ea=(57.6245, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for rad3 <=> PropylindaneRad
Level of Theory: CBS-QB3
Number of Rotors included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/intra_R_Add_Exocyclic
"""
)

entry(
    index = 14,
    label = "EthyltetralinRad <=> Ethyltetralin + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59167e+10, 's^-1'), n=0.899322, Ea=(121.108, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for EthyltetralinRad <=> Ethyltetralin + H
Level of Theory: CBS-QB3
Number of Rotors included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission
"""
)

entry(
    index = 15,
    label = "PropylindaneRad <=> Propylindane + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44564e+10, 's^-1'), n=0.96702, Ea=(108.102, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
"""
Calculation for PropylindaneRad <=> Propylindane + H
Level of Theory: CBS-QB3
Number of Rotors included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission
"""
)
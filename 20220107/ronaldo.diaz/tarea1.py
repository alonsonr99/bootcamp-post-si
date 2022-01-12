#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
00000000  =  0      -> everthing off
00000010  =  2      -> Casa
10001001  =  137    -> carro on, gato on, navidad on

multivariable = int(0)
"""
variables = ['Carro','Casa','Perro','Gato','Pez','Moto','Zapato','Navidad']
comparador = int(1)

print("Este programa almacena hasta 8 variables boleanas en un entero\n")
print('''Las variables son:
Carro   ->  on/off  1   ->  00000001
Casa    ->  on/off  2   ->  00000010
Perro   ->  on/off  4   ->  00000100
Gato    ->  on/off  8   ->  00001000
Pez     ->  on/off  16  ->  00010000
Moto    ->  on/off  32  ->  00100000
Zapato  ->  on/off  64  ->  01000000
Navidad ->  on/off  128 ->  10000000
        ''')

multivariable = int(input("Ingresa un numero para encender o apagar variables: ")) 
print("Activaste las variables de salida: {0:08b}\n".format(multivariable))

for x in range (8):
    if(multivariable&comparador):  
        print(variables[x],"is on")
    comparador <<= 1











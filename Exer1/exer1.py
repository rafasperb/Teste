#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:17:13 2018

@author: 08201713
"""

import sys

def tamanho(buffer):
    if(len(buffer)>20):
        return -1
    if(len(buffer)<1):
        return -1
    return len(buffer)

def find(buffer,x):
    if(len(x)>1):
        return -1
    return buffer.find(x)

MAX = 20
MIN = 1
aaa=0
buffer = ''

#buffer = sys.argv[1]
#letra  = sys.argv[2]

#tam = tamanho(buffer)
#print('tamanh do buffer: '+str(tam))
#let = find(buffer,letra)
#print('posição onde a letra foi encontrada: '+str(let))

#if(1 > tam > 20):
 #   print('Cadeia informada esta vazia ou seu tamanho é maior que 20')

#if(let == -1):
#    print('Caractere não pertence a esta cadeia.')

#if(1> len(letra) >1):
#    print('caractere informado de forma errada')    

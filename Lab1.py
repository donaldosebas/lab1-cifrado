'''
  Raul Angel Jimenez 19017
  Donaldo Sebastian Garcia 19683
  Oscar Saravia 19322
  Lab 1 Cifrado de informacion
'''

''' PRIMERA PARTE COMENTADA PARA VER LA SEGUNDA '''
import numpy as np 
import nltk
import re
from Cipher import Cipher
# from Cipher import FuerzaBruta, EfuerzaBruta, DfuerzaBruta

alphabetS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensajeCesar = 'Esto es apenas un texto de prueba.'
mensajeAfin = 'Hola Mundo Soy un Hacker!'
mensajeVigenere = 'Esta es La Prueba del Cifrado Vige!'
probabilidad_teorica = {'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1368, 'F': 0.0069, 'G': 0.0101, 'H': 0.007, 'I': 0.0625, 'J': 0.0044, 'K': 0.0002, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'Ñ': 0.0031, 'O': 0.0868, 'P': 0.0251, 'Q': 0.0088, 'R':0.0687, 'S':0.0798, 'T':0.0463, 'U': 0.0393, 'V': 0.009, 'W': 0.0001, 'X': 0.0022, 'Y': 0.009, 'Z': 0.0052}
cipher = Cipher(alphabetS, probabilidad_teorica)
llave_cesar = 10
llave_afin = [5, 12]
llave_vig = 'palabra'


print('\n El texto que se va a encriptar es: ', mensajeCesar ,'\n')

# Cifrado cesar
e1 = cipher.Ecesar(llave_cesar, mensajeCesar)
print('Encriptacion cifrado cesar: \n',e1,'\n')

d1 = cipher.Dcesar(llave_cesar, e1)
print('Desencriptacion cifrado cesar: \n',d1,'\n')

# Cifrado afin
print('\n El texto que se va a encriptar es: ', mensajeAfin ,'\n')
e2 = cipher.Eafin(llave_afin[0], llave_afin[1], mensajeAfin)
print('Encriptacion cifrado afin: \n',e2,'\n')

d2 = cipher.Dafin(llave_afin[0], llave_afin[1], e2)
print('Desencriptacion cifrado afin: \n',d2,'\n')

# Cifrado vigenere
print('\n El texto que se va a encriptar es: ', mensajeVigenere ,'\n')
e3 = cipher.Evigenere(llave_vig, mensajeVigenere)
print('Encriptacion cifrado vigenere: \n',e3,'\n')

d3 = cipher.Dvigenere(llave_vig, e3)
print('Desencriptacion cifrado vigenere: \n',d3,'\n')

print('\n ==========  DESENCRIPTACION POR FUERZA BRUTA  ========== \n')
# Decifrar por fuerza bruta cesar encription
print('\nFuerza bruta con cesar: \n')
print(cipher.ForceCesar(e1))

# Decifrar por fuerza bruta afin encription
print('\nFuerza bruta con afin: \n')
print(cipher.ForceAfin(e2))

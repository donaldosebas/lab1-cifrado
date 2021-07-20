'''
  Raul Angel Jimenez 19017
  Donaldo Sebastian Garcia 19683
  Oscar Saravia 19322
  Lab 1 Cifrado de informacion
'''

''' PRIMERA PARTE COMENTADA PARA VER LA SEGUNDA 
import numpy as np 
import nltk
import re
from Cipher import Cipher
# from Cipher import FuerzaBruta, EfuerzaBruta, DfuerzaBruta

alphabetS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje = 'Esto es apenas un texto de prueba.'
cipher = Cipher(alphabetS)
llave_cesar = 10
llave_afin = [5, 12]
llave_vig = 'palabra'

print('\n El texto que se va a encriptar es: ', mensaje ,'\n')

# Cifrado cesar
e1 = cipher.Ecesar(llave_cesar, mensaje)
print('Encriptacion cifrado cesar: \n',e1,'\n')

d1 = cipher.Dcesar(llave_cesar, e1)
print('Desencriptacion cifrado cesar: \n',d1,'\n')

# Cifrado afin
e2 = cipher.Eafin(llave_afin[0], llave_afin[1], mensaje)
print('Encriptacion cifrado afin: \n',e2,'\n')

d2 = cipher.Dafin(llave_afin[0], llave_afin[1], e2)
print('Desencriptacion cifrado afin: \n',d2,'\n')

# Cifrado vigenere
e3 = cipher.Evigenere(llave_vig, mensaje)
print('Encriptacion cifrado vigenere: \n',e3,'\n')

d3 = cipher.Dvigenere(llave_vig, e3)
print('Desencriptacion cifrado vigenere: \n',d3,'\n')

'''
from Cipher import Cipher

cipher = Cipher('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
mensaje = 'Esto es apenas un texto de prueba.'
encriptado = 'ÑCDYÑCKZÑWKCEWDÑHDYNÑZBEÑLK'

print(cipher.Probabilities(encriptado))
#print(len(cipher.Probabilities(encriptado)))

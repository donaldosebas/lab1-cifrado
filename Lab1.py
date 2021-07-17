'''import numpy as np 
import nltk
import re
from Cipher import Ecesar, Dcesar, Eafin, Dafin, Evigenere, Dvigenere
from Cipher import FuerzaBruta, EfuerzaBruta, DfuerzaBruta

alphabetS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

dictS = dict([(i, alphabetS[i]) for i in range(len(alphabetS))])'''

from Cipher import Cipher

cipher = Cipher('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

print(cipher.Evigenere('crypto', 'Hola como estas'))

import numpy as np 
import nltk
import re
from Cipher import Ecesar, Dcesar, Eafin, Dafin, Evigenere, Dvigenere
from Cipher import FuerzaBruta, EfuerzaBruta, DfuerzaBruta

alphabetS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

dictS = dict([(i, alphabetS[i]) for i in range(len(alphabetS))])


'''
  Raul Angel Jimenez 19017
  Donaldo Sebastian Garcia 19683
  Oscar Saravia 19322
  Modulo de distintas encriptaciones, Cifrado de informacion
'''
from persistence.persistence import Persistence
import numpy as np 
import nltk
import re

persistenceRepo = Persistence()

class Cipher:
    def __init__(self, abc, prob_teorica):
        self.abc = abc
        self.prob_teorica = prob_teorica

    def Ecesar(self, k, text):
        text = persistenceRepo.filter(text)
        return "".join(self.abc[(self.abc.index(l) + k) % len(self.abc)] for l in text)

    def Dcesar(self, k, abc):
        return "".join(self.abc[(self.abc.index(l) - k) % len(self.abc)] for l in abc)

    def Eafin(self, a, b, text):
        text = persistenceRepo.filter(text)
        return "".join(self.abc[(self.abc.index(l)*a + b) % len(self.abc)] for l in text)

    # algorimto de euclides
    def euclides(self, a, b):  # sourcery skip: remove-unnecessary-else
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.euclides(b % a, a)
            return (g, y - (b // a) * x, x)
            
    # modulo inverso
    def inv_mod(self, a, m):
        g, x, y = self.euclides(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    # decencriptacion afin
    def Dafin(self, a, b, text):
        return "".join(self.abc[(int((self.abc.index(l) - b) * self.inv_mod(a, len(self.abc)))) % len(self.abc)] for l in text)

    # encriptac vigenere
    def Evigenere(self, key, text):
        text = persistenceRepo.filter(text)
        key_array = [key[i % len(key)].upper() for i in range(len(text))]
        return ''.join(
            self.abc[
                (self.abc.index(text[i]) + self.abc.index(key_array[i]))
                % len(self.abc)
            ]
            for i in range(len(text))
        )

    # decencriptacion vigenere
    def Dvigenere(self, key, text):
        key_array = [key[i % len(key)].upper() for i in range(len(text))]
        return ''.join(
            self.abc[
                (self.abc.index(text[i]) - self.abc.index(key_array[i]))
                % len(self.abc)
            ]
            for i in range(len(text))
        )

    def Probabilities(self, text):  # sourcery skip: remove-unreachable-code
        text = persistenceRepo.filter(text)
        tokens = re.findall('.', text)
        freq = nltk.FreqDist(tokens)
        freq = freq.most_common(len(self.abc))
        freq_array = [i[1] for i in freq]
        freq_array = np.array(freq_array)
        p = freq_array / freq_array.sum()
        prob = {l[0]: p[count] for count, l in enumerate(freq)}
        for l in self.abc:
            if l not in prob:
                prob[l] = 0
        return {l: prob[l] for l in self.abc}
        '''print(sorted(prob.items()))
        return prob'''

    def metric(self, teoric, textProb):
        return {l: abs(teoric[l] - textProb[l]) for l in self.abc}

    def ForceCesar(self, text):
        keys = []
        for i in range(len(self.abc)):
            a = self.Dcesar(i, text)
            b = self.Probabilities(a)
            metric = self.metric(self.prob_teorica, b)
            abs_error = sum(value for key, value in metric.items())
            keys.append((i, abs_error))
        best_key_option = sorted(keys, key=lambda x: x[1])[0][0]
        return self.Dcesar(best_key_option, text), best_key_option
    
    def ForceAfin(self, text):
            key = []
            for i in range(len(self.abc)):
                for j in range(len(self.abc)):
                    a = self.Eafin(i, j, text)
                    b = self.Probabilities(a)
                    metric = self.metric(self.prob_teorica, b)
                    abs_error = sum(value for key, value in metric.items())
                    key.append((i, j, abs_error))
            best_key_option = sorted(key, key=lambda x: x[2])[0][0:2]
            return self.Eafin(best_key_option[0], best_key_option[1], text), best_key_option

    def ForceVigenere(self, text):
        keys = []


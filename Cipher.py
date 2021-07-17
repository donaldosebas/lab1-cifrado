'''
  Raul Angel Jimenez 19017
  Donaldo Sebastian Garcia 19683
  Oscar Saravia 19322
  Modulo de distintas encriptaciones, Cifrado de informacion
'''
from persistence.persistence import Persistence

persistenceRepo = Persistence()


class Cipher:
    def __init__(self, abc):
        self.abc = abc

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



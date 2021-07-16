from persistence.persistence import Persistence

persistenceRepo = Persistence()


class Cipher:
    def __init__(self, abc):
        self.abc = abc

    def ecesar(self, k, text):
        text = persistenceRepo.filter(text)
        cipher = ""
        for l in text:
            cipher += self.abc[(self.abc.index(l) + k) % len(self.abc)]
        return cipher

    def afin(self, k, text):
        text = persistenceRepo.filter(text)
        cipher = ""
        for l in text:
            cipher += self.abc[(self.abc.index(l) + k) % len(self.abc)]
        return cipher

    def vigenere(self, k, text):
        text = persistenceRepo.filter(text)
        cipher = ""
        for l in text:
            cipher += self.abc[(self.abc.index(l) + k) % len(self.abc)]
        return cipher

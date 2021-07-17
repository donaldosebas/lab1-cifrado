'''
  Raul Angel Jimenez 19017
  Donaldo Sebastian Garcia 19683
  Oscar Saravia 19322
  Modulo para persistencia de datos y limpieza, Cifrado de informacion
'''
class Persistence:
    def filter(self, text):
        t = text.upper()
        t = t.replace("Á", "A")
        t = t.replace("É", "E")
        t = t.replace("Í", "I")
        t = t.replace("Ó", "O")
        t = t.replace("Ú", "U")
        remover = [' ', '.', ',', ':', ';', '?', '!', '¿', '¡', '"', "'",
                   '(', ')', '[', ']', '{', '}', '\n', '\t', '1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in remover:
            t = t.replace(i, '')
        return t

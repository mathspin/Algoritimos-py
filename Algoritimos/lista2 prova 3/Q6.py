'''Testando um texto. Textando esse texto dessa forma, então testando, ok? 57'''

print("Texto: ")
texto = str(input()).strip()
palavras = texto.count(" ") + texto.count("	") + 1
frases = texto.count(".") + texto.count("?") + texto.count("!")
letras = len(texto) - texto.count(" ") - texto.count("	") - frases - texto.count(",")
print("Letras: "+str(letras)+"   ||   Palavras: "+str(palavras)+"   ||   Frases: "+str(frases))

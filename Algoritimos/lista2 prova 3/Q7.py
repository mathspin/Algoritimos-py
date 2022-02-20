'''Testando um texto. Testando esse texto dessa forma, então testando, ok? 57'''

print("digite o texto: ")
texto = str(input()).strip().lower()
texto = texto.replace(".","")
texto = texto.replace(",","")
texto = texto.replace("?","")
texto = texto.replace("!","")
palavras = texto.split(" ")
total = len(palavras)
i = 0
maior = 0
while i < total:
	n = palavras[i]
	vezes = palavras.count(n)
	if vezes > maior:
		mpalavra = n
		maior = vezes
		apareceu = vezes
	i += 1
print()
print("A palavra que mais repetiu foi '"+str(mpalavra)+"' que apareceu "+str(apareceu)+" vezes!")

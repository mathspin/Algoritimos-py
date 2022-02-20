'''Testando um texto. Testando esse texto dessa forma, então testando, ok? 57'''

print("digite o texto: ")
texto = str(input()).strip().lower()
texto = texto.replace(".","")
texto = texto.replace(",","")
texto = texto.replace("?","")
texto = texto.replace("!","")
texto = texto.replace("'","")
palavras = texto.split(" ")
total = len(palavras)
i = 0
maior = 0
while i < total:
	n = palavras[i]
	if n != "a" and str(n) != "o" and str(n) != "os" and str(n) != "um" and str(n) != "uns" and str(n) != "as":
		vezes = palavras.count(n)
		if vezes > maior:
				mpalavra = n
				maior = vezes
				apareceu = vezes
	i += 1
print()
print("A palavra que mais repetiu foi '"+str(mpalavra)+"' que apareceu "+str(apareceu)+" vezes!")
print(total)
'''Faca um programa que leia um paragrafo e mostre qual a palavra mais frequente no paragrafo, desconsiderando os artigos. Artigos: 'a', 'o', 'as', 'os', 'um' e 'uns'.'''

'''Testando um texto. Testando esse texto dessa forma, então testando, ok? muito bem bem bem bem muito57 a a a a a o o o o as as as as os os os os um um um um uns uns uns uns k k k k k k k k ahsudhasuhdas'''

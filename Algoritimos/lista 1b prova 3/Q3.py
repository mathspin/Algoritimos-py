n = 1
maior = 0
soma = 0
i = 0
media = 1
lista = []
while i >= 0:
	n = float(input("Digite um valor: "))
	if n == 0:
		break
	elif n > maior:
		maior = n
	soma += n
	i += 1
	lista.append(n)
print("Media: "+str(soma/i)+"   _   Maior: "+str(maior))

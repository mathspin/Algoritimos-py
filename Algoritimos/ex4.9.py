i = 0
maior=0
soma = 0
while i < 15:
	n = int(input("digite o codigo: "))
	if n > maior:
		maior = n
	soma += n
	i += 1
print(maior)
print(soma/i)


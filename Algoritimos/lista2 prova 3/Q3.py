n = str(input("Digite o nome: "))
nome = n.split(" ")
i = len(nome)
c = 0
resp = [nome[i-1].upper()+", "]
while c < i-1:
	ni = nome[c].upper()
	resp.append(ni[0]+".")
	c += 1
respf = ''.join(resp)
print(respf)

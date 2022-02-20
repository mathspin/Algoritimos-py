lug = []
i = 1
oc = 0
sel = 0
while i <= 40:
	lug.append(i)
	i+=1
while oc != 40:
	print()	
	print(" - Lugares disponiveis:")
	print()
	print(lug)
	print()
	sel = input("Digite o numero do assento selecionado: ")
	sel = int(sel)-1
	if 0 <= sel <= 39:
		if str(lug[sel]) == "-":
			print()
			print()
			print()
			print(" - Assento ocupado, por favor escolha outro! ")
		else:
			lug[sel] = ("-")
			print()
			print()
			print()
			print(" - Assento confirmado")
			oc += 1
	else:
		print()
		print()
		print()
		print(" - Assento invalido, digite outro valor!")
print()
print("Todos os acentos foram ocupados!")

t = float(input("numero de testes: "))
while t!=0:
	t -= 1
	nt = input()
	n = nt.split(" ")
	ano = 0
	while int(n[0]) <= int(n[1]):
		n[0] = int(n[0]) + (int(n[0])*float(n[2])/100)
		n[1] = int(n[1]) + (int(n[1])*float(n[3])/100)
		ano = ano + 1
		if ano > 100:
			print("mais de um seculo")
			break
	if ano<=100:
		print(str(ano)+" anos")





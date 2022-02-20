x = []
i = 0
ex = 0
while i < 10:
	ex = float(input("digite um valor: "))
	if ex <= 0:
		x.append(1)
	else:
		x.append(ex)
	i+=1
i = 0
while i < 10:
	print("X["+str(i)+"] = "+str(x[i]))
	i += 1

n = float(input("digite um valor: "))
v = []
i = 0
v.append(n)
print("N["+str(i)+"] = "+str(v[i]))
while i < 9:
	n *= 2
	v.append(n)
	i += 1
	print("N["+str(i)+"] = "+str(v[i]))

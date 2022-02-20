v = []
x = float(input("digite um valor: "))
v.append(x)
i = 0
print("N["+str(i)+"] = "+str(v[i]))
while i < 99:
	x = x/2
	v.append(x)
	i+=1
	print("N["+str(i)+"] = "+str(v[i]))

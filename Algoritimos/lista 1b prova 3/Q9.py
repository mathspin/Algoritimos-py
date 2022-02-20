v = []
i = 19
c = 0
while c!=20:
	v.append(c)
	c+=1
while i != -1:
	n = float(input("digite um numero: "))
	v[i] = n
	i-=1
i = 0
while i != 20:
	print("N["+str(i)+"] = "+str(v[i]))
	i+=1

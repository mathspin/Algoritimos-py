v = []
i = 0
while i < 5:
	n = float(input("digite um valor: "))
	if n<=10:	
		f = ("A["+str(i)+"] = "+str(n))
		v.append(f)
	i+=1
print(v)

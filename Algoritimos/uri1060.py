v = input("digite 6 valores separados por espaço ' ': ")
val = v.split(" ")
i=0
p=0
while i <=5:
	if float(val[i]) >= 0:
		p=p+1
	i=i+1
print(str(p)+" valores positivos")

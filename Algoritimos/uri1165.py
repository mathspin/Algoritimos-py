n = int(input("quantidade de testes: "))
while n!=0:
	n+=1
	x = int(input())
	i=0
	c=0
	while x>=i:
		i+=1
		if x%i==0:
			c+=1
	if c==2:
		print(str(x)+" eh primo")
	else:
		print(str(x)+" nao eh primo")

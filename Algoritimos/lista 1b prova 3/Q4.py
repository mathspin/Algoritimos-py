y = []
i = 0
x = float(input("Digite um valor x para ser o multiplicador: "))
while i >= 0:
	n = float(input("Digite um valor:(0 para encerrar) "))
	if n == 0:
		break
	y.append(n*x)
print(y)

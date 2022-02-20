alunos = []
notas = []
n = float(input("Qual o numero de alunos? "))
i = 0
while i < n:
	ni = input("Qual o nome do aluno "+str(i+1)+" ?")
	alunos.append(ni)
	ni = float(input("Qual a nota desse aluno? "))
	notas.append(ni)
	i += 1
i = 0
while i <= n:
	print(str(alunos[i])+" - "+str(notas[i]))
	i +=1

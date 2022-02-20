alunos = []
notas = []
frequencia = []
aprovamento = []
n = float(input("Qual o numero de alunos? "))
i = 0
while i < n:
	ni = input("Qual o nome do aluno "+str(i+1)+" ? ")
	alunos.append(ni)
	ni = float(input("Qual a nota desse aluno? "))
	notas.append(ni)
	ni = float(input("Qual a frequencia desse aluno? "))
	frequencia.append(ni)
	if float(notas[i]) >= 7 and float(frequencia[i]) >= 75:
		aprovamento.append("Aprovado")
	else:
		aprovamento.append("Reprovado")
	i += 1
i = 0
while i < n:
	print()
	print(str(alunos[i])+" -  n: "+str(notas[i])+" -  f: "+str(frequencia[i])+"% _   "+str(aprovamento[i]))
	i +=1

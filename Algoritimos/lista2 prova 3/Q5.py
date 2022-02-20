d = str(input("Digite uma data no formato 'DD/MM/AAAA': "))
data = (d.split("/"))
resp = [data[0]+" de "]
if data[1] == "01":
	data[1] = "Janeiro de "
elif data[1] == "02":
	data[1] = "Fevereiro de "
elif data[1] == "03":
	data[1] = "Março de "
elif data[1] == "04":
	data[1] = "Abril de "
elif data[1] == "05":
	data[1] = "Maio de "
elif data[1] == "06":
	data[1] = "Junho de "
elif data[1] == "07":
	data[1] = "Julho de "
elif data[1] == "08":
	data[1] = "Agosto de "
elif data[1] == "09":
	data[1] = "Setembro de "
elif data[1] == "10":
	data[1] = "Outubro de "
elif data[1] == "11":
	data[1] = "Novembro de "
elif data[1] == "12":
	data[1] = "Dezembro de "
resp.append(data[1])
resp.append(data[2])
print()
print("Você nasceu em: "+str(''.join(resp)))

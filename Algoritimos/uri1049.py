vi = input("vertebrado ou invertebrado? ")
if vi == "vertebrado":
	am = input("ave ou mamifero? ")
	if am == "ave":
		co = input("carnivoro ou onivoro? ")
		if co == "carnivoro":
			print("aguia")
		else:
			print ("pomba")
	else:
		oh = input("onivoro ou herbivoro? ")
		if oh == "onivoro":
			print ("homem")
		else:
			print ("vaca")
else:
	ia = input("inseto ou anelideo? ")
	if ia == "inseto":
		hh = input("hematofago ou herbivoro? ")
		if hh == "hematofago":
			print("pulga")
		else:
			print("lagarta")
	else:
		ho = input("heatofago ou onivoro? ")
		if ho == "hematofago":
			print("sanguessuga")
		else:
			print("minhoca")

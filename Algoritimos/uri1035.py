a = input("insira um valor para 'A': ")
b = input("insira um valor para 'B': ")
c = input("insira um valor para 'C': ")
d = input("insira um valor para 'D': ")
if b > c and d > a and c+d > a+b and int(c) >= 0 and int(d) >= 0 and int(a)%2 == 0:
	print ("valores aceitos")
else:
	print ("valores nao aceitos")

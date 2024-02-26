def fun_c(ia: int) -> bool:
	return ia % 2 == 0

ba = fun_c(5)
if ba == True:
	print("Liczba parzysta")
else:
	print("Liczba nieparzysta")
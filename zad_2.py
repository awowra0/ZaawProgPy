def fun_a(a, b, c, d, e):
	print(f"{a} {b} {c} {d} {e}")

def fun_b1(B):
	BB = []
	for i in B:
		BB.append(i*2)
	return BB

def fun_b2(B):
	return [k*2 for k in B]

def fun_c(C):
	for j in C:
		if j%2==0:
			print(f"{j}")

def fun_d(D):
	for l in D[1::2]:
		print(l)


fun_a("Adam","Adam","Adam","Aneta","Al")
print(fun_b1([0,1,2,3,4]))
print(fun_b2([1,2,3,4,5]))
fun_c(range(10))
fun_d(range(10))

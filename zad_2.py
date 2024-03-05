def fun_a(A: list):
    for i in A:
        print(i)


def fun_b1(B: list) -> list:
    BB = []
    for i in B:
        BB.append(i * 2)
    return BB


def fun_b2(B: list) -> list:
    return [k * 2 for k in B]


def fun_c(C: list):
    for j in C:
        if j % 2 == 0:
            print(j)


def fun_d(D):
    for la in D[1::2]:
        print(la)


fun_a("Adam", "Adam", "Adam", "Aneta", "Al")
print(fun_b1([0, 1, 2, 3, 4]))
print(fun_b2([1, 2, 3, 4, 5]))
fun_c(range(10))
fun_d(range(10))

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

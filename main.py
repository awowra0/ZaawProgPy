import func.funcs as fun
def main(num=4, A=range(5)):
    if num == 1:
        fun.fun_a(A)
    elif num == 2:
        print(fun.fun_b1(A))
    elif num == 3:
        print(fun.fun_b2(A))
    elif num == 4:
        fun.fun_c(A)
    elif num == 5:
        fun.fun_d(A)


if __name__ == "__main__":
    main()

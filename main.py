import zadania as fun


def main(num=4, A=range(5)):
    if num == 1:
        fun.zad_1(A)
    elif num == 2:
        print(fun.zad_2(A))
    elif num == 3:
        print(fun.zad_3(A))
    elif num == 4:
        fun.zad_4(A)
    elif num == 5:
        fun.zad_5(A)
    elif num == 6:
        fun.zad_6()
    elif num == 7:
        fun.zad_7()
    elif num == 8:
        fun.zad_8()


if __name__ == "__main__":
    main()

import zadania.zad_1
import zadania.zad_2
import zadania.zad_3
import zadania.zad_4
import zadania.zad_5
import zadania.zad_6
import zadania.zad_7
import zadania.zad_8


def main(num=4, A=[0, 1, 2, 3], B=[2, 3, 4, 5], a=2, b=3, c=4, S="Berlin"):
    if num == 1:
        print(zadania.zad_1.fun_1(a, b))
    elif num == 2:
        print(zadania.zad_2.fun_2(a, b))
    elif num == 3:
        zadania.zad_3.fun_3(a)
    elif num == 4:
        print(zadania.zad_4.fun_4(a, b, c))
    elif num == 5:
        print(zadania.zad_5.fun_5(A, a))
    elif num == 6:
        print(zadania.zad_6.fun_6(A, B))
    elif num == 7:
        zadania.zad_7.fun_7()
    elif num == 8:
        zadania.zad_8.fun_8(S)


if __name__ == "__main__":
    main()

import zadania.zad_1
import zadania.zad_2
import zadania.zad_3


def main(num=1):
    if num == 1:
        zadania.zad_1.fun_1()
    elif num == 2:
        zadania.zad_2.fun_2()
    elif num == 3:
        zadania.zad_3.fun_3()


if __name__ == "__main__":
    main()

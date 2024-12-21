from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg
def main():
    while True:
        print("\nСписок проблем")
        print("1- факторіал")
        print("2-квадарт")
        print("3- куб")
        print("4-корінь")
        print("5-кубічний корінь")
        print("6- логарифм")
        print("7- наткральний логарифм")
        print("8- десятковий ")
        print("0 - вихід")
        try:
            choice= int(input("\nвведіть номер проблеми"))
            if choice== 0:
                break 
            if choice== 1:
                n = int(input("введіть число"))
                result = fact(n)
                print(result)
            elif choice== 2:
                x= float(input("введіть число "))
                result= exp2(x)
                print(result)
            elif choice== 3:
                x= float(input("введіть число"))
                result= exp3(x)
                print(result)
            elif choice == 4:
                x= float(input("введіть число"))
                result= root2(x)
                print(result)
            elif choice== 5:
                x= float(input("введіть число"))
                result= root3(x)
                print(result)
            elif choice== 6:
                a = float(input("основа логарифма:"))
                b = float(input("логафирм числа:"))
                result= log(a, b)
                print(result)
            elif choice== 7:
                b= float(input("введіть додатнє число"))
                result= ln(b)
                print(result)
            elif choice== 8:
                b= float(input("введіть додатнє число"))
                result= lg(b)
                print(result)  
            else:
                print("вводьте число з діапазону 0-8")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()


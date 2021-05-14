# 45*3=555, 56+9=77, 56/6=4
def faultycalculator():
 num1=int(input('enter the first number: '))
 num2=int(input('enter the second number: '))
 op=input('enter the operator: ')

 if num1 == 56 and num2 == 9 and op == '+':
    print(77)
 elif op=='+':
    print(num1 + num2)
 elif num1 == 43 and num2 == 3 and op == '*':
        print(555)
 elif op=='*':
     print(num1 * num2)
 elif num1 == 56 and num2 == 7 and op == '/':
    print(44)
 elif op=='/':
    print(num1 / num2)
 elif op=="-":
     print(num1-num2)
 else:
    print(num1 % num2)

faultycalculator()
#Enter the first num, the second num and the operation
#List of operation: +, -, /, *, mod, pow, div
print('Enter the numbers and operation:')
a=float(input())
b=float(input())
Op=str(input())
if Op=='+':
  print(a+b)
elif Op=="-":
  print(a-b)
elif Op=="/":
  if b==0:
    print("Деление на 0!")
  else:
    print(a/b)
elif Op=="*":
  print(a*b)
elif Op=="mod":
  if b==0:
    print("Деление на 0!")
  else:
    print(a%b)
elif Op=="pow":
  print((a)**b)
elif Op=="div":
  if b==0:
    print("Деление на 0!")
  else:
    print(a//b)
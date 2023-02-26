#Enter the str with six numbers
#Program finds sum for first three numbers and second three numbers
#Program compares this pair of numbers and says the type of ticket
print('Enter the six numbers on your ticket:')
n=int(input())
n1=(n%1000000)//100000
n2=(n%100000)//10000
n3=(n%10000)//1000
n4=(n%1000)//100
n5=(n%100)//10
n6=n%10
if (n1+n2+n3)==(n4+n5+n6):
  print('Lucky')
else:
  print('Ordinary')
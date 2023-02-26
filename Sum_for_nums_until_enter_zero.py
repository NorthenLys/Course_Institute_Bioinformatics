#Program reads numbers from the console (one per line) until the sum of the entered numbers is 0
#Immediately after that program prints the sum of the squares of all the numbers read
print('Enter the number:')
s=0
s2=0
while True:
  a=int(input())
  s+=a
  b=a*a
  s2+=b
  if s==0:
    break
print(s2)
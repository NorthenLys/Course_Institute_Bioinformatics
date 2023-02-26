#Enter the three integers
#Program output: max, min, other
print('Enter the three numbers:')
a=int(input())
b=int(input())
c=int(input())
if b<=a>=c and a>=b>=c and a>=c<=b:
  print(a)
  print(c)
  print(b)
elif a<=b>=c and b>=a>=c and a>=c<=b:
  print(b)
  print(c)
  print(a)
elif b<=c>=a and c>=a>=b and c>=b<=a:
  print(c)
  print(b)
  print(a)
elif a<=b>=c and b>=c>=a and b>=a<=c:
  print(b)
  print(a)
  print(c)
elif b<=a>=c and a>=c>=b and a>=b<=c:
  print(a)
  print(b)
  print(c)
elif b<=c>=a and c>=b>=a and c>=a<=b:
  print(c)
  print(a)
  print(b)


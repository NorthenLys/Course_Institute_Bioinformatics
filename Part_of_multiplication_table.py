#Input: four numbers each in it's own row
#Output: part of multiplication table for integers in segment[a;b] * integers in segment[c;d]
#Rules:
#1.Numbers are integers
#2.Numbers are not more then 10
#3. a≤b, c≤d
print('Enter four numbers:')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(' ',end='\t')
if c<=d:
  for j in range(c,d+1):
    print(j,end='\t')
print(' ')
if a<=b:
  for i in range(a,b+1):
    print(i, end='\t')
    for k in range(c,d+1):
      print(k*i,end='\t')
    print(' ')

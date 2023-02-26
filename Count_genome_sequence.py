#Program calculates the percentage of characters G (guanine) and C (cytosine) in the input string
# Program are not case sensitive
print('Enter the genome:')
s=input()
k=0
for i in s:
  k+=1
x=s.count('g')
y=s.count('c')
i=s.count('g'.upper())
l=s.count('c'.upper())
o=x+i
t=y+l
fin_count=o+t
percent=(fin_count/k)*100
print(float(percent))

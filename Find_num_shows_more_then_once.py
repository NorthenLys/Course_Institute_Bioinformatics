# Input: list of numbers on one line
# Output: values in the list that occur more than once
# Rules:
# 1.Output numbers must not be repeated.
# 2.The output order can be arbitrary.
print('Enter the list of numbers:')
s=[int(i) for i in input().split()]
ordered_s=sorted(s)
news=[]
n=0
for i in ordered_s:
  if n<len(ordered_s)-1 and ordered_s[n]==ordered_s[n+1] and ordered_s[n]!=ordered_s[n-1]:
   news+=[i]
  n+=1
if ordered_s[0]==ordered_s[-1] and len(ordered_s)>1:
  news+=[ordered_s[0]]
print(*news)

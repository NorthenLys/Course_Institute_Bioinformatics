#Input:list of numbers, some number from list
#Output: all positions for some number in the input list
#Rules:
#1.Positions are numbered from zero
#2.If the number is not found in the list, output: "Not found"
#3.Positions displayed in one line, in ascending absolute value
print('Enter the list, then enter the one number:')
lst=list(input().split())
x=int(input())
ind=[]
n=-1
for i in lst:
  n+=1
  if int(i) == x:
    ind+=[n]
print(*ind,end=' ')
if len(ind)==0:
  print('Not found')
#Input: list of integers
#Def remove from list odd numbers, then divides even numbers by two
#Output:changed list of integers
print('Enter the list of integers:')
l=list(input())
def modify_list():
  copy_l = l
  odd=[]
  even=[]
  for i in copy_l:
    if int(i)%2==1:
      odd+=[i]
    else:
      even+=[int(i)//2]
  copy_l.clear()
  copy_l+=even
  return print(copy_l)
modify_list()
#Enter the positive integer for number of coders in the room
#Program counts coders and says how much coders we have. Program put the normal ending for word 'программист'
#Work with integers in the interval 0 ≤ n ≤ 1000
print('How much coders do you see in the room?')
n=int(input())
if n!=0 and n%10==1:
  if n%100==11:
    print(n,'программистов')
  else:
    print(n,'программист')
elif 0<n<=4 and n!=0 and n!=1:
  print(n,'программиста')
elif n%10==2 or n%10==3 or n%10==4:
  if n%100==12 or n%100==13 or n%100==14:
    print(n,'программистов')
  else:
    print(n,'программиста')
elif n!=0 and n!=1 and 4<n>=5:
  print(n,'программистов')
elif n==0:
  print(n,'программистов')
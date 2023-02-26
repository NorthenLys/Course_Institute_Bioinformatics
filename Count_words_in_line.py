#Input:words separated by space
#Output:a word and the number of repetitions of it in a line
#Rules:
#1.The order of output of words is arbitrary
#2.A unique word displayed only once
#3.Words are considered case insensitive
print('Enter the sentence:')
a = input().lower().split()
d={}
for i in a:
  d.update({i:[a.count(i)]})
for key,value in d.items():
  print(key,' ',*value)


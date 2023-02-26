#Algorithm compresses repeated characters in a string
#Groups of identical characters of the original string are replaced by this character
#and the number of repetitions of it in this position of the string
#Encoding are case-sensitive
print('Enter the DNA:')
s=input()
ans=s[0]
k=0
for i in s:
  if i==ans[len(ans)-1]:
    k+=1
  else:
    ans=ans+str(k)+str(i)
    k=1
ans=ans+str(k)
print(ans)
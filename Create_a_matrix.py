#Input: matrix as a sequence of rows.
#After the last row of the matrix comes a row containing only the string end
#Ex.of input:
#9 5 3
#0 7 -1
#-5 2 9
#end
#Output:matrix of the same size, in which each element in positions i, j is equal
# to the sum of the elements of the first matrix in positions (i-1, j), (i+1, j), (i, j-1), (i, j+ 1).
#Rules:
#1.For extreme characters, the neighboring element is on the opposite side of the matrix.
#2.In the case of a single row/column, the element is itself a neighbor in the corresponding direction.
print('Enter the matrix. Dont forget about end:')
b=[]
while True:
  a=list(input().split())
  if "".join(a)=="end":
    break
  b+=[[int(x) for x in a]]
c=[[0 for j in range(0, len(b[0]))] for i in range(0,len(b))]
for i in range(0,len(b)):
  for j in range(0, len(b[0])):
    if i==len(b)-1 and j==len(b[0])-1:
      c[i][j]= b[i-1][j]+b[0][j]+b[i][j-1]+b[i][0]
    elif i==len(b)-1:
      c[i][j]= b[i-1][j]+b[0][j]+b[i][j-1]+b[i][j+1]
    elif j==len(b[0])-1:
      c[i][j]= b[i-1][j]+b[i+1][j]+b[i][j-1]+b[i][0]
    else:
      c[i][j]= b[i-1][j]+b[i+1][j]+b[i][j-1]+b[i][j+1]
for i in range(len(c)):
  print(*c[i])
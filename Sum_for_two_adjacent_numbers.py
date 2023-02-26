#Input:list of numbers in one line
#Output:for each element of this list print the sum of it's two neighbors
#Rules:
#1.For list elements that are extreme, one of the neighbors is the element located at the opposite end of this list
#2.If only one number came to the input, program output it
#3.The output contain a single line with the numbers of the new list separated by a space
print('Enter the list of numbers:')
a = [int(i) for i in input().split()]
b = a
ans = []
n = 0
if len(a) == 1:
    print(*a)
else:
    for i in b:
        if n + 1 >= len(a):
            break
        ans += [a[n - 1] + a[n + 1]]
        n += 1
    ans += [a[-2] + a[0]]
print(*ans)

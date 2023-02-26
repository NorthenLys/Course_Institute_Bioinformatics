#Input: positive integer
#Output: Based on the input integer program shows count of elements of the sequence
#Rules:
#1.Number is repeated as many times as it's value
#2.Output: a sequence of numbers written with a space in one line
print('Enter the positive integer:')
n = int(input())
k = []
for i in range(1, n + 1):
    k += [i] * i
print(*k[:n], end=' ')
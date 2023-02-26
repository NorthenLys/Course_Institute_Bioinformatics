#Enter the type of figure and parameters for find S for figure
#The types: triangle, rectangle, circle
#The params for the figures: trangle (a,b,c - the lenght), rectangle(a,b - the lenght), circle (r - radius)
print('Enter the type of figure and parameters:')
F=str(input())
if F=='треугольник' or F=='trangle' or F=='t' or F=='т':
    a=int(input())
    b=int(input())
    c=int(input())
    p=(a+b+c)/2
    S=((p*(p-a)*(p-b)*(p-c))**0.5)
    print(float(S))
elif F=='прямоугольник'or F=='rectangle' or F=='r' or F=='п':
    a=int(input())
    b=int(input())
    S=a*b
    print(float(S))
elif F=='круг' or F=='circle' or F=='c' or F=='к':
    r=int(input())
    π=3.14
    S=π*((r)**2)
    print(float(S))
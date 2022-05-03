def makefib(n):
    fib = []
    for i in range(0,n):
        if i == 0 or i == 1:
            fib.append(i)
        else:
            fib.append(fib[i-2]+fib[i-1])
    return fib
print(makefib(10))

def inner_product(x,y):
    sum = 0
    for i in range(0,len(x)):
        sum +=x[i]*y[i]
    return sum

inner_product([2,3],[4,5])

a = 5
b = 2
wa = a + b
sa = a - b
seki = a * b


a = int(input('num1'))
b = int(input('num2'))
c = int(input('num3'))

if a > b :
    temp = 1
    a = b
    b = temp
if a > c :
    temp = a
    a = c 
    c = temp

if b > c :
    temp = b 
    b = c
    c = temp
print(a,b,c,sep = '')

def solve_f(a,b,c):
    D = (b*b -4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('解は{0},{1}'.format(x_1,x_2))


print(solve_f(1,1,-6))

num = 36 
divisors = []
for i in range(1,num + 1):
    if num % i == 0:
        divisors.append(i)
    print(divisors)


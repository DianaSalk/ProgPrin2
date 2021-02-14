# A список квадратов
a=int(input())
n=1
k=n
m=''
while k<=a:
    s=str(k)
    m=m+" "+s
    n=n+1
    k=n*n
m=m.strip()
print(m)

# B минимальный простой делитель
def prime_f(n):
    if n%2 == 0: return 2
    i = 3
    while n%i != 0 and i*i <= n:
        i+= 2
    if i*i <= n: return i
    return n
n=int(input())
print(prime_f(n))

# C список степеней двойки
n=int(input())
s=1
while s<=n:
    print(s, end=' ')
    s*=2

# D точная степень двойки
n=int(input())
s=1
flag=True
while s<=n:
    if s==n:
        print('YES')
        flag=False
        break;
    else:
        s*=2
if(flag):
    print('NO')

# E двоичный логарифм
n=int(input())
s, count = 2,0
if n==1:
    print(0)
else:
    while s<n:
        s*=2
        count+=1
    print(count+1)
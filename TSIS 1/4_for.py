# A ряд 1
a=int(input())
b=int(input())
c=str(a)
for y in range(a+1, b+1):
  x=str(y)
  c=c+" "+x
print(c)

# B ряд 2
a=int(input())
b=int(input())

if(b>a):
c=str(a)
for y in range(a+1, b+1):
   x=str(y)
   c=c+" "+x
print(c)
else:
c=str(a)
for y in range(a-1, b-1, -1):
   x=str(y)
   c=c+" "+x
print(c)

# C ряд 3
a = int(input())
b = 10 ** (a - 1)
a = 10 ** a

y = str(a - 1)
for x in range(a - 3, b - 1, -2):
    c = str(x)
    y = y + " " + c
print(y)

# D сумма квадратов
a=int(input())
sum=0
for x in range(1, a+1):
    sum=sum+x**2
print(sum)

# E сумма кубов
a=int(input())
sum=0
for x in range(1, a+1):
    sum=sum+x**3
print(sum)
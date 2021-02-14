# A длина отрезка
def dis(x,y,a,b):
    print((((x-a)**2+(y-b)**2)**.5))
x=int(input())
y=int(input())
a=int(input())
b=int(input())
dis(x,y,a,b)

# B минимум 4 чисел
def minim(x,y,a,b):
    print(min(x,y,a,b))
x=int(input())
y=int(input())
a=int(input())
b=int(input())
minim(x,y,a,b)

# C принадлежит ли точка квадрату 1
def IsPointInSquare(x, y):
    return(x*y)

x=float(input())
y=float(input())
if IsPointInSquare(x, y)>1 or IsPointInSquare(x, y)<-1:
    print('NO')
else:
    if (x>=-1 and x<=1) and (y>=-1 and y<=1):
        print('YES')
    else:
        print('NO')

# D принадлежит ли точка квадрату 2
x=float(input())
y=float(input())
if abs(y)<=1-abs(x) and abs(x)<=1:
    print('YES')
else:
    print('NO')

# E принадлежит ли точка кругу
x=float(input())
y=float(input())
a=float(input())
b=float(input())
r=float(input())
dis=((x-a)**2+(y-b)**2)**.5
if dis<=r:
    print('YES')
else:
    print('NO')
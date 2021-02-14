# A дробная часть
a=float(input())
print(a%1)

# B первая цифра после точки
x = float(input())
a=((x%1)*100)//10
print(int(a))

# C округление по российским правилам
x = float(input())
y=(x%1)*100
if(y>=50):
  print(int(x)+1)
else:
  print(int(x))

# D площадь треугольника
import math
a = float(input())
b = float(input())
c = float(input())
p=(a+b+c)/2
x=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(x)

# E Часы 1
import math
a = float(input())
b = float(input())
c = float(input())
s=b*60+c
cc=a+s/3600
print(cc*30)
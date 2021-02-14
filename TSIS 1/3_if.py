# A максимум двух чисел
a=int(input())
b=int(input())
if(a>=b):
  print(a)
else:
  print(b)

# B какое число больше?
a=int(input())
b=int(input())
if(a>b):
  print(1)
elif(a<b):
  print(2)
else:
  print(0)

# C знак числа
a=int(input())
if(a>0):
  print(1)
elif(a<0):
  print(-1)
else:
  print(0)

# D високосный год
a=int(input())
if(a%4==0 and a%100!=0):
  print("YES")
elif(a%400==0):
    print("YES")
else:
  print("NO")

# E максимум трех чисел
a=int(input())
b=int(input())
c=int(input())
if(a>b):
  if(b>=c):
    print(a)
  else:
    if(a>c):
      print(a)
    else:
      print(c)
else:
  if(c>=b):
    print(c)
  else:
    print(b)
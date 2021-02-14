# A делаем срезы
a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[:-2])
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[::-2])
print(len(a))

# B количество слов
a=input()
print(a.count(" ")+1)

# C две половинки
import math
a=input()
b=math.ceil(len(a)/2)
k=math.floor(len(a)/2)
print(a[b:]+a[:b])

# D переставть два слова
a=input()
b=" "
k=a.find(b)
print(a[k+1:],a[:k+1])

# E первое и последнее вхождение
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

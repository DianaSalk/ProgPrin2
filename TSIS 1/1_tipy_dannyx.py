# A степень двойки
print(2**179)

# B факториал
sum = 1
for x in range(1, 21):
    sum = sum * x
print(sum)

# C гипотенуза
import math
x=179
y=971
sum=math.sqrt(x**2+y**2)
print(sum)
# D ряд лейбница
n=1
sum=0
for i in range(10):
    if i%2==0:
        sum=sum+4/n
    else:
        sum=sum-4/n
    n=n+2
print(sum)

# E дзета-функция
import math

sum = 0
for x in range(1, 11):
    sum = sum + 1 / (x * x)

sum = math.sqrt(sum * 6)
print(sum)

# F сто раз букву А
print('A'*100)

# G сто раз Пайтон
print('Python'*100)

# H корень степени 10
m=int(str(179**10)*4)
print(m**.1)

# I квадрат
m=int(str(179)*50)
print(m**2)
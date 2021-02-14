# A  вывести только четные индексы
n=input().split()
[print(n[i],end=' ') for i in range(len(n)) if i%2==0]

# H первое неотрицательное число
n=input().split()
n=[int(i) for i in n if int(i)>0]
print(min(n))

# M reverse
n=input().split()
n.reverse()
for i in n:
    print(int(i), end=' ')

# №3850 Нули вправо
n=input().split()
l=len(n)
n=[int(i) for i in n if int(i)!=0]
for i in range(l-len(n)):
    n.append('0')
for i in n:
    print(int(i), end=' ')

# Z большой сдвиг
n=input().split()
k=int(input())
k=k%len(n)
if k>0:
    k = len(n) - k
else:
    k=-k
for i in range(k, len(n)):
    print(n[i], end=' ')
for i in range(0, k):
    print(n[i], end=' ')

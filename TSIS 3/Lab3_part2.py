
# A количество различных чисел
print(len(set(input().split())))

# B количество совпадающих
print(len(set(input().split()) & set(input().split())))

# C список совпадающих
z=list(set(input().split()).intersection(set(input().split())))
for i in sorted(z):
    print(int(i), end=' ')
# E кубики
a,b=input().split()
al=set()
bl=set()
for i in range(int(a)):
    al.add(input())
for i in range(int(b)):
    bl.add(input())
print(len(al & bl))
print(*sorted(al&bl, key=int))
print(len(al)-len(al & bl))
print(*sorted(al^(al&bl), key=int))
print(len(bl)-len(al & bl))
print(*sorted(bl^(al&bl), key=int))

# L словарь синонимов
d={}
n=int(input())
for i in range(n):
    w1,w2=input().split()
    d[w1]=w2
word=input()
if d.get(word):
    print(d.get(word))
else:
    for key, value in d.items():
        if word == value:
            print(key)
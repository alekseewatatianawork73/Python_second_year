mn = 2000
mx = -2000
x = int(input())
while x != 0:
    if x % 2 == 0 and x < mn:
        mn = x
    if x % 2 != 0 and x > mx:
        mx = x
    x = int(input())
print(mn, mx)


count = 0
summ = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x > 100:
        count += 1
    elif x < 100:
        summ += x
print(count, summ)


a = [int(x) for x in input().split()]
b = list(map(int, input().split()))
c = [] # c = set()
for x in a:
    if x in b and x not in c:
        c.append(x)
c.sort()
print(*c)

a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.intersection(b) # c = a & b
print(*c)


a = [x.lower() for x in input() if x.isalpha()]
b = [x.lower() for x in input() if x.isalpha()]
# print('YES' if sorted(a) == sorted(b) else 'NO')
a.sort()
b.sort()
print("YES" if a == b else "NO")


d1, d2 = {}, {}
for c in input().lower():
    if c.isalpha():
        d1[c] = d1.get(c, 0) + 1
for c in input().lower():
    if c.isalpha():
        d2[c] = d2.get(c, 0) + 1
print(d1, d2)
print('YES' if d1 == d2 else 'NO')


n = int(input())
m = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or j == n // 2 or i + j == n - 1:
            m[i][j] = 1
for i in range(n):
    print(*m[i])

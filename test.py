a,m,d,n = map(int, input().split())

y = a
for i in range(n-1):
    y = (y * m ) + d

print(y)

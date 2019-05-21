def gcd(a, b):
    while(b>0):
        a, b = b, a%b
    return a

T = int(input())
for t in range(1, T+1):
    N, L = input().split()
    N, L = int(N), int(L)
    x = input().split()
    print("Case #%d: "%t, end="")
    x = [int(n) for n in x]
    p = [0]*(L+1)
    k = 1
    while(x[k-1]==x[k]):
        k += 1
    p[k] = gcd(x[k-1], x[k])
    for i in range(k-1, -1, -1):
        p[i] = x[i]//p[i+1]
    for i in range(k+1, L+1):
        p[i] = x[i-1]//p[i-1]
    l = list(set(p))
    l.sort()
    d = {}
    for i in range(26):
        d[l[i]] = chr(65+i)
    print(''.join(map(d.get, p)))

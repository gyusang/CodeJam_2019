T = int(input())
for x in range(1, T+1):
    a = list(input())
    b = ['0']*len(a)
    print("Case #%d: "%x, end="")
    for i in range(len(a)):
        if a[i] == '4':
            b[i] = '1'
            a[i] = '3'
    print(''.join(a), end=" ")
    print(''.join(b))

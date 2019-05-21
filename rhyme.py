def equals(s, l, t):
    if len(s) <= l:
        return False
    if s[l] == t:
        return True
    else:
        return False

T = int(input())
for t in range(1, T+1):
    N = int(input())
    W = ['']*N
    for n in range(N):
        W[n] = input()[::-1]
    W.sort()
    answer = 0
    stage = 0
    start = [0]*51
    target = ['\0']*51
    for i in range(N):
        for s in range(stage+1):
            if not equals(W[i], s, target[s]):
                break
        for r in range(stage-1, s-1, -1):
            if i-start[r] >= 2:
                answer += 2
                for back in range(r):
                    start[back] += 2
        stage = s
        for r in range(stage, len(W[i])):
            target[r] = W[i][r]
            start[r] = i
        stage = len(W[i])
    for r in range(stage - 1, -1, -1):
        if N - start[r] >= 2:
            answer += 2
            for back in range(r):
                start[back] += 2
    print("Case #%d: %d"%(t, answer))




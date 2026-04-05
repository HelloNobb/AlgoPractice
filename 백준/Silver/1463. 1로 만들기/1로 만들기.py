import sys
input = sys.stdin.readline

N = int(input())

def make_1(N):
    if N == 1:
        return 0
    
    DP = [-1]*(N+1)
    DP[N] = 0
    
    for i in range(N,0,-1):
        # if DP[i] != -1:
        #     continue
        
        if i*3 <= N and DP[i*3] != -1:
            candy1 = DP[i*3] + 1
            DP[i] = candy1 if DP[i] == -1 else min(DP[i], candy1)
        if i*2 <= N and DP[i*2] != -1:
            candy2 = DP[i*2] + 1
            DP[i] = candy2 if DP[i] == -1 else min(DP[i], candy2)
        if i+1 <= N and DP[i+1] != -1:
            candy3 = DP[i+1] + 1
            DP[i] = candy3 if DP[i] == -1 else min(DP[i], candy3)
        
    
    return DP[1]

print(make_1(N))
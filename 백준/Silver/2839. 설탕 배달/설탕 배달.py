n = int(input())

DP = [-1]*(n+1)

def dp(N):
    if (N == 4):
        return -1
    
    DP[3] = 1
    if N == 3:
        return DP[3]
    DP[5] = 1
    for i in range(3, N+1):
        
        if i-5 >= 0 and DP[i-5] != -1:
            DP[i] = DP[i-5]+1
        elif i-3 >= 0 and DP[i-3] != -1:
            DP[i] = DP[i-3]+1
        #print(f"DP[{i}] = {DP[i]}")
    return DP[N]

print(dp(n))
# Recursive
def rLCS(s1,s2):
    memo = {}
    return _rLCS(s1,s2,0,0,memo)

def _rLCS(s1,s2,i,j,memo):
    if i == len(s1) or j == len(s2):
        return 0
    
    pos = (i,j)
    if pos in memo: return memo[pos]
    
    if s1[i] == s2[j]:
        memo[pos] = 1 + _rLCS(s1,s2,i+1,j+1, memo)
    else:
        memo[pos] = max(_rLCS(s1,s2,i+1,j,memo),_rLCS(s1,s2,i,j+1,memo))

    # print (f'pos = {pos} -> {memo[pos]}')
    return memo[pos]

def tLCS(s1,s2):
    n,m = len(s1),len(s2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    
    return dp[0][0]

if __name__ == '__main__':
    s1 = 'abcde'
    s2 = 'ceghf'
    # s1 =''
    # s2 =''

    print(rLCS(s1,s2))
    print(tLCS(s1,s2))
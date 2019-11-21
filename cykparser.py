NMax = 400
RMax = 30

dp = [[[0 for i in range(RMax)] for i in range(NMax)] for i in range(NMax)]
R = [None]

mp = {}
mp['S'] = 1
mp['A'] = 2
mp['T'] = 3
mp['B'] = 4
mp['C'] = 5

R.append([["T", "A"], ["B", "A"], ["A", "B"], ["b"]])
R.append([["A", "C"], ["a"]])
R.append([["A", "B"]])
R.append([["b"]])
R.append([["a"]])

inp = "a"*1000
if(len(inp) >= 1000):
    print("Bacot")
    exit(0)
elif(len(inp) == 0):
    print("Accepted")
    exit(0)

n = len(inp) #panjang input
m = 5 #banyaknya terminal

for s in range(1, n+1):
    for v in range(1, m+1):
        for e in R[v]:
            if(e[0] == inp[s - 1]):
                dp[1][s][v] = True
                break

for l in range(2, n+1):
    for s in range(1, (n-l+2)):
        for p in range(1, l):
            for a in range(1, m+1):
                for e in R[a]:
                    if(len(e) != 1):
                        b = mp[e[0]]
                        c = mp[e[1]]
                        if (dp[p][s][b] and dp[l-p][s+p][c]):
                            dp[l][s][a] = True
                            break

if(dp[n][1][1]):
    print("Accepted")
else :
    print("Syntax Error")
def CYKParser(inp, CNF):
    # Init
    n = len(inp) #panjang input
    m = len(CNF) #banyaknya terminal

    dp = [[[0 for i in range(m + 1)] for i in range(n + 1)] for i in range(n + 1)]
    R = [None] * (m + 1)
    mp = {}

    # Append rule
    # start_time = time.time()
    for i, variable in enumerate(CNF):
        mp[variable] = i + 1
        R[i + 1] = CNF[variable]
    # end_time = time.time()
    # print("time to just append => ", end_time - start_time)

    # start_time = time.time()
    # Parse
    for s in range(1, n + 1):
        for v in range(1, m + 1):
            for e in R[v]:
                if(e[0] == inp[s - 1]):
                    dp[1][s][v] = True
                    break
    # end_time = time.time()
    # print(cnt, "ini yang pertama => ", end_time - start_time)

    # start_time = time.time()
    for l in range(2, n + 1):
        for s in range(1, (n - l + 2)):
            for p in range(1, l):
                for a in range(1, m + 1):
                    for e in R[a]:
                        if(len(e) != 1):
                            b = mp[e[0]]
                            c = mp[e[1]]
                            if (dp[p][s][b] and dp[l - p][s + p][c]):
                                dp[l][s][a] = True
                                break

    # end_time = time.time()
    # print(cnt, ": ini yang kedua => ", end_time - start_time)

    # Result
    if(dp[n][1][1]):
        print("Accepted")
    else :
        print("Syntax Error")

def schedule_dp(tasks, max_time):
    n = len(tasks)
    dp = [[0]*(max_time+1) for _ in range(n+1)]

    for i in range(1, n+1):
        t = tasks[i-1].execution_time
        p = tasks[i-1].priority
        for w in range(max_time+1):
            if t <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-t] + p)
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][max_time]

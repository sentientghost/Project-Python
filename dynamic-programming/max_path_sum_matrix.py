class solution:
    def maximumPath(self, N, Matrix):
        return self.maximumPath_dp(N, Matrix)

    # dynamic programming solution
    def maximumPath_dp(self, N, Matrix):
        total = 0
        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

        for j in range(N):
            dp[0][j] = Matrix[0][j]

        for i in range(N):
            for j in range(N):
                dp[i][j] = Matrix[i][j] + \
                    max(dp[i-1][j], max(dp[i-1][max(0, j-1)],
                                        dp[i-1][min(j+1, N-1)]))

        for j in range(N):
            total = max(total, dp[N-1][j])

        return total

class solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, N):
        k = [[None for _ in range(W+1)] for _ in range(N+1)]
        return self.knapSack_dp(W, wt, val, N, k)

    # Memoized Solution
    def knapSack_memo(self, W, wt, val, N, k):
        if (N == 0 or W == 0):
            return 0

        if (k[N][W] != None):
            return k[N][W]

        if (wt[N-1] <= W):
            k[N][W] = max(val[N-1] + self.knapSack_memo(W-wt[N-1], wt,
                                                        val, N-1, k), self.knapSack_memo(W, wt, val, N-1, k))
            return k[N][W]
        elif (wt[N-1] > W):
            k[N][W] = self.knapSack_memo(W, wt, val, N-1, k)
            return k[N][W]

        return self.knapSack_memo(W, wt, val, N-1, k)

    # Dynamic Programmming Solution (Bottom-Up Approach)
    def knapSack_dp(self, W, wt, val, N, k):
        for n in range(N+1):
            for w in range(W+1):
                if (n == 0 or w == 0):
                    k[n][w] = 0
                elif wt[n-1] <= w:
                    k[n][w] = max(val[n-1] + k[n-1][w-wt[n-1]], k[n-1][w])
                else:
                    k[n][w] = k[n-1][w]

        return k[n][W]

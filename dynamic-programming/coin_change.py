class solution:
    def count(self, S, m, n):
        return self.count_dp(S, m, n)

    # recursive solution
    def count_recur(self, S, m, n):
        # base cases
        if (n == 0):
            return 1

        if (n < 0):
            return 0

        if (m <= 0 and n >= 1):
            return 0

        # recursive leap of faith
        # sum of including the coin and not including the coin
        return self.count_recur(S, m, n-S[m-1]) + self.count_recur(S, m-1, n)

    # dynamic programming solution
    def count_dp(self, S, m, n):
        k = [0 for _ in range(n+1)]

        k[0] = 1

        for i in range(0, m):
            for j in range(S[i], n+1):
                k[j] += k[j-S[i]]

        return k[n]

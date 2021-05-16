class solution:
    # find the minimum number of characters to be inserted to convert it to palindrome
    def countMin(self, Str):
        # recursion
        # return self.countMin_recurse(Str, 0, len(Str)-1)

        # dynamic programming
        return self.countMin_dp(Str)

    # recursive approach
    def countMin_recurse(self, Str, l, r):
        # base cases
        if (l == r):
            return 0

        if (l == r - 1):
            if (Str[l] == Str[r]):
                return 0
            else:
                return 1

        if (Str[l] == Str[r]):
            return self.countMin_recurse(Str, l + 1, r - 1)
        else:
            return (min(self.countMin_recurse(Str, l, r - 1),
                        self.countMin_recurse(Str, l + 1, r)) + 1)

    # dynamic programming
    def countMin_dp(self, Str):
        table = [[0 for _ in range(len(Str))] for _ in range(len(Str))]

        for i in range(1, len(Str)):
            l = 0
            for r in range(i, len(Str)):
                if (Str[l] == Str[r]):
                    table[l][r] = table[l + 1][r - 1]
                else:
                    table[l][r] = (min(table[l][r - 1],
                                       table[l + 1][r]) + 1)
                l += 1

        return table[0][len(Str) - 1]

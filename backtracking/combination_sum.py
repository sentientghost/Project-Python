class solution:
    def __init__(self):
        self.ans = []
        self.combi = []

    def combinationSum(self, A, N, B):
        A.sort(reverse=False)
        self.uniqueCombination(0, 0, A, B)

        return self.ans

    def addCombination(self):
        arr = self.combi.copy()
        if arr not in self.ans:
            self.ans.append(arr)
        return

    def uniqueCombination(self, k, total, A, B):
        if (total == B):
            self.addCombination()
            return

        for i in range(k, len(A), 1):
            if (total + A[i] > B):
                continue

            self.combi.append(A[i])

            self.uniqueCombination(i+1, total+A[i], A, B)

            self.combi.remove(self.combi[len(self.combi) - 1])

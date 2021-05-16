class solution:
    def hanoi(self, n, start, via, end):
        if (n == 0):
            return
        else:
            self.hanoi(n-1, start, end, via)
            self.printMove(start, end)
            self.hanoi(n-1, via, start, end)

    def printMove(self, start, end):
        print("Move disk from {} to {}".format(start, end))

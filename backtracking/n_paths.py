class solution:
    def numberOfPaths (self, n, m):
        if(m == 1 or n == 1):
            return 1
            
        return self.numberOfPaths(m-1, n) + self.numberOfPaths(m, n-1)

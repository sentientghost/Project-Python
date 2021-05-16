class solution:
    def longestSubstrDitinctChars(self, S):
        substring = []
        window = []
        for x in S:
            while x in window:
                window.pop(0)

            window.append(x)

            if (len(substring) < len(window)):
                substring.clear()
                substring.extend(window)

        return len(substring)

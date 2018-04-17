class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        d = {}
        for a,b in enumerate(s):
            if b in d:
                start = max(start, d[b] + 1)
            d[b] = a
            end = max(end, a - start + 1)
        return end    
s = Solution()
a = "asfddsafdsafbk"
b = s.lengthOfLongestSubstring(a)
print(a, b)

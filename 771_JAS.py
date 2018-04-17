class Solution:
#   def numJewelsInStones(self, J, S):
#       """
#       :type J: str
#       :type S: str
#       :rtype: int
#       """
#       return sum(s in J for s in S)
    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))

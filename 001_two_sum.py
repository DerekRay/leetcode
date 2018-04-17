import time
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i,num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index = nums.index(sub_num) 
                if i != t_index:
                    return [i, t_index]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

    def twoSum1(self, nums, target):
        for i,num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index = nums.index(sub_num) 
                if i != t_index:
                    return [i, t_index]
        
nums = [x for x in range(3, 10000, 2)]
target = 6000
solution = Solution()
start = time.clock()
two_sum = solution.twoSum(nums, target)
end = time.clock()
print(two_sum, end - start)

start = time.clock()
two_sum = solution.twoSum1(nums, target)
end = time.clock()
print(two_sum, end - start)

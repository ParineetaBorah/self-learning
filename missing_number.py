class Solution:
    '''
    Solution to missing number problem

    args:
    nums: List

    returns: int
    '''
    def missingNumber(self, nums):
        sum_nums = sum(nums)
        sum_all_nos = sum([i for i in range(0, len(nums)+1)])
        return sum_all_nos - sum_nums

nums = [8,6,4,2,5,7,0,1,9,10,11,12]
sol = Solution()
print(sol.missingNumber(nums))


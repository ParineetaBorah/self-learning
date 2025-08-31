class Solution:
    def missingNumber(self, nums):
        # all_nums = [i for i in range(0,len(nums)+1)]
        # missing_num = [i for i in all_nums if i not in nums][0]
        # return missing_num
        sum_nums = sum(nums)
        sum_all_nos = sum([i for i in range(0, len(nums)+1)])
        return sum_all_nos-sum_nums
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        new_nums = []

        for i in range(0, len(nums)):
            sum += nums[i]
            new_nums.append(sum)

        return (new_nums)
# Runtime: 75 ms
# Memory: 14.1 MB
# Beats: 73.3%

        # for i in nums:
        #     new_nums.append(sum + i)
        #     sum += i
# Runtime: 56 ms
# Memory: 14.2 MB
# Beats: 80.2%

        # for i in range(1,len(nums)):
        #     nums[i] += nums[i-1]
# Runtime: 88 ms
# Memory: 14.1 MB
# Beats: 26.74%


# nums = [1,2,3,4]


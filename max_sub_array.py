from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()
print(solution.maxSubArray(nums))
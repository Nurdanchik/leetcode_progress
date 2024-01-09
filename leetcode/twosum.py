from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
nums = [1, 2, 3, 4, 5]
target = 8
result = sol.twoSum(nums, target)
print(result)
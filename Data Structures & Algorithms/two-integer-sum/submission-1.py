class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        h = {}

        for i in range(N):
            if target - nums[i] in h:
                return [h[target - nums[i]], i]
            h[nums[i]] = i

        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_hash = {}

        for i, num in enumerate(nums):
            if target - num in val_hash:
                return [val_hash[target- num], i]

            val_hash[num] = i
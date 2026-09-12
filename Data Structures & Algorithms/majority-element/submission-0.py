class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        leading_num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == leading_num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    leading_num = nums[i]
                    count = 1

        return leading_num
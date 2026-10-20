class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        threshold = len(nums) // 3 + 1

        res = []

        for num in nums:
            count[num] += 1
            
            if count[num] == threshold:
                res.append(num)

        return res
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefix_sum[diff]
            prefix_sum[curr_sum] += 1

        return res
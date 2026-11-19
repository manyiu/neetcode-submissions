class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        seen = [False] * N

        for num in nums:
            if num > 0 and num <= N:
                seen[num - 1] = True

        for num in range(1, N + 1):
            if not seen[num - 1]:
                return num

        return N + 1
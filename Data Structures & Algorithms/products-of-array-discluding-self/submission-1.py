class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        prefix = [1] * N
        suffix = [1] * N

        for i in range(1, N):
            prefix[i] *= prefix[i - 1] * nums[i - 1]
            suffix[N - i - 1] *= suffix[N - i] * nums[N - i]

        return [prefix[i] * suffix[i] for i in range(N)]
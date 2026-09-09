class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a, b, c, d]
        # [bcd, cd , d , 1]
        # [1, a, ab, abc]
        # [bcd, acd, abd, abc]

        N = len(nums)

        forward = [1] * N
        backward = [1] * N

        for i in range(1, N):
            forward[i] = forward[i-1] * nums[i-1]
            backward[N - i - 1] = backward[N - i] * nums[N - i]

        return [ a*b for a, b in zip(forward, backward)]

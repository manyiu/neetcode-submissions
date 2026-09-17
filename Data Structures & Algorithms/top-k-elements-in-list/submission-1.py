class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_heap = []

        for num, freq in counter.items():
            heapq.heappush_max(max_heap, (freq, num))
        
        res = []

        for _ in range(k):
            _, num = heapq.heappop_max(max_heap)
            res.append(num)

        return res
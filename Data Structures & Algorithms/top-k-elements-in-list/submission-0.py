class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        min_heap = [(-count, num) for num, count in num_count.items()]
        heapq.heapify(min_heap)

        res = []

        for _ in range(k):
            _, num = heapq.heappop(min_heap)
            res.append(num)

        return res


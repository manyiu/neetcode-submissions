class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        uf = UnionFind(N)
        num_to_index = {}

        for i, num in enumerate(nums):
            if num in num_to_index:
                continue

            num_to_index[num] = i

            if num - 1 in num_to_index:
                uf.union(i, num_to_index[num - 1])
            if num + 1 in num_to_index:
                uf.union(i, num_to_index[num + 1])
            
        res = 0

        group_count = defaultdict(int)

        for i in range(N):
            root = uf.find(i)
            group_count[root] += 1
            res = max(res, group_count[root])

        return res



        
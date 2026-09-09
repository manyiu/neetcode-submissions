class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node: int, previous: int) -> bool:
            if node in visit:
                return False

            visit.add(node)

            for dest in adj[node]:
                if dest != previous:
                    if not dfs(dest, node):
                        return False

            return True

        return dfs(0, -1) and len(visit) == n
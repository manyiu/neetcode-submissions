class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_count = defaultdict(int)

        N = len(s)
        M = len(t)

        if N != M:
            return False

        for i in range(N):
            map_count[s[i]] += 1
            map_count[t[i]] -= 1

        for val in map_count.values():
            if val != 0:
                return False

        return True
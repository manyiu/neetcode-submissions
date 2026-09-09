class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if len(s) != len(t):
            return False

        for ch, c in s_count.items():
            if t_count[ch] != c:
                return False

        return True
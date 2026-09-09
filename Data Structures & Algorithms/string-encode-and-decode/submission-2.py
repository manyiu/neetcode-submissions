class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + ":" + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 0

        while i < len(s):
            if s[i] == ":":
                len_string = s[j:i]
                len_int = int(len_string)
                content = s[i+1: i+1+len_int]
                res.append(content)
                i = j = i + 1 + len_int
            else:
                i += 1

        return res

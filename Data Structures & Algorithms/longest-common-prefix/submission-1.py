class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        N = len(strs) # element count

        if N == 0:
            return res

        M = len(strs[0]) # character count of first element

        if M == 0:
            return res

        contin = True

        for i in range(M):
            match_ch = strs[0][i]

            for j in range(1, N):
                if i >= len(strs[j]) or match_ch != strs[j][i]:
                    contin = False

            if contin:
                res += match_ch
            else:
                break

        return res



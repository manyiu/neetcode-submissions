class Solution:

    def encode(self, strs: List[str]) -> str:
        curr = ""

        for s in strs:
            curr += str(len(s)) + "#" + s

        return curr

    def decode(self, s: str) -> List[str]:
        curr = []

        N = len(s)
        j = 0

        while j < N:
            i = j

            while s[j] != "#":
                j += 1

            seperator = j

            ch_count = int(s[i:j])

            word = s[seperator+1: seperator+1+ch_count]

            curr.append(word)

            j = seperator+1+ch_count

        return curr


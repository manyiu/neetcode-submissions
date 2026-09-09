class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([ str(len(word)) + ":" + word for word in strs])

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0

        while i < len(s):
            start = i

            while s[i] != ":":
                i += 1

            length = int(s[start:i])
            word = s[i+1:i+1+length]

            output.append(word)

            i = i + 1 + length

        return output
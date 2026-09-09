class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            word_map[key].append(word)

        res = []

        for group in word_map.values():
            res.append(group)

        return res
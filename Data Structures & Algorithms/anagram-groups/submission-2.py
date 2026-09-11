class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_word = defaultdict(list)

        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            group_word[key].append(s)

        res = []

        for indic in group_word.values():
            res.append(indic)

        return res
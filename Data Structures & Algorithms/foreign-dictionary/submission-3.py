class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            wordA, wordB = words[i], words[i + 1]

            minLen = min(len(wordA), len(wordB))

            if len(wordA) > len(wordB) and wordA[:minLen] == wordB:
                return ""

            for j in range(minLen):
                if wordA[j] != wordB[j]:
                    adj[wordB[j]].add(wordA[j])
                    break

        visit = set()
        path = set()
        topSort = []

        def dfs(src) -> bool:
            if src in path:
                return False

            if src in visit:
                return True

            visit.add(src)
            path.add(src)

            if src in adj:
                for dist in adj[src]:
                    if not dfs(dist):
                        return False

            path.remove(src)
            topSort.append(src)
            return True

        for c in adj:
            if not dfs(c):
                return ""

        return "".join(topSort)
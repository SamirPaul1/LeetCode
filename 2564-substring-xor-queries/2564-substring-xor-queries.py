class Solution:
    def substringXorQueries(self, s, queries):
        seen = defaultdict(lambda: [-1, -1])
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                seen[0] = [i, i]
                continue
            v = 0
            for j in range(i, len(s)):
                v = v*2 + int(s[j])
                if v > 2**32: break
                seen[v] = [i, j]
        return [seen[fst ^ snd] for fst, snd in queries]
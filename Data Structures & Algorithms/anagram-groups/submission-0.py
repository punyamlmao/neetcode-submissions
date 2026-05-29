class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in strs:
            j = "".join(sorted(i))
            if j in freq:
                freq[j].append(i)
            else:
                freq[j] = [i]

        return list(freq.values())
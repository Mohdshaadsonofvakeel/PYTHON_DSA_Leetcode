from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the word to get the canonical form of the anagram group
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())
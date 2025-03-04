# 3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict(list) prevents KeyErrors when adding new keys
        res = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key for all its anagrams
            # "eat", "tea", and "ate" all become "aet"
            sorted_key = "".join(sorted(s))
            
            # Group the original string under its sorted key
            res[sorted_key].append(s)
            
        # Return only the values (the lists of grouped anagrams)
        return list(res.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_list = []
        for i in range(len(strs)):
            # Skip if this string has already been grouped
            if strs[i] is None:
                continue
                
            # Start a new group with the current string
            ang = [strs[i]]
            # Sort once for comparison
            sorted_i = sorted(strs[i])
            
            for j in range(i + 1, len(strs)):
                # Only compare if the string hasn't been grouped yet
                if strs[j] is not None:
                    if sorted_i == sorted(strs[j]):
                        ang.append(strs[j])
                        # Mark as None so it's skipped in the outer loop
                        strs[j] = None
            
            list_list.append(ang)
            # No need to set strs[i] = None here as the loop won't revisit it
            
        return list_list
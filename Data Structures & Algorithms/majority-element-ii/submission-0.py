class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsDict = {}
        output = []
        threshold = len(nums) // 3
        
        # 1. Count frequencies
        for i in nums:
            numsDict[i] = 1 + numsDict.get(i, 0)
            
        # 2. Check which numbers pass the threshold
        for n in numsDict:
            if numsDict[n] > threshold:
                output.append(n)
                
        return output
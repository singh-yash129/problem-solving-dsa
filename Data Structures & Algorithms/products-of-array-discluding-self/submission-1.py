class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        output = []
        
        # Count zeros and get the product of all non-zero elements
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero_count += 1

        # Populate the output array based on the number of zeros
        for i in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if i != 0:
                    output.append(0)
                else:
                    output.append(prod)
            else:
                output.append(prod // i)
                
        return output
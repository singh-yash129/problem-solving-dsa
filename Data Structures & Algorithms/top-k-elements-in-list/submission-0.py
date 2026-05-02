class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        # 2. Sort the dictionary items by frequency (index 1 of the tuple)
        # sorted() returns a list of tuples: [(num, count), (num, count)...]
        sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

        # 3. Extract the top k keys (num) from the tuples
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res
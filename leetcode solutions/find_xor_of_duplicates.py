from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans =0
        for key,value in freq.items():
            if value ==2:
                ans = key ^ ans
        return ans

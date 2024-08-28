class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums= nums + [0]
        MaxConsecutiveOnes = 0
        consectiveOnes = 0
        pointer=0

        while pointer<len(nums):
            if nums[pointer] ==1:
                pointer+=1
                consectiveOnes +=1

            else:
                if consectiveOnes>MaxConsecutiveOnes:
                    MaxConsecutiveOnes = consectiveOnes

                consectiveOnes =0
                pointer = pointer +1
        return MaxConsecutiveOnes
        
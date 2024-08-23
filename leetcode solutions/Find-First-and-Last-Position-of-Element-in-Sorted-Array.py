class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:

      left = 0
      right = len(nums)-1
      lb=-1
      while left<=right:
          mid= left + (right -left)//2
          if target > nums[mid]:
              left = mid +1
          elif target <=nums[mid]:
              lb= mid
              right =mid-1


      left = 0
      right = len(nums)-1
      ub=-1
      while left<=right:
          mid= left + (right -left)//2
          if target >= nums[mid]:
              ub= mid
              left = mid +1
          elif target < nums[mid]:
              right =mid-1


      lb = lb if -1<lb < len(nums) and nums[lb] ==target  else -1
      ub = ub if len(nums )>ub > -1 and  nums[ub] == target else -1
      return [lb,ub]
      
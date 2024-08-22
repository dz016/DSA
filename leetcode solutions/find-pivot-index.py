class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
      pre=[nums[0]]
      for i in range(1,len(nums)):
          pre.append(nums[i] + pre[i-1])


      for i in range(len(pre)):
          util = pre[-1] - pre[i]
          print(i,util)
          boolean = util == pre[i-1] if i!=0 else util == 0

          if boolean:
              return i

      return -1





class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      ans =[]
      res=[]
      def helper(i,acc):
          if i>=len(candidates):
              if acc == target:
                  ans.append(res.copy())
              return

          Sum = acc
          helper(i+1,Sum)
          while Sum<=target:
              res.append(candidates[i])
              Sum = Sum + candidates[i]
              helper(i+1,Sum)


          while Sum>acc:
              Sum = Sum -res.pop()

      helper(0,0)
      return ans











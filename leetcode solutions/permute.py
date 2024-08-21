class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
      answer = []
      def helper(p,up):
          nonlocal answer
          if len(up) ==0 :
              answer.append(p)
              return


          for i in range(len(p) +1 ):
              left = p[:i]
              right = p[i:]

              helper(left + [up[0]] +right,up[1:])

      helper([],nums)
      return answer



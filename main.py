def permute(nums):
  answer = []
  def helper(p,up):
      nonlocal answer
      if len(up) ==0 :
          answer.append(p)
          return
      
      
      
      for i in range(len(p) +1 ):
          left = p[:i]
          right =p[i:]
          helper(left + [up[0]] +right,up[1:])
      return
          
  helper([],nums)
  return answer



print(permute([1,2,3]))
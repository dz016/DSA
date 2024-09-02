


def solution(s1,s2):
    if len(s1) != len(s2):

        return False
    ans =True
    helper ={}


    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else :
            if len(helper) ==1 and helper.get(s2[i],"-1") != s1[i]:
                ans = False

            if len(helper)>1:
                ans = False

            helper[s1[i]] = s2[i]
    return ans

print(solution("banke","bnaka"))

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        ans=0
        cT=0
        cF=0
        for r in range(len(answerKey)) :
            if answerKey[r] == 'T' :
                cT += 1
            else :
                cF += 1
            while min(cT,cF) > k :
                if answerKey[l] == 'T' :
                    cT -= 1
                else :
                    cF -= 1
                l+=1
            ans = max(ans,r-l+1)
        return ans  

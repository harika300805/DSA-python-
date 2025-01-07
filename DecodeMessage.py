class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        original = list("abcdefghijklmnopqrstuvwxyz")
        k=[]
        for i in key:
            if i != " " and i not in k :
                k.append(i)
        d=dict(zip(k,original))
        res=""
        for j in message:
            if j == " ":
                res += " "
            else:
                res += d[j]  
        return res      
        

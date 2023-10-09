#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        n=len(s)
        x=0
        count=0
        while(x!=n):
            x+=numRows+(numRows-2)
            count+=(numRows-2)+1
            if(n-x<=numRows):
                x+=n-x
                count+=1
                continue
            if(n-x<=numRows+(numRows-2)):
                count+=((n-x)-numRows)+1
                x+=n-x
                
                continue
        # print(count)
        n=0
        i=0
        j=0
        n=0
        l = [[0 for i in range(numRows)] for j in range(count)]
        # l=[[0]*numRows]*count
        # print(l)
        while(n!=len(s)):
            while(j!=numRows):
                if(n==len(s)):
                    break
                l[i][j]=s[n]
                j+=1
                n+=1
            i+=1
            for j in range(numRows-2,0,-1):
                if(n==len(s)):
                    break
                l[i][j]=s[n]
                n+=1
                i+=1
            j=0
            
        # print(l)
        b=''
        for i in range(numRows):
            for j in range(count):
                if(l[j][i]!=0):
                    b+=(l[j][i])
                    
        return (b)
        
# @lc code=end


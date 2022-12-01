class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di={}
        
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
                
        for i,j in enumerate(di):
            if di[j]==1:
                return j

class Solution:
    def singleNumber(self, nums) :
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1 
        for i in count:
                if count[i] == 1:
                    return i
        return -1 

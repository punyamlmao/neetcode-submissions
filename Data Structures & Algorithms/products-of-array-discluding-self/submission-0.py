class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        freq_left={}
        freq_right={}
        total_left=1
        total_right=1
        for i in range(len(nums)):
            total_left=total_left*nums[i]
            freq_left[i]=total_left
        
        for i in range(len(nums)-1,-1,-1):
            total_right=total_right*nums[i]
            freq_right[i]=total_right
        
        for i in range(len(nums)):
            if i==0:
                output.append(freq_right[i+1])
            elif i==len(nums)-1:
                output.append(freq_left[i-1])
            else:
                output.append(freq_left[i-1]*freq_right[i+1])
        return output
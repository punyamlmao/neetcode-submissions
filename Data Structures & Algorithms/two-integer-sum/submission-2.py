class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k_map={}
        ans=[]
        for i in range(len(nums)):
            if (target-nums[i]) in k_map:
                ans.append(k_map[target-nums[i]])
                ans.append(i)
            else:
                k_map[nums[i]]=i
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        max_count = 0
        smallest=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in nums:
            count=0
            if i-1 not in freq:
                smallest = i
                count+=1
                while (smallest+1 in freq):
                    count+=1
                    smallest+=1
            if count > max_count:
                max_count=count
        return max_count
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for i in sorted(freq, key=lambda x: freq[x], reverse=True):
            if k!=0:
                result.append(i)
                k-=1
        return result
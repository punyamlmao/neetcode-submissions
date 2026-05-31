class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s=s.lower()
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            elif s[left]==" " or not s[left].isalnum():
                left+=1
            elif s[right]==" " or not s[right].isalnum():
                right-=1
            else:
                print(left)
                return False
        return True
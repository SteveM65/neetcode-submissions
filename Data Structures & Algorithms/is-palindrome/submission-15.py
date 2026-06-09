class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Get two pointers in beginning and end
        #Check if they are the same (lowercase)
        #If they are spaces or non-alphanumeric, move forward     
        #If not matching, return false



        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
            
        return True



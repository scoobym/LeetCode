class Solution:

    count = 0

    def isSubstrings(self, s, left, right):
        while(left>=0 and right<len(s)) and (s[left]==s[right]):
            left -= 1
            right += 1
            self.count += 1

    def countSubstrings(self, s):
        if len(s)==0:
            return 0
        for i in range(len(s)):
            self.isSubstrings(s,i,i)
            self.isSubstrings(s,i,i+1)

        return self.count



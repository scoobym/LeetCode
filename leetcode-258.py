class Solution:
    def addDigits(self, num):
        if num==0 :
            return num
        elif num%9==0 :
            return 9
        else:
            return num%9
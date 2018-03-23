class Solution:
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        sum = 1
        i=2
        while i<=num/i :
            if num%i==0 :
                if i==num//i :
                    sum+=i
                else:
                    sum+=i
                    sum+=num//i
            i+=1
        if sum==num:
            return True
        else:
            return False
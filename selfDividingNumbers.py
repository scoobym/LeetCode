class Solution:
    def selfDividingNumbers(self, left, right):
        list = []
        for i in range(left,right+1):
            d=i
            j=1
            while (d!=0) and ((i%j)==0):
                j=d%10
                d=d//10
                if j==0:
                    break 
            if d==0 and i%j==0:
                list.append(i)
        return list

test = Solution()
print(test.selfDividingNumbers(1,100))
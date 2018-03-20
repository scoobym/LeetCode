class Solution:
    def integerBreak(self, n):
        t=0
        if n%3==0:
            if n==3:
                i=2
            else:
                i=1
                while t!=n:
                    t=t+3
                    i=i*3
        elif n%3==1:
            i=4
            while t!=(n-4):
                t=t+3
                i=i*3
        elif n%3==2:
            if n==2:
                i = 1
            else:
                i=2
                n=n-2
                while(n>0)and(t!=n):
                    t+=3
                    i=i*3
        return i




            
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j=0
        temp = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[' :
                temp.append(s[i])
            else:
                if s[i]==')' :
                    if len(temp)==0 or temp.pop()!='(':
                        return False
                elif s[i]==']' :
                    if len(temp)==0 or temp.pop()!='[':
                        return False
                elif s[i]=='}' :
                    if len(temp)==0 or temp.pop()!='{':
                        return False        
        if len(temp)==0:
            return True
        else:
            return False
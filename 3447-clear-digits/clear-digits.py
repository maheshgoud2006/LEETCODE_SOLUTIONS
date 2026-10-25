class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
            
        
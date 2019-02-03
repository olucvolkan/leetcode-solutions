#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        #created tuple's every character
        for i in zip(*strs):
            if len(set(i)) !=1:
                return prefix
            else:
                prefix +=i[0]
        return prefix

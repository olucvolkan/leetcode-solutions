#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        couples = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        total = 0
        i = 0
        string_length = len(s)
        while i<string_length:
            if string_length <=2:
                if s[i:i+2] in couples.keys():
                    total += couples[s[i:i+2]]
                    i+=2
                else:
                    total +=pair[s[i]]
                    i+=1
            else:
                if s[i:i+2] in couples.keys():
                    total +=couples[s[i:i+2]]
                    i+=2
                else:
                    total += pair[s[i]]
                    i+=1
        return total
class Solution:
    def romanToInt(self, s: str) -> int:
        '''Meth 1:  I did take IV, XL, XC, CD, CM to the hashmap so while looping checked for s[i] + s[I + 1] in hashmap… 
        We can also do Meth2: Only take the given Roman values in hashmap and when s[i] < s[i+1] subtract the s[i] value from integer formed.'''
        integer = 0
        i = 0
        romanToInt = {'I' : 1, 'IV' : 4, 'V': 5, 'IX' : 9, 'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90, 'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
        while i < len(s):
            if i < len(s) - 1 and s[i] + s[i + 1] in romanToInt:
                integer += romanToInt[s[i] + s[i + 1]]
                i += 1
            else:
                integer += romanToInt[s[i]]
            i += 1
        return integer
     
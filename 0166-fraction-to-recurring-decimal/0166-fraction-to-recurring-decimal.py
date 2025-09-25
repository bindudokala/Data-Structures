class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []
        q = 0
        if numerator == 0:
            return "0"
        
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        
        q += numerator // denominator
        result.append(str(q))

        rem = numerator % denominator
        if rem == 0:
            return "".join(result)
        
        result.append(".")
        remainder_map = {}
        
        while rem != 0:
            if rem in remainder_map:
                indx = remainder_map[rem]
                result.insert(indx, "(")
                result.append(")")
                break

            remainder_map[rem] = len(result)
            rem *= 10
            result.append(str(rem // denominator))
            rem %= denominator
        
        return "".join(result)

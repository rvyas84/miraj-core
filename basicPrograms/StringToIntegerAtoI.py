class StringToIntegerAtoI:

    def __init__(self):
        pass

    def StringToIntegerAtoI(self, s:str) -> int:
        if not s:
            return 0
        s = s.strip()

        sign = 1
        result = 0

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            
            s = s[1:]

        for c in s:
            if not c.isdigit():
                break
            else:
                result = result * 10 + int(c)
        
        result = result * sign

        if result > 2**31 -1:
            return 2**31 -1
        elif result < -2**31:
            return -2**31
        
        return result

StoI = StringToIntegerAtoI()
print(StoI.StringToIntegerAtoI("1234 San Franciscos"))
print(StoI.StringToIntegerAtoI("-1234 San Jose"))
print(StoI.StringToIntegerAtoI("San Jose 2345"))
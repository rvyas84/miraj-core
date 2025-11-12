class StringToIntegerAtoI:

    def __init__(self):
        pass

    def StringToIntegerAtoI(self, s: str) -> int:
        """
        Convert a string to an integer (implementing the atoi function).

        This function converts a string representation of an integer to its 
        integer value. It handles leading whitespace, optional sign, and 
        stops converting at the first non-digit character. The function 
        also ensures that the returned integer is within the 32-bit signed 
        integer range.

        Parameters:
        s (str): The string to convert to an integer.

        Returns:
        int: The converted integer value, or the bounds of a 32-bit signed 
        integer if the value exceeds that range.
        """
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

        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        
        return result

if __name__ == "__main__":
    StoI = StringToIntegerAtoI()
    print(StoI.StringToIntegerAtoI("1234 San Franciscos"))
    print(StoI.StringToIntegerAtoI("-1234 San Jose"))
    print(StoI.StringToIntegerAtoI("San Jose 2345"))


    # output

    # 1234
    # -1234
    # 0
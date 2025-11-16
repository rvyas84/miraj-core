class RomanToInt:
    def romanToInt(self, input: str) -> int:
        
        hashEqui = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        i = 0
        n = len(input)
        sum = 0

        while i < n:
            if i < n - 1 and hashEqui[input[i]] < hashEqui[input[i+1]]:
                sum += hashEqui[input[i+1]] - hashEqui[input[i]]
                i += 2
            else:
                sum += hashEqui[input[i]]
                i += 1
        
        return sum

if __name__ == "__main__":
    romToIn = RomanToInt()
    print(romToIn.romanToInt("MCMXCIV"))
    print(romToIn.romanToInt("III"))


# Output: 1994, 3

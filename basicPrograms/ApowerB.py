class calculatePower:

    def calPower(self, baseNum, exponentNum):
        result = 1

        for i in range(exponentNum):
            result = result * baseNum
        
        return result

cal = calculatePower()
print(cal.calPower(2,3))

# Quick Way To Calculate ApowerB
print(2**3)
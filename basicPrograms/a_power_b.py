class calculatePower:
    """
    A class to calculate the power of a number.

    Methods
    -------
    calPower(baseNum, exponentNum):
        Calculates the result of baseNum raised to the power of exponentNum.
    """

    def calPower(self, baseNum, exponentNum):
        result = 1

        if exponentNum < 0:
            baseNum = 1 / baseNum
            exponentNum = -exponentNum

        for i in range(exponentNum):
            result = result * baseNum

        if result > 2**31:
            return 2**31
        elif result < -2**31:
            return -2**31
        else:
            return result

if __name__ == "__main__":
    cal = calculatePower()
    print(cal.calPower(2,3))

    # Quick Way To Calculate ApowerB
    print(2**3)
    print(2**-3)
class PrintSeries:
    """
    A class to print a series of numbers in a specific pattern.

    Methods
    -------
    printSeries(n: int):
        Prints a series of numbers from 1 to n, where each number i is printed i times.
    """

    def __init__(self):
        pass

    def printSeries(self, n):
        for i in range(n):
            for j in range(i + 1):
                print(f"{i + 1} ", end='')

if __name__ == "__main__":    
    ps = PrintSeries()
    ps.printSeries(5)

    # Output
    # 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
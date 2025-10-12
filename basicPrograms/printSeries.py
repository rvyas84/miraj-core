class PrintSeries:

    def __init__(self):
        pass

    def printSeries(self, n):
        for i in range(n):
            for j in range(i+1):
                print(f"{i + 1} ", end='')

    
ps = PrintSeries()
ps.printSeries(5)

class PrintFibonacci:
    def __init__(self):
        pass
    
    def printFibo(self, n: int) -> int:
        if n < 0:
            raise ValueError("Value must be greater than zero")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.printFibo(n - 1) + self.printFibo(n - 2)

fibo = PrintFibonacci()
for i in range(10):
    print(fibo.printFibo(i), end=" ")
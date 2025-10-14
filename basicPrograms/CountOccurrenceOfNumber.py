class countOcurrence:
    def __init__(self, list):
        self.list = list
    
    # Using classic approach
    def countOccurrenceOfNumber(self) -> int:
        count = 0

        for i in self.list:
            if i == 2:
                count += 1

        return count
    
totalCount = countOcurrence([1,2,2,2,2,2,3,4,5,6])
print(totalCount.countOccurrenceOfNumber())

# Using Python Inbuilt Function
print([1,2,2,2,2,2,3,4,5,6].count(2))
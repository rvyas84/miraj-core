class countOcurrence:
    """
    A class to count the occurrences of a specific number in a list.

    Attributes:
        list (list): A list of numbers in which to count occurrences.
    """

    def __init__(self, list):
        self.list = list
    
    # Using classic approach
    def countOccurrenceOfNumber(self) -> int:
        """
        Counts the occurrences of the number 2 in the list.

        Returns:
            int: The count of occurrences of the number 2.
        """
        count = 0

        for i in self.list:
            if i == 2:
                count += 1

        return count
    
totalCount = countOcurrence([1,2,2,2,2,2,3,4,5,6])
print(totalCount.countOccurrenceOfNumber())

# Using Python Inbuilt Function
print([1,2,2,2,2,2,3,4,5,6].count(2))
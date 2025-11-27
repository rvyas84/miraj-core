class UniqueSortList:
    """
    A class to sort a list of values in both ascending and descending order.

    Methods
    -------
    sortList(listValues):
        Sorts the provided list of values and prints the sorted lists in 
        ascending and descending order.
    """

    def __init__(self):
        pass

    def sortList(self, listValues):
        print(sorted(listValues))  # Sorts in ascending order
        print(f"Discending Order Sorting {sorted(listValues, reverse=True)}")  # Sorts in descending order
class SortList:

    def __init__(self):
        pass

    def sortList(self, listValues):
        print(sorted(listValues)) # Sorts in ascending order
        print(f"Discending Order Sorting {sorted(listValues, reverse = True)}") # Sorts in descending order


if __name__ == "__main__":
    sl = SortList()
    sl.sortList([1,1,7,1,4,1,6,1,2,1,1,1,4,1,6,1,8,1,9,1,9,1,7,1,5,1,3])

# Output
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9]
# Discending Order Sorting [9, 9, 8, 7, 7, 6, 6, 5, 4, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
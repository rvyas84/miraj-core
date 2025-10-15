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
    
sl = SortList()
sl.sortList([1,1,7,1,4,1,6,1,2,1,1,1,4,1,6,1,8,1,9,1,9,1,7,1,5,1,3])
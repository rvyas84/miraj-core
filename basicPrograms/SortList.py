class SortList:

    def __init__(self):
        pass

    def sortList(self, listValues):
        print(sorted(listValues)) # Sorts in ascending order
        print(f"Discending Order Sorting {sorted(listValues, reverse = True)}") # Sorts in descending order
    
sl = SortList()
sl.sortList([1,1,7,1,4,1,6,1,2,1,1,1,4,1,6,1,8,1,9,1,9,1,7,1,5,1,3])
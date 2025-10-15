class RemoveDupFromList:
    """
    A class to remove duplicates from a list.

    Methods
    -------
    removeDupFromList(values):
        Removes duplicates from the provided list of values and prints the unique values.
    """

    def __init__(self):
        pass

    def removeDupFromList(self, values):
        print(set(values))
    
removeDup = RemoveDupFromList()
removeDup.removeDupFromList([9,1,3,2,4,6,6,5,3,4,5,7,6,5,3,2,7,8,8,1])
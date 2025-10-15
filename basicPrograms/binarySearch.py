class binarySearchApp:
    """
    A class to represent a binary search application.

    Attributes
    ----------
    values : list
        A list to store integer values for searching.

    Methods
    -------
    createList(requiredElements):
        Prompts the user to enter integer values and stores them in the values list.

    getList():
        Returns the list of stored values.

    runBinarySearch(searchValue):
        Performs a binary search on the values list to find the specified searchValue.
    """
    
    def __init__(self):
        self.values = []
    
    def createList(self, requiredElements):
        for i in range(requiredElements):
            val = int(input("Enter the value: "))
            self.values.append(val)
        
    def getList(self):
        return self.values
    
    def runBinarySearch(self, searchValue):
        start = 0
        end = len(self.values) - 1
        middle = int((end + start)/2)

        if len(self.values) == 0:
            print("List is Empty")
        
        while start <= end:
            if searchValue == self.values[middle]:
                print("Search value {} is found".format(searchValue))
                break
            elif searchValue > self.values[middle]:
                start = middle + 1
            elif searchValue < self.values[middle]:
                end = middle -1
            
            middle = int((start + end) / 2)
            
            if start > end:
                print("Search value {} is not found".format(searchValue))

            

bs = binarySearchApp()
bs.createList(5) # 1, 2, 3, 4 ,5
print(bs.getList())
bs.runBinarySearch(8)
bs.runBinarySearch(3)
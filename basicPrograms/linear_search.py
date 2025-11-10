class LinerSaerch:
    """
    A class to represent a linear search algorithm.

    Attributes
    ----------
    values : list
        A list to store the elements for searching.

    Methods
    -------
    createStack(totalElements):
        Prompts the user to input values and stores them in the values list.

    searchVal(searchTerm):
        Searches for the specified term in the values list and prints the result.
    """
    
    def __init__(self):
        self.values = []
    
    def createStack(self, totalElements):
        for i in range(totalElements):
            val = int(input("Enter value {}: ".format(i+1)))
            self.values.append(val)

    def searchVal(self, searchTerm):
        count = 0
        if len(self.values) == 0:
            print("List Is Empty")
        else:
            for i in range(len(self.values)):
                count += 1
                if (searchTerm == self.values[i]):
                    print ("Search Term {} is found at {}".format(searchTerm, i))
                    break
                
            if count == len(self.values):
                print("Search Term {} Is Not Found".format(searchTerm))


if __name__ == "__main__":
    ls = LinerSaerch()
    ls.createStack(5) # 10, 20, 30, 40, 50
    ls.searchVal(40)
    ls.searchVal(80)
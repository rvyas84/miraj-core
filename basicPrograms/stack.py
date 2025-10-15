class stackApp:
    """
    A class to represent a stack data structure.

    Attributes
    ----------
    values : list
        A list to store the elements of the stack.

    Methods
    -------
    createStack(totalElements):
        Prompts the user to enter values to create the stack.
    
    getTop():
        Returns the top element of the stack without removing it.
    
    isEmpty():
        Checks if the stack is empty.
    
    remove():
        Removes and returns the top element of the stack.
    """
    
    def __init__(self):
        self.values = []
    
    def createStack(self, totalElements):
        for i in range(totalElements):
            val = input("Enter value {}: ".format(i+1))
            self.values.append(val)
    
    def getTop(self):
        return self.values[-1]
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def remove(self):
        return self.values.pop(-1)

st = stackApp()
st.createStack(5)
print(st.getTop())
print(st.remove())
print(st.remove())
print(st.getTop())
print(st.isEmpty())
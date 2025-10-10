class stackApp:
    
    def __init__(self):
        self.values = []
    
    def createStack(self, totalElements):

        for i in range(totalElements):
            val = input("Enter value {}: ".format(i+1))
            # Using Mannual Appeding Op
            # self.values = self.values + [val]

            #Using Append Function
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
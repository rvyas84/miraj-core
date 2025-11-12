class QueueApp:
    """
    A class to represent a simple queue application.

    Attributes:
    ----------
    values : list
        A list to store the elements of the queue.

    Methods:
    -------
    createQueue(elem):
        Initializes the queue with a specified number of elements.
    
    appendQueue(num):
        Adds an element to the end of the queue.
    
    removeFromQueue():
        Removes and returns the front element of the queue.
    
    isEmpty():
        Checks if the queue is empty.
    
    getQueue():
        Returns the current elements in the queue.
    """
    
    def __init__(self):
        self.values = []

    def createQueue(self, elem):
        val = 0

        for i in range(elem):
            val = input("Enter the Number: ")
            self.values.append(val)
        
    def appendQueue(self, num):
        self.values.append(num)

    def removeFromQueue(self):
        front = self.values[0]
        self.values = self.values[1:]

        return front
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def getQueue(self):
        return self.values

if __name__ == "__main__":
    q1 = QueueApp()
    q1.createQueue(5)
    q1.appendQueue(20)
    print(q1.getQueue())
    print(q1.removeFromQueue())
    print(q1.getQueue())
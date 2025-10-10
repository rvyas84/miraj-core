class ReverseString:

    def __init__(self):
        pass

    def stringReversal(self, strValue):
        return strValue[::-1]
    
revStr = ReverseString()
print("Reversed String {} {} {}".format(revStr.stringReversal("rajan"), revStr.stringReversal("rajan"), revStr.stringReversal("rajan")))
print(f"Reversed String {revStr.stringReversal("rajan")}  {revStr.stringReversal("rajan")}")
print("Reversed String", revStr.stringReversal("rajan"), revStr.stringReversal("rajan"))
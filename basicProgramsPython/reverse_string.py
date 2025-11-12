class ReverseString:
    """
    A class to reverse a given string.

    Methods
    -------
    stringReversal(strValue: str) -> str
        Returns the reversed version of the input string.
    """

    def __init__(self):
        pass

    def stringReversal(self, strValue):
        return strValue[::-1]

if __name__ == "__main__":    
    revStr = ReverseString()
    print("Reversed String {} {} {}".format(revStr.stringReversal("rajan"), revStr.stringReversal("rajan"), revStr.stringReversal("rajan")))
    print(f"Reversed String {revStr.stringReversal("rajan")} {revStr.stringReversal("rajan")}")
    print("Reversed String", revStr.stringReversal("rajan"), revStr.stringReversal("rajan"))
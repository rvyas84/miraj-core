class ReverseWordOrder:
    """
    A class to reverse the order of words in a given string.

    Methods
    -------
    reverseWordOrders(s: str) -> str:
        Reverses the order of words in the input string.
    """

    def __init__(self):
        pass

    def reverseWordOrders(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == "__main__":
    revOrder = ReverseWordOrder()
    input_string = "Hello Words From Python"
    print(revOrder.reverseWordOrders(input_string))
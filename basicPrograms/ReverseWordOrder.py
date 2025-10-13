class ReverseWordOrder:

    def __init__(self):
        pass

    def reverseWordOrders(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

revOrder = ReverseWordOrder()
input_string = "Hello Words From Python"
print(revOrder.reverseWordOrders(input_string))
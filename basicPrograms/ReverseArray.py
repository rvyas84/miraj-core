class ReverseArray:

    def __init__(self):
        pass

    def reverseArray(self, ary, start, end):

        if start >= end:
            return
        
        ary[start], ary[end] = ary[end], ary[start]
        self.reverseArray(ary, start + 1, end - 1)


revArray = ReverseArray()
arrayValues = [11,12,13,14,15,16]
revArray.reverseArray(arrayValues, 0, len(arrayValues)-1)
print(arrayValues)
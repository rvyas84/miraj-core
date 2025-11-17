class CountChars:
    def getCharCount(self, input_string: str) -> dict:
        result_dic = {}
        for char in input_string:
            if char not in result_dic:
                result_dic[char] = 1
            else:
                result_dic[char] += 1
        return result_dic

if __name__ == "__main__":
    countChars = CountChars()
    print(countChars.getCharCount('ThisisatestString'))

    # Output: {'T': 1, 'h': 1, 'i': 3, 's': 3, 'a': 1, 't': 3, 'e': 1, 'S': 1, 'r': 1, 'n': 1, 'g': 1}
import re

class CountException:
    def countExc(self, logs: str) -> dict:
        result = {}
        regPattern = r'\b\w+Exception\b'

        exceptionList = re.findall(regPattern, logs)

        for error in exceptionList:
            result[error] = result.get(error, 0) + 1

        return result
    
if __name__ == "__main__":
    count = CountException()
    print(count.countExc('2024-03-12 ERROR NullPointerException at line 52 2024-03-12 ERROR IOException connection reset 2024-03-12 ERROR NullPointerException at line 612024-03-12 ERROR TimeoutException request timed out'))


# Output: {'NullPointerException': 2, 'IOException': 1, 'TimeoutException': 1}
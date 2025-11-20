from typing import List

class ReorderLogFiles:
    """
    A class to reorder log files.

    Methods
    -------
    reorderLogFiles(logs: List[str]) -> List[str]:
        Reorders the given log files such that all letter-logs come before digit-logs.
        Letter-logs are sorted lexicographically by their contents, and in case of ties,
        by their identifiers. Digit-logs maintain their original order.
    """
    def reorderLogFiles(self, logs: List[str]):
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x.split(' ',1)[1], x.split()[0]))

        return letter_logs + digit_logs
    
if __name__=="__main__":
    reorder = ReorderLogFiles()
    print(reorder.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

    # Output: ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
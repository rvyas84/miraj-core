class CheckParentheses:
    """
    A class to check the validity of parentheses in a given string.

    Methods
    -------
    isValidParentheses(s: str) -> bool:
        Checks if the input string has valid parentheses.
    """

    def __init__(self):
        pass

    def isValidParentheses(self, s: str) -> bool:
        hashmap = {")":"(", "]":"[", "}":"{"}
        stk = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
        
        return not stk

if __name__ == "__main__":    
    par = CheckParentheses()
    print(par.isValidParentheses("[[]{{}}]")) # Return True
    print(par.isValidParentheses("[[]{{}}")) # Return False
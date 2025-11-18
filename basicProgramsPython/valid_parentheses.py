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
    
    def isValidPara(self, input: str) -> bool:
        if len(input) % 2 != 0:
            return False

        st = []

        for ch in input:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            elif (ch == ')' and st[-1] == '(' and st):
                st.pop()
            elif (ch == '}' and st[-1] == '{' and st):
                st.pop()
            elif (ch == ']' and st[-1] == '[' and st):
                st.pop()
            
        return len(st) == 0



if __name__ == "__main__":    
    par = CheckParentheses()
    print(par.isValidParentheses("[[]{{}}]")) # Return True
    print(par.isValidParentheses("[[]{{}}")) # Return False
    print(par.isValidPara("[[]{{}}]"))
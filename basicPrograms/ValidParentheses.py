class CheckParentheses:

    def __init__(self):
        pass

    def isValidParentheses(self, s: str) -> bool:
        hashmap = {")":"(", "]":"[", "}":"{"}
        stk = []

        for c in s:
            if c not in hashmap:
                stk.append(c)
                print(stk)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    print(f"After pop {stk}")
                    if popped != hashmap[c]:
                        return False
        
        return not stk
    
par = CheckParentheses()
print(par.isValidParentheses("[[]{{}}]"))
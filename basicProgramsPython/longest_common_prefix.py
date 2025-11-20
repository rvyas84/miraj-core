from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, input: List[str]) -> str:

        min_length = float('inf')

        for s in input:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in input:
                if s[i] != input[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]
    
if __name__ == "__main__":
    longPreFix = LongestCommonPrefix()
    print(longPreFix.longestCommonPrefix(["Flower", "Flow", "Flows"]))

# Output: Flow
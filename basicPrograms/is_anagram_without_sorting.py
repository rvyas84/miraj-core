class IsAnagram:

    def isAnagram(self, str1: str, str2: str) -> bool:
        
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")

        if len(str1) != len(str2):
            return False
        
        str1 = str1.lower()
        str2 = str2.lower()

        result = {}

        for ch in str1:
            result[ch] = result.get(ch, 0) + 1
        
        for ch in str2:
            if ch not in result:
                return False
            
            result[ch] -= 1

            if result[ch] == 0:
                del result[ch]
        
        return len(result) == 0
    
if __name__ == "__main__":
    isAna = IsAnagram()
    print(isAna.isAnagram("Life","File"))
    print(isAna.isAnagram("Life","Filf   "))
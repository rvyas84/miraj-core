class IsAnagram:
    
    def checkAnagram(self, s1: str, s2:str) -> bool:
        
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
        
        if len(s1) != len(s2):
            return False
        
        s1 = s1.lower()
        s2 = s2.lower()

        s1 = "".join(sorted(s1))
        s2 = "".join(sorted(s2))

        return s1 == s2

if __name__ == "__main__":
    isAna = IsAnagram()
    print(isAna.checkAnagram("Cat","Acd")) # False
    print(isAna.checkAnagram("Cat","ACT")) # True
    print(isAna.checkAnagram("Rat","ART")) #True
    print(isAna.checkAnagram("Rat","ART   ")) # True
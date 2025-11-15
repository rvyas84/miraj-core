class CheckPalindromeNumber:
    def is_num_pali(self, num: int) -> bool:

        if num < 0:
            return False

        div = 1

        while num >= 10 * div:
            div *= 10
        
        while num:
            right = num % 10
            left = num // div

            if right != left:
                return False
            
            num = (num % div) // 10 # type: ignore
            div = div /100

        return True
    
if __name__ == "__main__":
    pali = CheckPalindromeNumber()
    print(pali.is_num_pali(121))

# Output: True
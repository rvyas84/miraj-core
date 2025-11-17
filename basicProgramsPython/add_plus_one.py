from typing import List

class PlusOne:
    def plus_one(self, digits: List[int]) -> List[int]: # type: ignore

        for last_digit in range(len(digits) - 1, -1, -1):
            digits[last_digit] += 1
            
            # For digit is < 10 (without carry on)
            if digits[last_digit] < 10:
                return digits
            
            # else replce digit with 0
            digits[last_digit] = 0
        
        # [1] is a list containing a single element → 9
        return [1] + digits

if __name__ == '__main__':
    digits = [1,1,9,9]
    s = PlusOne()
    print(s.plus_one(digits))

# Output: [1,2,0,0]
class TwoSum:
    """
    A class to find two indices of numbers in a list that add up to a specific target.

    Methods
    -------
    twoSum(values: List[int], target: int) -> List[int]:
        Returns the indices of the two numbers such that they add up to the target.
    """

    def __init__(self):
        pass
    
    def twoSum(self, values, target):
        complement = 0
        result = {}

        if len(values) <= 0:
            print("List is empty")
        elif len(values) == 1:
            print("List has only 1 value")
        else:
            for i in range(len(values)):
                complement = int(target - values[i])

                if complement in result:
                    print(result)
                    return [i, result.get(complement)]
                
                result[values[i]] = i

            return ["No Value", "No Value"]

fn = TwoSum()
print(fn.twoSum([1,7,3,4,5,6,7,8,9,10], 12))

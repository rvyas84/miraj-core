from typing import List


class FindMedian:
    """
    A class to find the median of two sorted arrays.

    Methods
    -------
    findMedian(l1: List[int], l2: List[int]) -> float:
        Returns the median of two sorted arrays l1 and l2.
    """

    def __init__(self):
        pass

    def findMedian(self, l1: List[int], l2: List[int]) -> float: # type: ignore
        len1 = len(l1)
        len2 = len(l2)
        
        if len1 > len2:
            return self.findMedian(l2, l1)

        start = 0
        end = len1

        while start <= end:
            midL1 = (start + end) // 2
            midL2 = ((len1 + len2 + 1) // 2) - midL1

            maxLeftL1 = float('-inf') if midL1 == 0 else l1[midL1 - 1]
            minRightL1 = float('inf') if midL1 == len1 else l1[midL1]

            maxLeftL2 = float('-inf') if midL2 == 0 else l2[midL2 - 1]
            minRightL2 = float('inf') if midL2 == len2 else l2[midL2]

            if maxLeftL1 <= minRightL2 and maxLeftL2 <= minRightL1:
                if not ((len1 + len2) % 2) == 0:
                    return max(maxLeftL1, maxLeftL2)
                else:
                    return ((max(maxLeftL1, maxLeftL2) + min(minRightL1, minRightL2))/2)
            elif maxLeftL1 > minRightL2:
                end = midL1 - 1
            else:
                start = midL1 + 1

median = FindMedian()
print(median.findMedian([1,2,3,4,5,6,7],[8,9,10]))

# Output

# 5.5
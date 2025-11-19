import collections
from typing import List

class TopKElements:
    def topKElemNum(self, input: List[int], k: int):
        result_dic = collections.Counter(input)
        result_dic = sorted(result_dic, key = lambda x:result_dic[x], reverse = True)

        return result_dic[:k]
    
    def topKElemChar(self, input: str, k: int):
        result_dic = collections.Counter(input)
        result_dic = sorted(result_dic, key = lambda x:result_dic[x], reverse = True) # type: ignore

        return result_dic[:k]
    
if __name__ == "__main__":
    topK = TopKElements()
    print(topK.topKElemNum([1,1,1,1,1,2,2,2,3,3,4,5,5,5,5,5,5,5], 3)) # Output: [5, 1, 2]
    print(topK.topKElemChar("iiisssttm", 2)) # Output: ['i', 's']
    print(topK.topKElemChar("i", 2)) # Output: ['i']
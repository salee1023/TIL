import numpy as np
def solution(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)

    answer = (A+B).tolist()
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
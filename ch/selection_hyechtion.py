

def select_sort(arr: list[int]) -> list[int]:
    res = arr.copy()
    for i in range(0, len(res)):
        smallestIdx = i
        for j in range(i+1, len(res)):
            if res[smallestIdx] > res[j]:
                smallestIdx = j
        if smallestIdx != i:
            res[smallestIdx], res[i] = res[i], res[smallestIdx]
    return res


print(select_sort([1, 3, 100, 24, 13, 18, 22]))

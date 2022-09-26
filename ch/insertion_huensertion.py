def insert_sort(arr: list[int]) -> list[int]:
    res = arr.copy()
    for pointer in range(1, len(res)):
        tmp = res[pointer]
        gap_index = pointer
        i = gap_index - 1
        while i >= 0:
            if res[i] > tmp:
                res[i], res[gap_index] = res[gap_index], res[i]
                gap_index = i
            else:
                break
            i -= 1
        res[gap_index] = tmp
    return res


print(insert_sort([1, 3, 100, 24, 13, 18, 22]))

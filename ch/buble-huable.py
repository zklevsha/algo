

def bubble_sort(arr: list[int]) -> list[int]:
    unsorted_initl_indx = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, unsorted_initl_indx):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        unsorted_initl_indx -= 1
    return arr

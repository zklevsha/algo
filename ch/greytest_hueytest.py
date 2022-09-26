# The following function finds the greatest single number within an array,
# but has an efficiency of O(N2). Rewrite the function so that it becomes a
# speedy O(N):

def greatestNumberQuadratic(array):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True

        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                isIValTheGreatest = False

        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i


def greatestNumberLinear(array) -> int:
    greates = array[0]
    for i in range(1, len(array)):
        if array[i] > greates:
            greates = array[i]
    return greates


arr = [1, 5, 100, 30, 49, 1000]
print(greatestNumberLinear(arr))
print(greatestNumberQuadratic(arr))
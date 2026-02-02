# FASTER
def insertion_sort(array):
    """Time Complexity O(n*n)"""
    for i in range(1, len(array)):
        current_element = array[i]

        j = i - 1
        while j >= 0 and current_element < array[j]:
            # right shift all the elements as we need one space to put the current_element
            array[j + 1] = array[j]   # shifting
            j -= 1

        # the value of `j` for which the while condintion fails
        # is the value of the range (inclusive) where the items are already sorted, so
        # `j + 1` th index is the position that needs to be updated to
        # sort the array till the index position `i`
        array[j + 1] = current_element

    return array



# SLOWER
def insertion_sort2(array):
    """Time Complexity O(n*n)"""
    for i in range(1, len(array)):
        current_element = array[i]

        for j in range(i - 1, -1, -1):
            if current_element < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]   # swapping
            else: break

    return array



"""
PERFORMANCE COMPARISON
============================================================

Size       Swap (ms)       Shift (ms)      Difference
------------------------------------------------------------
10         0.0069          0.0043          +61.1%
50         0.0758          0.0613          +23.7%
100        0.2570          0.2069          +24.2%
500        6.0198          4.1769          +44.1%
1000       20.5159         13.4861         +52.1%
"""

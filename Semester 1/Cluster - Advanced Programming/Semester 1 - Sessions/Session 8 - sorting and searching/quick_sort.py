def partition(lst, low, high):
  
    # Choosing the pivot
    pivot = lst[high]
    
    i = low - 1
    
    # Traverse the lst and move all smaller
    # elements on the left side. 
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    
    # Move pivot after smaller elements and
    # return its position
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

# The QuickSort function implementation
def quick_sort(lst, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pivot_index = partition(lst, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(lst, low, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, high)

# Function to print an list
def print_list(lst):
    for i in lst:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 11, 90]
    print("Given list is")
    print_list(lst)

    quick_sort(lst, 0, len(lst) - 1)

    print("\nSorted list is")
    print_list(lst)

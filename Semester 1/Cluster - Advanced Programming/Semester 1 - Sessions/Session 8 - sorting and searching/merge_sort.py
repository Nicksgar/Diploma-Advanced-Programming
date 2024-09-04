def merge(lst, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp lists
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp lists L[] and R[]
    for i in range(n1):
        L[i] = lst[left + i]
    for j in range(n2):
        R[j] = lst[mid + 1 + j]

    i = 0  # Initial index of first sublist
    j = 0  # Initial index of second sublist
    k = left  # Initial index of merged sublist

    # Merge the temp lists back
    # into list[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1

def merge_sort(lst, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)

def print_list(lst):
    for i in lst:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 11, 90]
    print("Given list is")
    print_list(lst)

    merge_sort(lst, 0, len(lst) - 1)

    print("\nSorted list is")
    print_list(lst)

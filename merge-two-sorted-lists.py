# One of the most efficient sorting algorithm is the merge sort algorithm. 
# Merge sort has two phases: the dividing phase and the merge phase.
# Write a mergeTwoLists() function with two parameters list1 and list2. The lists of numbers
# passed for these parameters are already in sorted order from smallest to largest number.
# The function returns a single list of all numbers from these two lists.


def main() -> None:
    print(mergeTwoLists([1, 3, 6, 10, 11], [5, 7, 8, 9]))


def mergeTwoLists(list1, list2) -> list[int]:
    
    merge_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    
    if i < len(list1):
        for k in range(i, len(list1)):
            merge_list.append(list1[k])

    if j < len(list2):
        for k in range(j , len(list2)):
            merge_list.append(list2[k])


    return merge_list




if __name__ == "__main__":
    main()

# Write a function called findMaxNumber that takes in an array of numbers 
# and returns the largest number in the array.

def main() -> None:
    print(find_max_number([2,1,3,4,2,5,6]))

def find_max_number(arr) -> int:

    largest_num: int = arr[0]
    
    for num in range(1, len(arr)):
        if arr[num] > largest_num:
            largest_num = arr[num]


    return largest_num
            


if __name__ == "__main__":
    main()
def insertion_sort(numbers):
    # Traverse from 1 to len(numbers)
    # We start at 1 because we assume the first element (index 0) is already "sorted"
    for i in range(1, len(numbers)):
        
        key = numbers[i]
        j = i - 1
        
        # Move elements of numbers[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
            
        # Place the key at its correct position
        numbers[j + 1] = key
            
    return numbers

if __name__ == "__main__":
    try:
        user_input = input("Enter integer number with space: ")
        # .split() handles the spaces between numbers
        numbers = list(map(int, user_input.split()))
        
        sorted_numbers = insertion_sort(numbers)
        print("Sorted number is", sorted_numbers)
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
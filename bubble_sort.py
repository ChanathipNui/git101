def bubble_sort(numbers):
    n = len(numbers)
    
    # Traverse through all array elements
    for i in range(n):
        # optimization: keep track if any swap happened
        swapped = False
        
        # Last i elements are already in place, so we check up to n-i-1
        for j in range(0, n - i - 1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then the list is sorted
        if not swapped:
            break
            
    return numbers

if __name__ == "__main__":
    # Added .split() to correctly separate the numbers by space
    try:
        user_input = input("Enter integer number with space: ")
        numbers = list(map(int, user_input.split()))
        
        sorted_numbers = bubble_sort(numbers)
        print("Sorted number is", sorted_numbers)
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
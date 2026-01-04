def selection_sort(numbers):
    n = len(numbers)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
            
    return numbers

if __name__ == "__main__":
    try:
        user_input = input("Enter integer number with space: ")
        # .split() handles the spaces between numbers
        numbers = list(map(int, user_input.split()))
        
        sorted_numbers = selection_sort(numbers)
        print("Sorted number is", sorted_numbers)
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
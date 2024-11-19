def NumberChecker():
    while True:
        try:
            # Get user input and split it into a list of numbers (as strings)
            numbers = input("Enter numbers separated by spaces: ").split()

            # Convert the numbers from strings to integers for validation
            int_numbers = [int(num) for num in numbers]

            # Check if all numbers are different by comparing the length of the list and the set
            if len(int_numbers) == len(set(int_numbers)):
                print("Numbers are different from each other:", int_numbers)
                break

            else:
                print("There are duplicates")
                break
            
        
        except ValueError:
            # Handle cases where the input contains non-numeric values
            print("Invalid input! Please enter valid numbers.")
            break

# Call the function
NumberChecker()

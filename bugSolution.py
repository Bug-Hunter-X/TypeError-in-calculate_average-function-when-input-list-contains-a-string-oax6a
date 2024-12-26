def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage
my_list = [10, 20, "30", 40]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list_2 = [10,20,30,40]
result2 = calculate_average(my_list_2)
print(f"The average is: {result2}")

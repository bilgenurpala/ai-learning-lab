#  Debugging Challenge

# Bug 1 - FizzBuzz
# Bug: Missing colon at the end of elif number % 5 == 0
# Bug: return number should be return str(number) to keep return type consistent

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:        # added missing colon
        return "Buzz"
    else:
        return str(number)       # consistent return type

# Bug 2 - Celsius to Fahrenheit
# Bug: celsius_to_fahrenheit is a function reference, not a function call
# Fix: celsius_to_fahrenheit(temp) instead of celsius_to_fahrenheit

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperatures = [0, 20, 37, 100]
for temp in temperatures:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")  # added (temp)

# Bug 3 - Find average
# Bug: + 1 at the end of return statement incorrectly adds 1 to the average

def find_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # removed incorrect + 1

print(find_average([10, 20, 30]))  # Output: 20.0
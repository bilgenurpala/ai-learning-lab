# Caesar Cipher

# Rules:
# - Create a function called `caesar(text, shift, direction)`
# - `direction` can be `"encode"` or `"decode"`
# - Shift each letter in the text by the given number
# - Numbers and symbols stay unchanged
# - Ask the user for direction, text and shift amount
# - Keep looping until the user types `"no"` to quit

# Example:
# ```
# Type 'encode' or 'decode': encode
# Type your message: hello
# Type the shift number: 3
# Result: khoor

def caesar(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if direction == "decode":
                shift_amount = -shift_amount
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

while True:
    direction = input("Type 'encode' or 'decode': ")
    if direction not in ["encode", "decode"]:
        print("Invalid direction. Please try again.")
        continue
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    result = caesar(text, shift, direction)
    print(f"Result: {result}")
    if input("Type 'no' to quit or press Enter to continue: ").lower() == "no":
        break


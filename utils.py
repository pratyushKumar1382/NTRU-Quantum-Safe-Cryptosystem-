def string_to_encoded_array(s):
    encoded_array = []
    for char in s:
        # Get ASCII value
        ascii_value = ord(char)
        # Get 8-bit binary representation, pad with zeros if necessary
        binary_rep = format(ascii_value, '08b')
        # Convert binary to encoded array
        for bit in binary_rep:
            if bit == '1':
                encoded_array.append(1)
            else:
                encoded_array.append(0)
        # Introduce -1 after each character's bits
        encoded_array.append(-1)
    return encoded_array

def encoded_array_to_string(encoded_array):
    decoded_string = ""
    current_byte = ""
    for num in encoded_array:
        if num == -1:
            if current_byte:
                # Convert binary string to ASCII character
                ascii_value = int(current_byte, 2)
                decoded_string += chr(ascii_value)
                current_byte = ""
        else:
            current_byte += str(num)
    # Handle any remaining byte (in case there's no trailing -1)
    if current_byte:
        ascii_value = int(current_byte, 2)
        decoded_string += chr(ascii_value)
    return decoded_string

# Example usage:
# original_string = "Hello"
# encoded = string_to_encoded_array(original_string)
# print(f"Encoded: {encoded}")

# decoded = encoded_array_to_string(encoded)
# print(f"Decoded: {decoded}")



if __name__ == "__main__":
    print(encode("hello"))
    print(type(encode("hello")))

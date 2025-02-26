#!/usr/bin/env python3
import base64

def caesar_decipher(text, shift):
    """Decipher text encrypted with Caesar cipher using the given shift."""
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the shift (add 26 to handle negative shifts)
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def main():
    # Step 1: Read the encoded content
    encoded_data = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
    print(f"Encoded data: {encoded_data}")

    # Step 2: First layer of Base64 decoding
    first_decode = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
    print(f"First decode: {first_decode}")

    # Step 3: Extract the content from the Python byte string format
    # The format is b'...' so we extract between positions 2 and -2
    # (-2 instead of -1 to account for the quote and possible newline)
    inner_content = first_decode[2:-2]
    print(f"Inner content: {inner_content}")

    # Step 4: Second layer of Base64 decoding
    second_decode = base64.b64decode(inner_content).decode('utf-8')
    print(f"Second decode: {second_decode}")

    # Step 5: Try all possible Caesar shifts (0-25)
    print("\nTrying all Caesar shifts:")
    flag_found = False
    for shift in range(26):
        deciphered = caesar_decipher(second_decode, shift)
        # Print all shifts but highlight the one that looks like a flag
        if "picoCTF{" in deciphered:
            print(f"Shift {shift} (FOUND FLAG): {deciphered}")
            flag_found = True
        else:
            print(f"Shift {shift}: {deciphered}")
    
    if flag_found:
        print("\nSummary of decoding process:")
        print("1. Base64 decode the original string")
        print("2. Extract the content from Python byte string format")
        print("3. Base64 decode the extracted content")
        print("4. Apply Caesar cipher decryption with shift 7")
        print(f"\nThe flag is: {caesar_decipher(second_decode, 7)}")

if __name__ == "__main__":
    main()
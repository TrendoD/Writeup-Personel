#!/usr/bin/env python3

def gray_code(i):
    """Binary Reflected Gray Code (BRGC) implementation"""
    return i ^ (i >> 1)

def decrypt_flag():
    # The encrypted flag from the server
    encrypted_flag = "60797d6e6c455d490d41774a1b4e1d705e1c155314557d415452075211573957033b0459015e5b16"
    
    # The FLAG_OFFSET we determined from solving the Tower of Hanoi puzzle
    offset = 38  # Binary: 0b100110
    
    # Convert hex to bytes
    encrypted = bytes.fromhex(encrypted_flag)
    decrypted = bytearray()
    
    # Decrypt using Gray code as the key generation function
    for i, byte in enumerate(encrypted):
        key = gray_code(i + offset) & 0xFF
        decrypted.append(byte ^ key)
    
    # Convert to ASCII
    return decrypted.decode('ascii')

if __name__ == "__main__":
    flag = decrypt_flag()
    print(f"Flag: {flag}")
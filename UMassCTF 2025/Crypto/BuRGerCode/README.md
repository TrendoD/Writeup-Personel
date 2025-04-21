# BuRGerCode - Crypto Challenge

## Challenge Overview
- **Category:** Crypto
- **Points:** 100
- **Description:** You need to decode the BuRGerCode to recover the flag.

## Initial Analysis
- The challenge provides a partial source code and a server connection
- The code reveals a custom encryption scheme called "BuRGerCode"
- A Tower of Hanoi puzzle is used to derive a key offset

## The Encryption
```python
def encrypt(message: bytes, offset = FLAG_OFFSET) -> str:
    encrypted = bytearray()
    for (i, char) in enumerate(message):
        encrypted.append(char ^ (key_gen_func(i + offset) & 0xFF))
    return encrypted.hex()
```

## Key Insights
1. The name "BuRGerCode" with capitalized "R" and "G" hints at **Binary Reflected Gray Code** (BRGC)
2. Gray code is a binary numeral system where two successive values differ by only one bit
3. The key generation function is: `i ^ (i >> 1)`
4. By solving the Tower of Hanoi puzzle, we learned the FLAG_OFFSET is 38

## Decryption Solution
```python
def gray_code(i):
    return i ^ (i >> 1)

def decrypt_flag():
    encrypted_flag = "60797d6e6c455d490d41774a1b4e1d705e1c155314557d415452075211573957033b0459015e5b16"
    offset = 38
    
    encrypted = bytes.fromhex(encrypted_flag)
    decrypted = bytearray()
    
    for i, byte in enumerate(encrypted):
        key = gray_code(i + offset) & 0xFF
        decrypted.append(byte ^ key)
    
    return decrypted.decode('ascii')

print(decrypt_flag())
```

## Flag
`UMASS{gr4y_c0d3_s01v3s_burg3r5_0f_h4n01}`
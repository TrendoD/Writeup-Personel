# Mod 26 - picoCTF Challenge Writeup

## Introduction
Mod 26 is a beginner-friendly cryptography challenge that introduces participants to ROT13, a simple substitution cipher based on letter rotation in the alphabet.

## Challenge Description
The challenge presents us with the following:

> Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}`

This challenge focuses on ROT13 (Rotation 13), a basic substitution cipher named after its technique of rotating each letter by 13 positions in the alphabet. The name "Mod 26" refers to modular arithmetic with the 26 letters of the English alphabet, which is the mathematical foundation of rotation ciphers.

## Solution Process

### Understanding ROT13
Before solving, let's understand what ROT13 is:

- ROT13 is a special case of the Caesar cipher where each letter is shifted by 13 positions
- It's mathematically expressed as: `(x + 13) mod 26` for encryption
- For decryption, we apply the same transformation (adding 13 again)
- Since the English alphabet has 26 letters, rotating by 13 twice gets you back to the original text
- The mapping works as follows:
  - A → N, B → O, C → P, etc.
  - N → A, O → B, P → C, etc.
- Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged

### Decryption Method
To decrypt the given ciphertext, we need to apply ROT13 to each alphabetic character. There are multiple ways to accomplish this:

#### Manual Decryption
We could create a lookup table and translate each character manually:

```
Original: ABCDEFGHIJKLMNOPQRSTUVWXYZ
ROT13:    NOPQRSTUVWXYZABCDEFGHIJKLM
```

#### Using Command Line Tools
On Unix/Linux systems, we can use the `tr` command:

```bash
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

#### Using Python
A simple Python script can perform the decryption:

```python
def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            result += chr(rotated)
        else:
            result += char
    return result

encrypted = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
decrypted = rot13(encrypted)
print(decrypted)
```

#### Using Online Tools
Numerous websites offer ROT13 decoding services, such as CyberChef, which can quickly process the text.

### Applying the Decryption
Let's decrypt the given ciphertext: `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}`

Applying ROT13 transformation:
- "cvpb" → "pico"
- "PGS" → "CTF"
- "{" remains "{" (non-alphabetic)
- "arkg" → "next"
- "_" remains "_" (non-alphabetic)
- "gvzr" → "time"
- "_" remains "_" (non-alphabetic)
- "V'yy" → "I'll"
- "_" remains "_" (non-alphabetic)
- "gel" → "try"
- "_" remains "_" (non-alphabetic)
- "2" remains "2" (non-alphabetic)
- "_" remains "_" (non-alphabetic)
- "ebhaqf" → "rounds"
- "_" remains "_" (non-alphabetic)
- "bs" → "of"
- "_" remains "_" (non-alphabetic)
- "ebg13" → "rot13"
- "_" remains "_" (non-alphabetic)
- "nSkgmDJE" → "aFxtzQWR"
- "}" remains "}" (non-alphabetic)

The decrypted text is:
`picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}`

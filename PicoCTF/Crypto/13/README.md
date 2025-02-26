# CTF Challenge Writeup: 13

## Introduction
Challenge "13" is a simple cryptography problem that introduces participants to the ROT13 cipher, requiring decryption of an encoded message to retrieve the flag.

## Challenge Description
The challenge presents us with the following text:

```
Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`
```

ROT13 (short for "rotate by 13 places") is a simple letter substitution cipher that replaces each letter with the letter 13 positions after it in the alphabet. It's a special case of the Caesar cipher, developed in ancient Rome.

What makes ROT13 interesting is that the alphabet has 26 letters, and 13 is exactly half of that. This means applying ROT13 twice returns the original text - it's its own inverse operation. Because of this property, it has historically been used in online forums to hide potential spoilers or punchlines, rather than for serious security purposes.

## Solution Process

### Understanding ROT13

In ROT13:
- 'A' becomes 'N', 'B' becomes 'O', and so on
- 'N' becomes 'A', 'O' becomes 'B', and so on
- Lowercase letters follow the same pattern ('a' → 'n', etc.)
- Non-alphabetic characters remain unchanged

This can be visualized as:
```
Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:   NOPQRSTUVWXYZABCDEFGHIJKLM
```

### Method 1: Manual Decryption

We can decrypt the ciphertext `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}` character by character:

- c → p  (c + 13 in the alphabet)
- v → i
- p → c
- b → o
- P → C
- G → T
- S → F
- { → {  (non-alphabet characters stay the same)
- a → n
- b → o
- g → t
- _ → _
- g → t
- b → o
- b → o
- _ → _
- o → b
- n → a
- q → d
- _ → _
- b → o
- s → f
- _ → _
- n → a
- _ → _
- c → p
- e → r
- b → o
- o → b
- y → l
- r → e
- z → m
- } → }

Putting this all together, we get: `picoCTF{not_too_bad_of_a_problem}`

### Method 2: Using Command Line Tools

We can use the `tr` command in Linux/Unix to perform ROT13:

```bash
echo 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

Output:
```
picoCTF{not_too_bad_of_a_problem}
```

### Method 3: Using Python

```python
def rot13(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
plaintext = rot13(ciphertext)
print(plaintext)  # Outputs: picoCTF{not_too_bad_of_a_problem}
```

### Method 4: Using Online Tools

There are numerous online tools available for ROT13 decoding, such as:
- [CyberChef](https://gchq.github.io/CyberChef/)
- [rot13.com](https://rot13.com/)

Simply input the ciphertext and the tool will output the plaintext.

## Flag 

```
picoCTF{not_too_bad_of_a_problem}
```

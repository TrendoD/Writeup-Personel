# Interencdec - picoCTF 2024 Writeup

## Challenge Information
- **Name**: interencdec
- **Category**: Cryptography
- **Difficulty**: Easy
- **Author**: NGIRIMANA SCHADRACK
- **Tags**: picoCTF 2024, base64, caesar, browser_webshell_solvable

## Challenge Description

The challenge presents us with a file containing encoded content. According to the description:

> Can you get the real meaning from this file.

A hint is also provided:

> Engaging in various decoding processes is of utmost importance

The encoded content provided in the file is:
```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
```

## Introduction

"interencdec" is a crypto challenge from picoCTF 2024 that tests participants' ability to decode multiple layers of encoding and encryption to uncover a hidden flag. This writeup details the step-by-step process of solving this challenge, which involves peeling back several layers of data transformation using Python.

## Solution Process

To solve this challenge, I created a Python script that methodically applies various decoding techniques to uncover the hidden flag.

### Step 1: Initial Base64 Decoding

Looking at the encoded content, the presence of alphanumeric characters and "==" padding at the end indicates base64 encoding. Our first step is to decode this first layer using Python's `base64` module:

```python
import base64

encoded_data = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
first_decode = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
print(f"First decode: {first_decode}")
```

Output:
```
First decode: b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='
```

### Step 2: Analyzing the First Decode

The output of our first decode looks like a Python byte string (indicated by the `b'...'` format). This is a common representation for binary data in Python.

To proceed, we need to extract the content between the `b'` prefix and the trailing `'` character:

```python
# Extract the content from the Python byte string format
inner_content = first_decode[2:-2]
print(f"Inner content: {inner_content}")
```

This gives us:
```
Inner content: d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==
```

### Step 3: Second Layer of Base64 Decoding

The extracted content still has the characteristics of base64 encoding (alphanumeric character set and "==" padding at the end). Let's decode this second layer:

```python
second_decode = base64.b64decode(inner_content).decode('utf-8')
print(f"Second decode: {second_decode}")
```

Result:
```
Second decode: wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}
```

### Step 4: Identifying and Applying Caesar Cipher Decryption

The output from our second decode looks promising - it has the structure of a CTF flag with curly braces `{}`, but the content is still encrypted. Given the "caesar" tag in the challenge description, it's likely a Caesar cipher was applied.

The Caesar cipher is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet. To find the correct shift, we'll try all possible values (0-25):

```python
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

# Try all possible shifts (0-25)
for shift in range(26):
    deciphered = caesar_decipher(second_decode, shift)
    if "picoCTF{" in deciphered:
        print(f"Shift {shift} (FOUND FLAG): {deciphered}")
    else:
        print(f"Shift {shift}: {deciphered}")
```

Running this code produces 26 different outputs, one for each possible shift. At shift 7, we find:

```
Shift 7 (FOUND FLAG): picoCTF{caesar_d3cr9pt3d_890d2379}
```

This matches the expected format for a picoCTF flag, so we've found our solution!

### Step 5: Verification and Summary

Let's summarize the decoding process:

1. **First Layer**: Base64 decode `YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==`  
   Result: `b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='`

2. **Extract Content**: Remove Python byte string formatting `b'...'`  
   Result: `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==`

3. **Second Layer**: Base64 decode the extracted content  
   Result: `wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}`

4. **Final Layer**: Apply Caesar cipher decryption with shift 7  
   Result: `picoCTF{caesar_d3cr9pt3d_890d2379}`

## Complete Python Solution

Here's the complete Python script that implements all the steps described above:

```python
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
```

## Running the Script

When you run the script, you get the following output:

```
Encoded data: YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
First decode: b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='
Inner content: d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==  
Second decode: wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}

Trying all Caesar shifts:
Shift 0: wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}
Shift 1: voiuIZL{igkygx_j3ix9vz3j_890j2379}
Shift 2: unhtHYK{hfjxfw_i3hw9uy3i_890i2379}
Shift 3: tmgsGXJ{geiwev_h3gv9tx3h_890h2379}
Shift 4: slfrFWI{fdhvdu_g3fu9sw3g_890g2379}
Shift 5: rkeqEVH{ecguct_f3et9rv3f_890f2379}
Shift 6: qjdpDUG{dbftbs_e3ds9qu3e_890e2379}
Shift 7 (FOUND FLAG): picoCTF{caesar_d3cr9pt3d_890d2379}
Shift 8: ohbnBSE{bzdrzq_c3bq9os3c_890c2379}
Shift 9: ngamARD{aycqyp_b3ap9nr3b_890b2379}
Shift 10: mfzlZQC{zxbpxo_a3zo9mq3a_890a2379}
Shift 11: leykYPB{ywaown_z3yn9lp3z_890z2379}
Shift 12: kdxjXOA{xvznvm_y3xm9ko3y_890y2379}
Shift 13: jcwiWNZ{wuymul_x3wl9jn3x_890x2379}
Shift 14: ibvhVMY{vtxltk_w3vk9im3w_890w2379}
Shift 15: haugULX{uswksj_v3uj9hl3v_890v2379}
Shift 16: gztfTKW{trvjri_u3ti9gk3u_890u2379}
Shift 17: fyseSJV{squiqh_t3sh9fj3t_890t2379}
Shift 18: exrdRIU{rpthpg_s3rg9ei3s_890s2379}
Shift 19: dwqcQHT{qosgof_r3qf9dh3r_890r2379}
Shift 20: cvpbPGS{pnrfne_q3pe9cg3q_890q2379}
Shift 21: buoaOFR{omqemd_p3od9bf3p_890p2379}
Shift 22: atnzNEQ{nlpdlc_o3nc9ae3o_890o2379}
Shift 23: zsmyMDP{mkockb_n3mb9zd3n_890n2379}
Shift 24: yrlxLCO{ljnbja_m3la9yc3m_890m2379}
Shift 25: xqkwKBN{kimaiz_l3kz9xb3l_890l2379}

Summary of decoding process:
1. Base64 decode the original string
2. Extract the content from Python byte string format
3. Base64 decode the extracted content
4. Apply Caesar cipher decryption with shift 7

The flag is: picoCTF{caesar_d3cr9pt3d_890d2379}
```

## Flag

The flag for this challenge is:

```
picoCTF{caesar_d3cr9pt3d_890d2379}
```

*This writeup was created for educational purposes to help others learn from this CTF challenge.*
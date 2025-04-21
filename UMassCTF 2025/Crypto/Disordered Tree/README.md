# Disordered Tree - Crypto Challenge

## Challenge Overview
- **Category:** Crypto
- **Points:** 352
- **Description:** The (key distribution) tree is speaking to me. This is not good. Please send help.

## Files
- `output.txt`: Contains RSA parameters, a timestamp, keys, and encrypted flag
- `redacted_source.py`: Shows the encryption algorithm

## Solution

### Understanding the Challenge
This challenge implements a tree-based key distribution scheme using RSA. The encryption uses:
- Function `f(block)`: Modular exponentiation with exponent `fe`
- Function `g(block)`: Modular exponentiation with exponent `ge`

The timestamp bits determine whether `f` or `g` is applied at each step to encrypt a master key.

### Vulnerability
The scheme is vulnerable because:
1. It includes many intermediate key prefixes in the output
2. We can find the closest prefix to our target timestamp
3. We only need to apply the remaining operations for the missing bits

### Exploitation Steps
1. Parse all parameters from `output.txt`
2. Find the key prefix that matches the most bits of the target timestamp
3. Apply the remaining operations (f or g) based on the remaining timestamp bits
4. XOR the result with the encrypted flag to get the plaintext

### Solution Code
```python
# Load the output file
with open('output.txt', 'r') as f:
    lines = f.read().splitlines()

# Extract key values
n = int(lines[0].split('=', 1)[1], 16)
fe = int(lines[1].split('=', 1)[1], 16)
ge = int(lines[2].split('=', 1)[1], 16)
now = lines[3].split('=', 1)[1]
flag_ct = int(lines[-1].split('=', 1)[1], 16)

# Build map of prefixes to keys
key_lines = []
i = lines.index('keys:') + 1
while i < len(lines) - 1:
    if i + 1 < len(lines) and lines[i+1].startswith('0x'):
        prefix = lines[i]
        key_value = int(lines[i+1], 16)
        key_lines.append((prefix, key_value))
        i += 2
    else:
        i += 1

# Find prefix with most matching bits
prefix_match = []
for prefix, key_value in key_lines:
    match_len = 0
    for i in range(min(len(prefix), len(now))):
        if prefix[i] == now[i]:
            match_len += 1
        else:
            break
    prefix_match.append((match_len, prefix, key_value))

prefix_match.sort(reverse=True)
best_match = prefix_match[0]
match_len, prefix, key_value = best_match

# Apply remaining bits
block = key_value
remaining_bits = now[len(prefix):]
for bit in remaining_bits:
    block = pow(block, fe if bit == '1' else ge, n)

# Decrypt the flag
flag_int = block ^ flag_ct
flag_bytes = flag_int.to_bytes((flag_int.bit_length() + 7) // 8, 'big')
flag = flag_bytes.decode('ascii')
print(flag)
```

## Flag
`UMASS{perhaps_dont_be_using_commutative_encryption}`
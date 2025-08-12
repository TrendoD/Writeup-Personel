# WHY2025 CTF TIMES Challenge Writeup

## Challenge Summary
- Website: https://why2025-ctf-times.ctf.zone/
- Challenge involves a paywall and obfuscated JavaScript: `paywall.min.js`

## Steps Taken
1. **Source Code Analysis**
   - Inspected the website source and found `paywall.min.js`.
   - The JavaScript was heavily obfuscated.

2. **Reverse Engineering**
   - Deobfuscated the code to reveal its logic.
   - The script draws text on a canvas, including the flag.

3. **Flag Extraction**
   - The flag is revealed in the code and rendered on the page:

```
flag{2d582cd42552e765d2658a14a0a25755}
```

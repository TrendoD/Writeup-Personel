# Shoe Shop 1.0 Challenge Writeup

## Challenge Summary
- Website: shoe-shop-1.ctf.zone
- Functionality: Register, login, shop for shoes, view cart

## Steps Taken
1. **Register and Login**
   - Created a user account and logged in.

2. **Cart Manipulation**
   - Noticed the cart page endpoint: `index.php?page=cart&id=3489`
   - Challenge hint: Admin has already taken the exclusive shoe (sold out)
   - Changed the cart `id` parameter to `1` to access the admin's cart

3. **Flag Retrieval**
   - Accessing cart with `id=1` revealed the flag.
   ![Screenshot](image.png)

## Flag
```
flag{00f34f9c417fcaa72b16f79d02d33099}
```


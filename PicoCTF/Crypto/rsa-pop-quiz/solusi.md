# RSA Pop Quiz - picoCTF Writeup

## Challenge Overview

RSA Pop Quiz is a cryptography challenge from picoCTF 2019 that tests understanding of RSA encryption concepts. The challenge presents a series of problems related to RSA theory and implementation, each requiring calculation of different RSA parameters. Successfully answering all problems reveals the flag.

**Challenge Description:**
> Class, take your seats! It's PRIME-time for a quiz...

**Target Server:** jupiter.challenges.picoctf.org:1981

## RSA Background

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem widely used for secure data transmission. It relies on the practical difficulty of factoring the product of two large prime numbers.

Key RSA components:
- p, q: Two large prime numbers (kept secret)
- n: Modulus (n = p × q), part of both public and private keys
- e: Public exponent, commonly 65537
- d: Private exponent (kept secret)
- φ(n): Euler's totient function, calculated as (p-1) × (q-1)

## Problem Solutions

### Problem 1: Calculate n given p and q

**Given:**
- p = 76753
- q = 60413

**Task:** Calculate n

**Solution:**
In RSA, n is simply the product of p and q.

n = p × q = 76753 × 60413 = 4,636,878,989

**Concept tested:** Basic RSA parameter relationships

### Problem 2: Calculate q given p and n

**Given:**
- p = 54269
- n = 5051846941

**Task:** Calculate q

**Solution:**
Since n = p × q, we can rearrange to find q = n/p

q = n ÷ p = 5051846941 ÷ 54269 = 93089

**Concept tested:** RSA parameter relationships and divisibility

### Problem 3: Factoring a large n

**Given:**
- e = 3
- n = (very large number, 617 digits)

**Task:** Find q and p

**Solution:**
Factoring a 617-digit number into its prime components is computationally infeasible with current technology. This is the security foundation of RSA.

Answer: Not feasible (N)

**Concept tested:** RSA security relies on the hardness of integer factorization

### Problem 4: Calculate Euler's Totient

**Given:**
- p = 12611
- q = 66347

**Task:** Calculate totient(n)

**Solution:**
For RSA, the totient function φ(n) = (p-1) × (q-1)

φ(n) = (12611-1) × (66347-1) = 12610 × 66346 = 836,623,060

**Concept tested:** Euler's Totient function calculation for RSA

### Problem 5: RSA Encryption

**Given:**
- plaintext = 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717
- e = 3
- n = (very large number)

**Task:** Calculate ciphertext

**Solution:**
In RSA, encryption is calculated as c = m^e mod n, where m is the plaintext:

ciphertext = plaintext^3 mod n

**Concept tested:** RSA encryption formula

### Problem 6: RSA Decryption (Cube Root Attack)

**Given:**
- ciphertext = 107524013451079348539944510756143604203925717262185033799328445011792760545528944993719783392542163428637172323512252624567111110666168664743115203791510985709942366609626436995887781674651272233566303814979677507101168587739375699009734588985482369702634499544891509228440194615376339573685285125730286623323
- e = 3
- n = (very large number)

**Task:** Recover plaintext

**Solution:**
Without the private key, standard RSA decryption isn't feasible. However, there was a potential vulnerability with e=3 if the ciphertext is the result of a plaintext that wasn't properly reduced modulo n. We checked for a perfect cube root, but it wasn't vulnerable.

Answer: Not feasible without private key (N)

**Concept tested:** Limitations of RSA decryption without private key and potential small exponent attacks

### Problem 7: Calculate Private Key d

**Given:**
- p = 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
- q = 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
- e = 65537

**Task:** Calculate d

**Solution:**
The private key d is calculated as the modular multiplicative inverse of e modulo φ(n).

1. Calculate φ(n) = (p-1) × (q-1)
2. Calculate d such that (d × e) ≡ 1 (mod φ(n))

This is accomplished using the extended Euclidean algorithm.

**Concept tested:** RSA private key generation

### Problem 8: Decryption with Partial Key Information

**Given:**
- p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
- ciphertext = 18031488536864379496089550017272599246134435121343229164236671388038630752847645738968455413067773166115234039247540029174331743781203512108626594601293283737392240326020888417252388602914051828980913478927759934805755030493894728974208520271926698905550119698686762813722190657005740866343113838228101687566611695952746931293926696289378849403873881699852860519784750763227733530168282209363348322874740823803639617797763626570478847423136936562441423318948695084910283653593619962163665200322516949205854709192890808315604698217238383629613355109164122397545332736734824591444665706810731112586202816816647839648399
- e = 65537
- n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239

**Task:** Decrypt ciphertext

**Solution:**
1. Calculate q = n/p
2. Calculate φ(n) = (p-1) × (q-1)
3. Calculate d = e^(-1) mod φ(n)
4. Decrypt: plaintext = ciphertext^d mod n

The plaintext decrypts to reveal the flag: `picoCTF{wA8_th4t$_ill3aGal..ode01e4bb}`

**Concept tested:** Practical RSA decryption when one factor is known

## Final Flag

**Flag:** `picoCTF{wA8_th4t$_ill3aGal..ode01e4bb}`

im also make the fully automated script for this challenge https://github.com/TrendoD/Writeup-Personel/blob/main/PicoCTF/Crypto/rsa-pop-quiz/script.py

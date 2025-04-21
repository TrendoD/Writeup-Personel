# UMassCTF 2025

This repository contains solutions to various challenges from UMMASCTF. Each subdirectory contains a specific challenge with its own README and solution files.

## Crypto Challenges

### [Disordered Tree](Crypto/Disordered%20Tree/)
A key distribution scheme challenge involving RSA and a tree-based key distribution method. The vulnerability lies in the intermediate keys provided in the output.

**Flag:** `UMASS{perhaps_dont_be_using_commutative_encryption}`

### [BuRGerCode](Crypto/BuRGerCode/)
A challenge combining cryptography with the Tower of Hanoi puzzle. The name hints at Binary Reflected Gray Code (BRGC) used for key generation.

**Flag:** `UMASS{gr4y_c0d3_s01v3s_burg3r5_0f_h4n01}`

## Forensics Challenges

### [Macrotrace](Forensic/Macrotrace/)
A forensics challenge involving a malicious Excel spreadsheet with macros. The flag is hidden in a Windows event log as a base64-encoded string.

**Flag:** `UMASS{drop_it_like_its_hot}`
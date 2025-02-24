#!/usr/bin/env python3
"""
RSA Pop Quiz Challenge Solver - picoCTF 2019
This script connects to the RSA Pop Quiz server and solves all problems sequentially to get the flag.
"""

import socket
import time
import re
import gmpy2
from Crypto.Util.number import long_to_bytes

# Challenge server details
HOST = "jupiter.challenges.picoctf.org"
PORT = 1981

def receive_data(s, timeout=5):
    """Receive data from socket with timeout"""
    s.settimeout(timeout)
    result = b""
    
    try:
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                result += chunk
            except socket.timeout:
                break
    except Exception as e:
        print(f"Error receiving data: {e}")
    
    return result.decode('utf-8', errors='replace')

def main():
    """Main function to connect to server and solve all problems in sequence"""
    try:
        print(f"Connecting to {HOST}:{PORT}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Connected successfully!")
        
        # ==== Problem 1: Calculate n from p and q ====
        print("\n==== Problem 1: Calculate n from p and q ====")
        problem_text = receive_data(s)
        print(problem_text)
        
        # Extract p and q
        p = None
        q = None
        for line in problem_text.split('\n'):
            if "p :" in line:
                p = int(line.split(":", 1)[1].strip())
            elif "q :" in line:
                q = int(line.split(":", 1)[1].strip())
        
        if p and q:
            n = p * q
            print(f"Calculated n = {n}")
            
            s.send(b"y\n")
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            s.send(f"{n}\n".encode())
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
        
        # ==== Problem 2: Calculate q from p and n ====
        print("\n==== Problem 2: Calculate q from p and n ====")
        
        # Extract p and n from previous response
        p = None
        n = None
        for line in response.split('\n'):
            if "p :" in line:
                try:
                    p = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "n :" in line:
                try:
                    n = int(line.split(":", 1)[1].strip())
                except:
                    pass
        
        if p and n:
            q = n // p
            print(f"Calculated q = {q}")
            
            s.send(b"y\n")
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            s.send(f"{q}\n".encode())
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
        
        # ==== Problem 3: Large number factorization (not feasible) ====
        print("\n==== Problem 3: Large number factorization (not feasible) ====")
        # Just answer "no" for this problem
        s.send(b"n\n")
        time.sleep(0.5)
        
        response = receive_data(s)
        print(response)
        
        # ==== Problem 4: Calculate totient function ====
        print("\n==== Problem 4: Calculate totient function ====")
        
        # Extract p and q from previous response
        p = None
        q = None
        for line in response.split('\n'):
            if "p :" in line:
                try:
                    p = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "q :" in line:
                try:
                    q = int(line.split(":", 1)[1].strip())
                except:
                    pass
        
        if p and q:
            totient = (p - 1) * (q - 1)
            print(f"Calculated totient = {totient}")
            
            s.send(b"y\n")
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            s.send(f"{totient}\n".encode())
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
        
        # ==== Problem 5: Calculate ciphertext ====
        print("\n==== Problem 5: Calculate ciphertext ====")
        
        # Extract plaintext, e, and n
        plaintext = None
        e = None
        n = None
        
        for line in response.split('\n'):
            if "plaintext :" in line:
                try:
                    plaintext = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "e :" in line:
                try:
                    e = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "n :" in line and "totient" not in line.lower():
                try:
                    n = int(line.split(":", 1)[1].strip())
                except:
                    pass
        
        if plaintext and e and n:
            ciphertext = pow(plaintext, e, n)
            print(f"Calculated ciphertext")
            
            s.send(b"y\n")
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            s.send(f"{ciphertext}\n".encode())
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
        
        # ==== Problem 6: Decrypt ciphertext with e=3 (not feasible) ====
        print("\n==== Problem 6: Decrypt ciphertext with e=3 (not feasible) ====")
        # Just answer "no" for this problem
        s.send(b"n\n")
        time.sleep(0.5)
        
        response = receive_data(s)
        print(response)
        
        # ==== Problem 7: Calculate private key d ====
        print("\n==== Problem 7: Calculate private key d ====")
        
        # Extract p, q, and e
        p = None
        q = None
        e = None
        
        for line in response.split('\n'):
            if "p :" in line:
                try:
                    p = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "q :" in line:
                try:
                    q = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "e :" in line:
                try:
                    e = int(line.split(":", 1)[1].strip())
                except:
                    pass
        
        if p and q and e:
            # Calculate totient = (p-1)(q-1)
            totient = (p - 1) * (q - 1)
            print("Calculated totient = (p-1) * (q-1)")
            
            # Calculate d = e^(-1) mod totient
            d = int(gmpy2.invert(e, totient))
            print("Calculated private key d")
            
            # Verify d is correct: (d * e) % totient should equal 1
            if (d * e) % totient == 1:
                print("Verified: (d * e) mod totient = 1")
                
                s.send(b"y\n")
                time.sleep(0.5)
                
                response = receive_data(s)
                print(response)
                
                s.send(f"{d}\n".encode())
                time.sleep(0.5)
                
                response = receive_data(s)
                print(response)
        
        # ==== Problem 8: Decrypt ciphertext with given prime factor ====
        print("\n==== Problem 8: Decrypt ciphertext with given prime factor ====")
        
        # Extract p, ciphertext, e, and n
        p = None
        ciphertext = None
        e = None
        n = None
        
        for line in response.split('\n'):
            if "p :" in line:
                try:
                    p = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "ciphertext :" in line:
                try:
                    ciphertext = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "e :" in line:
                try:
                    e = int(line.split(":", 1)[1].strip())
                except:
                    pass
            elif "n :" in line:
                try:
                    n = int(line.split(":", 1)[1].strip())
                except:
                    pass
        
        if p and ciphertext and e and n:
            # Step 1: Calculate q = n/p
            q = n // p
            print(f"Calculated q = n/p")
            
            # Step 2: Calculate the totient phi(n) = (p-1) * (q-1)
            totient = (p - 1) * (q - 1)
            print(f"Calculated totient = (p-1) * (q-1)")
            
            # Step 3: Calculate d = e^(-1) mod totient
            d = int(gmpy2.invert(e, totient))
            print(f"Calculated private key d")
            
            # Step 4: Decrypt the ciphertext
            plaintext = pow(ciphertext, d, n)
            print(f"Decrypted plaintext")
            
            # Try to convert to bytes and then to string
            try:
                plaintext_bytes = long_to_bytes(plaintext)
                plaintext_str = plaintext_bytes.decode('ascii')
                print(f"Plaintext (as text): {plaintext_str}")
                
                # Check if it looks like a flag
                if "picoCTF" in plaintext_str:
                    print(f"\n🚩 FLAG FOUND: {plaintext_str}")
            except Exception as e:
                print(f"Could not convert to text: {e}")
            
            s.send(b"y\n")
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            s.send(f"{plaintext}\n".encode())
            time.sleep(0.5)
            
            response = receive_data(s)
            print(response)
            
            # Check for the flag
            flag_match = re.search(r'picoCTF{.*?}', response)
            if flag_match:
                print(f"\n🚩 FLAG FOUND: {flag_match.group(0)}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            s.close()
            print("Connection closed")
        except:
            pass

if __name__ == "__main__":
    main()

CipherOrbit is a lightweight, open‑source command‑line utility for encrypting and decrypting text using a customizable rotating cipher.  
It combines the simplicity of a Caesar shift with a configurable "orbit" length, allowing multiple successive rotations for stronger obfuscation.

## Features
- Simple CLI with `encrypt` and `decrypt` commands  
- Adjustable shift amount and orbit count  
- Supports Unicode input (UTF‑8)  
- No external dependencies – pure Python 3  
- Helpful error messages and usage hints  

## Installation
```bash
# Clone the repository
git clone https://github.com/yourname/CipherOrbit.git
cd CipherOrbit

# (Optional) Install as a script
pip install .
```

## Usage
```bash
# Encrypt a message with a shift of 5 and orbit of 3
python cipher_orbit.py encrypt -s 5 -o 3 "Hello World!"

# Decrypt the previous output
python cipher_orbit.py decrypt -s 5 -o 3 "Mjqqt Btwqi!"
```

Run `python cipher_orbit.py -h` for a full list of options.
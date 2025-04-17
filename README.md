![BinGenetic](BinGenetic_Banner.jpg?raw=true)

**BinGenetic** is a lightweight Python library that enables seamless conversion between binary data and genetic sequences (DNA or RNA), facilitating research in DNA data storage and bioinformatics.

---
## 🔧 **Development Details**
- **👨‍💻 Developer:** [Ravin Kumar](https://mr-ravin.github.io)  
- **📂 GitHub Repository:** [BinGenetic](https://github.com/mr-ravin/bingenetic)

---
## 📥 **Installation**
```sh
pip install bingenetic
```
or,
```sh
pip install git+https://github.com/mr-ravin/bingenetic.git
```

### 📌 **Dependencies:**
- Python >= 3.7
- No additional dependencies required

---
## 🚀 **Usage & Examples**

### 🔹 Binary Code to Genetic Code:
```python
import bingenetic

# Convert binary to DNA sequence
genetic_code = bingenetic.btg("00011011", "dna")  # Binary -> DNA
print(genetic_code)  # Output: 'ACGT'
```

### 🔹 Genetic Code to Binary Code:
```python
import bingenetic

# Convert DNA sequence to binary
binary_code = bingenetic.gtb("ACGT", "dna")  # DNA -> Binary
print(binary_code)  # Output: '00011011'
```

---
## 📌 **Use Cases**
- **DNA Data Storage** – Store digital information using biological sequences.
- **Bioinformatics** – Encode and decode genetic data efficiently.
- **Cryptography** – Convert binary data into genetic code for secure encoding.

---
## 📜 **License**
```
Copyright (c) 2020 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```


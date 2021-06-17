# BinGenetic
This repository contains a simple python library to convert binary data (in digital form) to genetic codes and further genetic codes back to binary data.

##### Author: [Ravin Kumar](https://mr-ravin.github.io)

- #### Binary Code to Genetic Code:

```python
import bingenetic
genetic_code = bingenetic.btg(["00011011"],"dna") # first parameter is binary code as a list, second parameter is the type of genetic code i.e. DNA, or RNA
```

- #### Genetic Code to Binary Code:

```python
import bingenetic
binary_code = bingenetic.gtb(["ATCG"],"dna") # first parameter is genetic code as a list, second parameter is the type of genetic code i.e. DNA, or RNA
```


#### Installation using pip:
```
pip install bingenetic
```

```
Copyright (c) 2020 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

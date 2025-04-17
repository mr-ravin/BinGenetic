__version__ = '2.6'

def gtb(gen_code_str: str, mode: str = "dna") -> str:
    """
    Converts a list of genetic sequence (DNA or RNA) into binary representation.

    Parameters:
    gen_code_str (str):          String of genetic sequence to be converted.
                                 Sequence should consist of 'A', 'T', 'C', 'G' for DNA,
                                 or 'A', 'U', 'C', 'G' for RNA.
    mode (str, optional): Specifies whether the input sequence is "dna" or "rna". 
                          Defaults to "dna".

    Returns:
    str: Binary representation of the input genetic sequence.

    Raises:
    TypeError: If an invalid genetic sequence is encountered.
    """
    mode = mode.lower()
    
    DNA_TO_BINARY = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    RNA_TO_BINARY = {'A': '00', 'C': '01', 'G': '10', 'U': '11'}
    
    if mode not in ("dna", "rna"):
        raise ValueError("Mode must be either 'dna' or 'rna'")
    
    lookup = DNA_TO_BINARY if mode == "dna" else RNA_TO_BINARY
    
    binary_str = ""

    try:
        binary_str = ''.join(lookup[base] for base in gen_code_str.upper())
    except KeyError:
        raise TypeError("Not a valid {} sequence".format(mode.upper()))
    
    return binary_str

def btg(bin_code_str: str, mode: str = "dna") -> str:
    """
    Converts a string of binary sequence into genetic sequence (DNA or RNA).

    Parameters:
    bin_code_str (str):          String of binary sequence to be converted.
                                 Binary sequence should have an even length 
                                 and contain only '0' and '1'.
    mode (str, optional): Specifies whether the output should be "dna" or "rna". 
                          Defaults to "dna".

    Returns:
    str: Genetic sequence corresponding to the input binary sequence.

    Raises:
    TypeError: If an invalid binary sequence is encountered or if the binary sequence length is odd.
    """
    mode = mode.lower()
    
    BINARY_TO_DNA = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    BINARY_TO_RNA = {'00': 'A', '01': 'C', '10': 'G', '11': 'U'}
    
    if mode not in ("dna", "rna"):
        raise ValueError("Mode must be either 'dna' or 'rna'")
    
    lookup = BINARY_TO_DNA if mode == "dna" else BINARY_TO_RNA
    
    genetic_str = ""
    
    if len(bin_code_str) % 2 != 0:
            raise TypeError("Binary sequence length must be even")
    try:
            genetic_str = ''.join(lookup[bin_code_str[i:i+2]] for i in range(0, len(bin_code_str), 2))
    except KeyError:
            raise TypeError("Invalid binary sequence for {}".format(mode.upper()))
    
    return genetic_str

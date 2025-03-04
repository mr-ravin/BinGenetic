__version__ = '2.3'

def gtb(gen_code_list: list[str], mode: str = "dna") -> str:
    """
    Converts a list of genetic sequences (DNA or RNA) into binary representations.

    Parameters:
    gen_code_list (list of str): List of genetic sequences to be converted.
                                 Each sequence should consist of 'A', 'T', 'C', 'G' for DNA,
                                 or 'A', 'U', 'C', 'G' for RNA.
    mode (str, optional): Specifies whether the input sequence is "dna" or "rna". 
                          Defaults to "dna".

    Returns:
    str: Concatenated binary representation of the input genetic sequences.

    Raises:
    TypeError: If an invalid genetic sequence is encountered.
    """
    mode = mode.lower()
    
    DNA_TO_BINARY = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    RNA_TO_BINARY = {'A': '00', 'C': '01', 'G': '10', 'U': '11'}
    
    if mode not in ("dna", "rna"):
        raise ValueError("Mode must be either 'dna' or 'rna'")
    
    lookup = DNA_TO_BINARY if mode == "dna" else RNA_TO_BINARY
    
    binary_list = []
    for gen_code_line in gen_code_list:
        try:
            binary_list.append(''.join(lookup[base] for base in gen_code_line.upper()))
        except KeyError:
            raise TypeError("Not a valid {} sequence".format(mode.upper()))
    
    return ''.join(binary_list)

def btg(bin_code_list: list[str], mode: str = "dna") -> str:
    """
    Converts a list of binary sequences into genetic sequences (DNA or RNA).

    Parameters:
    bin_code_list (list of str): List of binary sequences to be converted.
                                 Each binary sequence should have an even length 
                                 and contain only '0' and '1'.
    mode (str, optional): Specifies whether the output should be "dna" or "rna". 
                          Defaults to "dna".

    Returns:
    str: Concatenated genetic sequence corresponding to the input binary sequences.

    Raises:
    TypeError: If an invalid binary sequence is encountered or if the binary sequence length is odd.
    """
    mode = mode.lower()
    
    BINARY_TO_DNA = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    BINARY_TO_RNA = {'00': 'A', '01': 'C', '10': 'G', '11': 'U'}
    
    if mode not in ("dna", "rna"):
        raise ValueError("Mode must be either 'dna' or 'rna'")
    
    lookup = BINARY_TO_DNA if mode == "dna" else BINARY_TO_RNA
    
    genetic_list = []
    for bin_code_line in bin_code_list:
        if len(bin_code_line) % 2 != 0:
            raise TypeError("Binary sequence length must be even")
        try:
            genetic_list.append(''.join(lookup[bin_code_line[i:i+2]] for i in range(0, len(bin_code_line), 2)))
        except KeyError:
            raise TypeError("Invalid binary sequence for {}".format(mode.upper()))
    
    return ''.join(genetic_list)

def gtb(gen_code_list,mode="dna"): # genetic code to binary code
  res_list=[]
  mode = mode.lower()
  if mode=="dna":
    for gen_code_line in gen_code_list:
       tmp=""
       elem_idx=0
       gen_code_line_len=len(gen_code_line)
       while elem_idx<gen_code_line_len:
           if gen_code_line[elem_idx].upper()=="A":
             tmp=tmp+"00"
           elif gen_code_line[elem_idx].upper()=="T":
             tmp=tmp+"11"
           elif gen_code_line[elem_idx].upper()=="C":
             tmp=tmp+"01"
           elif gen_code_line[elem_idx].upper()=="G":
             tmp=tmp+"10"
           else:
             raise TypeError("Not a valid DNA Sequence")
           elem_idx=elem_idx+1
       res_list.append(tmp)
  elif mode=="rna":
    for gen_code_line in gen_code_list:
       tmp=""
       elem_idx=0
       gen_code_line_len=len(gen_code_line)
       while elem_idx<gen_code_line_len:
           if gen_code_line[elem_idx].upper()=="A":
             tmp=tmp+"00"
           elif gen_code_line[elem_idx].upper()=="U":
             tmp=tmp+"11"
           elif gen_code_line[elem_idx].upper()=="C":
             tmp=tmp+"01"
           elif gen_code_line[elem_idx].upper()=="G":
             tmp=tmp+"10"
           else:
             raise TypeError("Not a valid RNA Sequence")
           elem_idx=elem_idx+1
       res_list.append(tmp)
  return res_list

def btg(bin_code_list,mode="dna",EOF_CODE=""): # binary code to genetic code, here EOF_CODE is a special binary code to make binary numbers even
  res_list=[]
  mode = mode.lower()
  if mode=="dna":
    for bin_code_line in bin_code_list:
      tmp=""
      elem_idx=0
      bin_code_line_len=len(bin_code_line)
      while bin_code_line_len%2==1:
        bin_code_line=bin_code_line+EOF_CODE
        bin_code_line_len=len(bin_code_line)
      while elem_idx<bin_code_line_len:
        if bin_code_line[elem_idx]=="0" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"A"
        elif bin_code_line[elem_idx]=="0" and bin_code_line[elem_idx+1]=="1":
          tmp=tmp+"C"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"G"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="1":
          tmp=tmp+"T"
        else:
          raise TypeError("Not a valid binary sequence of the DNA")
        elem_idx=elem_idx+2
      res_list.append(tmp)
  elif mode=="rna":
    for bin_code_line in bin_code_list:
      tmp=""
      elem_idx=0
      bin_code_line_len=len(bin_code_line)
      while bin_code_line_len%2==1:
        bin_code_line=bin_code_line+EOF_CODE
        bin_code_line_len=len(bin_code_line)
      while elem_idx<bin_code_line_len:
        if bin_code_line[elem_idx]=="0" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"A"
        elif bin_code_line[elem_idx]=="0" and bin_code_line[elem_idx+1]=="1":
          tmp=tmp+"C"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"G"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="1":
          tmp=tmp+"U"
        else:
          raise TypeError("Not a valid binary sequence of the RNA")
        elem_idx=elem_idx+2
      res_list.append(tmp)
  return res_list

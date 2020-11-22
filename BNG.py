def gtb(gen_code_list,mode="dna"): # genetic code to binary code
  res_list=[]
  if mode=="dna":
    for gen_code_line in gen_code_list:
       tmp=""
       elem_idx=0
       gen_code_line_len=len(gen_code_line)
       while elem_idx<gen_code_line_len:
           if gen_code_line[elem_idx]=="A":
             tmp=tmp+"00"
           elif gen_code_line[elem_idx]=="T":
             tmp=tmp+"01"
           elif gen_code_line[elem_idx]=="C":
             tmp=tmp+"10"
           else:
             tmp=tmp+"11"
           elem_idx=elem_idx+1
       res_list.append(tmp)
  else:
    for gen_code_line in gen_code_list:
       tmp=""
       elem_idx=0
       gen_code_line_len=len(gen_code_line)
       while elem_idx<gen_code_line_len:
           if gen_code_line[elem_idx]=="A":
             tmp=tmp+"00"
           elif gen_code_line[elem_idx]=="U":
             tmp=tmp+"01"
           elif gen_code_line[elem_idx]=="C":
             tmp=tmp+"10"
           else:
             tmp=tmp+"11"
           elem_idx=elem_idx+1
       res_list.append(tmp)
  return res_list

def btg(bin_code_list,mode="dna",EOF_CODE=""): # binary code to genetic code, here EOF_CODE is a special binary code to make binary numbers even
  res_list=[]
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
          tmp=tmp+"T"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"C"
        else:
          tmp=tmp+"G"
        elem_idx=elem_idx+2
      res_list.append(tmp)
  else:
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
          tmp=tmp+"U"
        elif bin_code_line[elem_idx]=="1" and bin_code_line[elem_idx+1]=="0":
          tmp=tmp+"C"
        else:
          tmp=tmp+"G"
        elem_idx=elem_idx+2
      res_list.append(tmp)
  return res_list

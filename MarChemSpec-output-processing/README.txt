================================================================================

This folder contains:
(1) 8 MarChemSpec input files (.dat)
(2) 8 corresponding MarChemSpec output files (.rs2)
(3) a script for processing raw output and calculating key seawater properties

The processing routine process-output.py was used to generate Table 1 in REF(yr), and is intended to be used for consistent calculations of seawater chemical properties based on MarChemSpec results. 

================================================================================

The 8 seawater examples included here are:
(1) RSW_0deg - modern reference seawater at 0 degrees celsius 
(2) RSW_25deg - modern reference seawater at 25 degrees celsius 
(3) ESW_CaMg_0deg - theoretical paleoseawater with Eocene-like [Ca2+] and [Mg2+] at 0 degrees celsius 
(4) ESW_CaMg_25deg - theoretical paleoseawater with Eocene-like [Ca2+] and [Mg2+] at 25 degrees celsius 
(5) ESW_CaMg_NaCl_0deg - theoretical paleoseawater with Eocene-like [Ca2+] and [Mg2+] plus NaCl-based ionic strength normalization at 0 degrees celsius 
(6) ESW_CaMg_NaCl_25deg - theoretical paleoseawater with Eocene-like [Ca2+] and [Mg2+] plus NaCl-based ionic strength normalization at 25 degrees celsius 
(7) ESW_CaMgSO4_NaCl_0deg - theoretical paleoseawater with Eocene-like [Ca2+], [Mg2+], and [SO42-] plus NaCl-based ionic strength normalization at 0 degrees celsius 
(8) ESW_CaMgSO4_NaCl_25deg - theoretical paleoseawater with Eocene-like [Ca2+], [Mg2+], and [SO42-] plus NaCl-based ionic strength normalization at 25 degrees celsius 

Properties calculate include:
(1)
(2)
(3)

See REF(yr) for a full description. Note that to run MarChemSpec with any of these example files, the filename will need to be changed back to 'MCS.dat' and the file placed in the user's MarChemSpec root folder. See official MarChemSpec documentation for information on how to run the model (marchemspec.org).
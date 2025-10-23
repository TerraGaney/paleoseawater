================================================================================

This folder contains:
(1) 8 MarChemSpec input files (.dat)
(2) 8 corresponding MarChemSpec output files for ion activities and concentrations (.rs2)
(3) 8 corresponding MarChemSpec output files for K calculations (.rs5)
(4) a script for processing raw MarChemSoec output and calculating key paleo-seawater properties

The processing routine process-output.py was used to generate Table 1 in Ganey et al. (in prep). The script calculates various paleo-seawater chemical properties based on MarChemSpec model results, and writes to Table1.csv.

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

Properties calculated and/or tabulated include:
(1) paleo-seawater equilibrium contants K0, K1, K2, KB, KH2O, KspC, KspA, KS (mol per kg seawater basis)
(2) temperature (TempC; ºC)
(3) absolute salinity (SalA; g/kg seawater)
(4) calcium amount concentration ([Ca2+]; mol per kg seawater)
(5) magnesium amount concentration ([Mg2+]; mol per kg seawater)
(6) sulfate amount concentration ([SO42-]; mol per kg seawater)
(7) ionic strength (IonicStr; moleq per kg seawater)
(8) free pH (pHF)
(9) total pH (pHT)
(10) alkalinity (ALK; umol per kg seawater)
(11) DIC (umol per kg seawater)
(12) calcium carbonate saturation state (Omega)

See Ganey et al. (in prep) for full formulas and description. Note that to run MarChemSpec independently with any of these example files, the filename will need to be changed back to 'MCS.dat' and the file placed in the user's MarChemSpec root folder. See official MarChemSpec documentation for information on how to run the model (marchemspec.org).
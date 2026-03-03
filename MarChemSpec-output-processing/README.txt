================================================================================

This folder contains:
(1) 8 MarChemSpec input files (.dat)
(2) 8 corresponding MarChemSpec output files for ion activities and concentrations (.rs2)
(3) 8 corresponding MarChemSpec output files for K calculations (.rs4)
(4) a script for processing raw MarChemSpec output and calculating key paleo-seawater properties
(5) script output and processing results (Table.csv)

The processing routine process-output-kgw.py was used to generate Table 1 and Table 3 in Ganey et al. (GBC; 2026). The script calculates various paleo-seawater chemical properties based on MarChemSpec model results, and writes to Table.csv.

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
(1) paleo-seawater equilibrium contants pK0, pK1, pK2, pKB, pKH2O, pKspC, pKspA, KHSO4 (mol per kg pure water basis)
(2) temperature (TempC; ºC)
(3) absolute salinity (SalA; g/kg pure water)
(4) kgw/kgsw conversion factor
(5) calcium amount concentration ([Ca2+]; mol per kg water)
(6) magnesium amount concentration ([Mg2+]; mol per kg water)
(7) sulfate amount concentration ([SO42-]; mol per kg water)
(8) sodium amount concentration ([Na+]; mol per kg water)
(9) chloride amount concentration ([Cl-]; mol per kg water)
(10) ionic strength (IonicStr; moleq per kg water)
(11) free pH (pHF)
(12) total pH (pHT)
(13) alkalinity (ALK; umol per kg water)
(14) DIC (umol per kg water)
(15) calcium carbonate saturation state (Omega)
(16) fraction of free over total hydrogen ions (alphaH)
(17) fraction of free over total carbonate ions (alphaCO3)
(18) fraction of free over total hydroxide (alphaOH)

See Ganey et al. (GBC; 2026) for full formulas and description. Note that to run MarChemSpec independently with any of these example files, the filename will need to be changed back to 'MCS.dat' and the file placed in the user's MarChemSpec root folder. See official MarChemSpec documentation for information on how to run the model (marchemspec.org).

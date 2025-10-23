================================================================================

This folder contains:
(1) a 'look-up table' for computing paleo-seawater K values based on MarChemSpec model results
(2) an example script that calculates and prints Ks from the look-up table, using user-defined [Ca2+] and [Mg2+]

================================================================================

Instructions:

Running MCS_lookup_table_wrapper.py will prompt the user to provide non-modern values of seawater [Ca2+] and [Mg2+]. Concentrations should be provided in mol per kg seawater (not mM). Allowable values are from 0.001 to 0.06 M for Ca2+ and Mg2+ both (1 to 60 mM). The steps are 0.001 units. Acceptable input might be e.g. Ca2+ = 0.013 and Mg2+ = 0.038 or any such pair, but the script would *not* accept e.g. Ca = 0.0133 (too precise). Interpolation is not available at this time.

The wrapper script calculates Ks using the provided lookup table, plus default temperature and absolute salinity inputs (25ºC, 35 g/kgs). Temp and salinity can be changed in the script if desired (lines 18, 19).

The formulas used to calculate Ks can be found in Dickson (2010; Table 1.1). All p_i,j coefficients in the original equations were refit based on MarChemSpec to account for variable seawater Ca2+, Mg2+. The new parameters p_i,j are what populate the lookup table for every Ca2+, Mg2+ pair. Please refer to Ganey et al. (in prep) and Hain et al. (2015) for details on the fitting process or further description of the table.
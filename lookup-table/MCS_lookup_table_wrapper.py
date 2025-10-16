import numpy as np
import pandas as pd

# Read in lookup table
MCSdf = pd.read_csv('MarChemSpec_LOOKUP_60x60.csv')
ca = MCSdf['[Ca2+]']
mg = MCSdf['[Mg2+]']

# Request desired non-modern Ca2+, Mg2+ concentrations (mol/kg seawater basis) from user
# Acceptable ranges are from 0.001 to 0.06 M for both ions, with 0.001 unit (1 mM) precision (see spreadsheet for acceptable pairs; no interpolation available at this time)
ca_in = float(input('\nEnter [Ca2+] (mol/kg seawater): '))
mg_in = float(input('Enter [Mg2+] (mol/kg seawater): '))
print('\n')

df_loc = MCSdf.loc[(ca == ca_in) & (mg == mg_in)]

# Set default variables (note modern surface ocean temperature, salinity - can be altered if desired)
TempC = 25.0
Sal = 34.900901
TempK = TempC + 273.15
sqrtSal = np.sqrt(Sal)
lnTempK = np.log(TempK)
log10TempK = np.log10(TempK)
I = 19.924*Sal/(1000-1.005*Sal)
sqrtI = np.sqrt(I)

# Calculate Ks
K0 = np.exp( (float(df_loc['K0p0']))+(float(df_loc['K0p1']))*100/TempK+(float(df_loc['K0p2']))*np.log(TempK/100) + Sal*((float(df_loc['K0p3']))+(float(df_loc['K0p4']))*TempK/100+(float(df_loc['K0p5']))*TempK/100*TempK/100) )
K1 = np.power(10,((float(df_loc['K1p0'])) + (float(df_loc['K1p1']))/TempK + (float(df_loc['K1p2']))*np.log(TempK) + (float(df_loc['K1p3']))*Sal + (float(df_loc['K1p4'])*Sal*Sal)))
K2 = np.power(10,((float(df_loc['K2p0'])) + (float(df_loc['K2p1']))/TempK + (float(df_loc['K2p2']))*np.log(TempK) + (float(df_loc['K2p3']))*Sal + (float(df_loc['K2p4']))*Sal*Sal))
Kb = np.exp( (float(df_loc['Kbp0'])) + (float(df_loc['Kbp1']))*sqrtSal + (float(df_loc['Kbp2']))*Sal + (1/TempK)*((float(df_loc['Kbp3']))+(float(df_loc['Kbp4']))*sqrtSal+(float(df_loc['Kbp5']))*Sal+(float(df_loc['Kbp6']))*Sal*sqrtSal+(float(df_loc['Kbp7']))*Sal*Sal) + lnTempK*((float(df_loc['Kbp8']))+(float(df_loc['Kbp9']))*sqrtSal+(float(df_loc['Kbp10']))*Sal) + (float(df_loc['Kbp11']))*sqrtSal*TempK )
Kw = np.exp( (float(df_loc['Kwp0'])) + (float(df_loc['Kwp1']))/TempK + (float(df_loc['Kwp2']))*lnTempK + sqrtSal*( (float(df_loc['Kwp3']))/TempK + (float(df_loc['Kwp4'])) + (float(df_loc['Kwp5']))*lnTempK ) + (float(df_loc['Kwp6']))*Sal  )
KspC = np.power(10, (float(df_loc['Kcp0'])) + (float(df_loc['Kcp1']))*TempK + (float(df_loc['Kcp2']))/TempK + (float(df_loc['Kcp3']))*log10TempK + sqrtSal*((float(df_loc['Kcp4']))+(float(df_loc['Kcp5']))*TempK+(float(df_loc['Kcp6']))/TempK) + (float(df_loc['Kcp7']))*Sal+(float(df_loc['Kcp8']))*Sal*sqrtSal )
KspA = np.power(10, (float(df_loc['Kap0'])) + (float(df_loc['Kap1']))*TempK + (float(df_loc['Kap2']))/TempK + (float(df_loc['Kap3']))*log10TempK + sqrtSal*((float(df_loc['Kap4']))+(float(df_loc['Kap5']))*TempK+(float(df_loc['Kap6']))/TempK) + (float(df_loc['Kap7']))*Sal+(float(df_loc['Kap8']))*Sal*sqrtSal )
Ks = np.exp( (float(df_loc['Ksp0'])) + (float(df_loc['Ksp1']))/TempK + (float(df_loc['Ksp2']))*lnTempK + sqrtI*( (float(df_loc['Ksp3']))/TempK  + (float(df_loc['Ksp4'])) + (float(df_loc['Ksp5']))*lnTempK) + I*( (float(df_loc['Ksp6']))/TempK  + (float(df_loc['Ksp7'])) + (float(df_loc['Ksp8']))*lnTempK) + (float(df_loc['Ksp9']))/TempK *I*sqrtI + (float(df_loc['Ksp10']))/TempK *I*I + np.log(1-0.001005*Sal) )

# Print Ks
print('K0 at Ca/Mg = ' + str(K0))
print('K1 at Ca/Mg = ' + str(K1))
print('K2 at Ca/Mg = ' + str(K2))
print('KB at Ca/Mg = ' + str(Kb))
print('KH2O at Ca/Mg = ' + str(Kw))
print('KspC at Ca/Mg = ' + str(KspC))
print('KspA at Ca/Mg = ' + str(KspA))
print('KHSO4 at Ca/Mg = ' + str(Ks) + '\n')
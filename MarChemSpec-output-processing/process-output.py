import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import io


class LoadOutput():
    def __init__(self, rs2filename, rs5filename):
        self.LoadRawOutput(rs2filename)
        self.LoadKsOutput(rs5filename)


    def LoadRawOutput(self, rs2filename):

        # ------------------ Read in .rs2 output file ------------------ #
        with open(rs2filename) as file_in:
            self.rawMCSOutput = []
            for line in file_in:
                self.rawMCSOutput.append(line)

        # ------------------ Load results and write to df ------------------ #
        shape_MCSResults = self.rawMCSOutput[5:] 
        shape_MCSResults[0] = "iCount iFail Err T P aW Osm kH mH gH kNA mNA gNA kMG mMG gMG kCA mCA gCA kK mK gK kMGOH mMGOH gMGOH \
        kSR mSR gSR kMGF mMGF gMGF kCAF mCAF gCAF kCL mCL gCL kSO4 mSO4 gSO4 kHSO4 mHSO4 gHSO4 kOH mOH gOH \
        kBR mBR gBR kHCO3 mHCO3 gHCO3 kCO3 mCO3 gCO3 kBOH4 mBOH4 gBOH4 kF mF gF kBOH3 mBOH3 gBOH3 kCO2 mCO2 gCO2 kHF mHF \
        gHF kMGCO3 mMGCO3 gMGCO3 kCACO3 mCACO3 gCACO3 kSRCO3 mSRCO3 gSRCO3"
        self.MCSResultsTable = pd.read_csv(io.StringIO('\n'.join(shape_MCSResults)), delim_whitespace = True)

        # ------------------ Load activity coefficients (gammas) ------------------ #
        self.gammaH = self.MCSResultsTable['gH'][0]
        self.gammaNa = self.MCSResultsTable['gNA'][0]
        self.gammaMg = self.MCSResultsTable['gMG'][0]
        self.gammaCa = self.MCSResultsTable['gCA'][0]
        self.gammaK = self.MCSResultsTable['gK'][0]
        self.gammaMgOH = self.MCSResultsTable['gMGOH'][0]
        self.gammaSr = self.MCSResultsTable['gSR'][0]
        self.gammaMgF = self.MCSResultsTable['gMGF'][0]
        self.gammaCaF = self.MCSResultsTable['gCAF'][0]
        self.gammaCl = self.MCSResultsTable['gCL'][0]
        self.gammaSO4 = self.MCSResultsTable['gSO4'][0]
        self.gammaHSO4 = self.MCSResultsTable['gHSO4'][0]
        self.gammaOH = self.MCSResultsTable['gOH'][0]
        self.gammaBr = self.MCSResultsTable['gBR'][0]
        self.gammaHCO3 = self.MCSResultsTable['gHCO3'][0]
        self.gammaCO3 = self.MCSResultsTable['gCO3'][0]
        self.gammaBOH4 = self.MCSResultsTable['gBOH4'][0]
        self.gammaF = self.MCSResultsTable['gF'][0]
        self.gammaBOH3 = self.MCSResultsTable['gBOH3'][0]
        self.gammaCO2 = self.MCSResultsTable['gCO2'][0]
        self.gammaHF = self.MCSResultsTable['gHF'][0]
        self.gammaMgCO3 = self.MCSResultsTable['gMGCO3'][0]
        self.gammaCaCO3 = self.MCSResultsTable['gCACO3'][0]
        self.gammaSrCO3 = self.MCSResultsTable['gSRCO3'][0]
        self.actWater = self.MCSResultsTable['aW'][0]

        # ------------------ Load amount concentrations (mol/kg seawater) ------------------ #
        self.molH = self.MCSResultsTable['mH'][0]
        self.molNa = self.MCSResultsTable['mNA'][0]
        self.molMg = self.MCSResultsTable['mMG'][0]
        self.molCa = self.MCSResultsTable['mCA'][0]
        self.molK = self.MCSResultsTable['mK'][0]
        self.molMgOH = self.MCSResultsTable['mMGOH'][0]
        self.molSr = self.MCSResultsTable['mSR'][0]
        self.molMgF = self.MCSResultsTable['mMGF'][0]
        self.molCaF = self.MCSResultsTable['mCAF'][0]
        self.molCl = self.MCSResultsTable['mCL'][0]
        self.molSO4 = self.MCSResultsTable['mSO4'][0]
        self.molHSO4 = self.MCSResultsTable['mHSO4'][0]
        self.molOH = self.MCSResultsTable['mOH'][0]
        self.molBr = self.MCSResultsTable['mBR'][0]
        self.molHCO3 = self.MCSResultsTable['mHCO3'][0]
        self.molCO3 = self.MCSResultsTable['mCO3'][0]
        self.molBOH4 = self.MCSResultsTable['mBOH4'][0]
        self.molF = self.MCSResultsTable['mF'][0]
        self.molBOH3 = self.MCSResultsTable['mBOH3'][0]
        self.molCO2 = self.MCSResultsTable['mCO2'][0]
        self.molHF = self.MCSResultsTable['mHF'][0]
        self.molMgCO3 = self.MCSResultsTable['mMGCO3'][0]
        self.molCaCO3 = self.MCSResultsTable['mCACO3'][0]
        self.molSrCO3 = self.MCSResultsTable['mSRCO3'][0]
        self.actWater = self.MCSResultsTable['aW'][0]

        concentration_conversion_factor = 1 + (np.multiply(self.molH,(1.0078/1000)) + np.multiply(self.molNa,(22.989/1000)) + np.multiply(self.molMg,(24.305/1000)) + np.multiply(self.molCa,(40.078/1000)) + np.multiply(self.molK,(39.10/1000)) + np.multiply(self.molMgOH,(41.318/1000)) + np.multiply(self.molSr,(87.62/1000)) + np.multiply(self.molMgF,(43.31/1000)) + np.multiply(self.molCaF,(59.08/1000)) + np.multiply(self.molCl,(35.45/1000)) + np.multiply(self.molSO4,(96.07/1000)) + np.multiply(self.molHSO4,(97.064/1000)) + np.multiply(self.molOH,(17.008/1000)) + np.multiply(self.molBr,(79.9/1000)) + np.multiply(self.molHCO3,(61.018/1000)) + np.multiply(self.molCO3,(60.009/1000)) + np.multiply(self.molBOH4,(78.84/1000)) + np.multiply(self.molF,(19/1000)) + np.multiply(self.molBOH3,(61.83/1000)) + np.multiply(self.molCO2,(44.01/1000)) + np.multiply(self.molHF,(20.008/1000)) + np.multiply(self.molMgCO3,(84.32/1000)) + np.multiply(self.molCaCO3,(100.087/1000)) + np.multiply(self.molSrCO3,(147.63/1000)))

        self.molH = np.divide(self.molH, concentration_conversion_factor)
        self.molNa = np.divide(self.molNa, concentration_conversion_factor)
        self.molMg = np.divide(self.molMg, concentration_conversion_factor)
        self.molCa = np.divide(self.molCa, concentration_conversion_factor)
        self.molK = np.divide(self.molK, concentration_conversion_factor)
        self.molMgOH = np.divide(self.molMgOH, concentration_conversion_factor)
        self.molSr = np.divide(self.molSr, concentration_conversion_factor)
        self.molMgF = np.divide(self.molMgF, concentration_conversion_factor)
        self.molCaF = np.divide(self.molCaF, concentration_conversion_factor)
        self.molCl = np.divide(self.molCl, concentration_conversion_factor)
        self.molSO4 = np.divide(self.molSO4, concentration_conversion_factor)
        self.molHSO4 = np.divide(self.molHSO4, concentration_conversion_factor)
        self.molOH = np.divide(self.molOH, concentration_conversion_factor)
        self.molBr = np.divide(self.molBr, concentration_conversion_factor)
        self.molHCO3 = np.divide(self.molHCO3, concentration_conversion_factor)
        self.molCO3 = np.divide(self.molCO3, concentration_conversion_factor)
        self.molBOH4 = np.divide(self.molBOH4, concentration_conversion_factor)
        self.molF = np.divide(self.molF, concentration_conversion_factor)
        self.molBOH3 = np.divide(self.molBOH3, concentration_conversion_factor)
        self.molCO2 = np.divide(self.molCO2, concentration_conversion_factor)
        self.molHF = np.divide(self.molHF, concentration_conversion_factor)
        self.molMgCO3 = np.divide(self.molMgCO3, concentration_conversion_factor)
        self.molCaCO3 = np.divide(self.molCaCO3, concentration_conversion_factor)
        self.molSrCO3 = np.divide(self.molSrCO3, concentration_conversion_factor)


    def LoadKsOutput(self, rs5filename):

        # ------------------ Read in .rs5 output file ------------------ #
        with open(rs5filename) as file_in:
            self.rawMCSOutput = []
            for line in file_in:
                self.rawMCSOutput.append(line)

        # ------------------ Load results and write to df ------------------ #
        shape_MCSResults = self.rawMCSOutput[12:] # Make shape for NCA parameters attribute
        shape_MCSResults[0] = "iCount T P pH_T upH_T pH_SW upH_SW pH_F upH_F pCO2 upCO2 fCO2 ufCO2 DIC uDIC TotAlk uTotAlk pKCO2_T upKCO2_T \
        pKHCO3_T upKHCO3_T pKBOH3_T upKBOH3_T pKH2O_T upKH2O_T pKHF_T upKHF_T pKCO2_SW upKCO2_SW pKHCO3_SW upKHCO3_SW pKBOH3_SW upKBOH3_SW pKH2O_SW upKH2O_SW \
        pKCO2_F upKCO2_F pKHCO3_F upKHCO3_F pKBOH3_F upKBOH3_F pKH2O_F upKH2O_F pKHF_F upKHF_F pKHSO4_F upKHSO4_F p[Ca_CO3] up[Ca_CO3]"
        self.MCSKResults = pd.read_csv(io.StringIO('\n'.join(shape_MCSResults)), delim_whitespace = True)

        self.fCO2 = self.MCSKResults['fCO2'][0]
        self.pCO2 = self.MCSKResults['pCO2'][0]

        pK1 = self.MCSKResults['pKCO2_T'][0]
        self.K1 = 10**(-pK1)

        pK2 = self.MCSKResults['pKHCO3_T'][0]
        self.K2 = 10**(-pK2)

        pKB = self.MCSKResults['pKBOH3_T'][0]
        self.KB = 10**(-pKB)

        pKW = self.MCSKResults['pKH2O_T'][0]
        self.KW = 10**(-pKW)

        pKS = self.MCSKResults['pKHSO4_F'][0]
        self.KS = 10**(-pKS)

        pKsp = self.MCSKResults['p[Ca_CO3]'][0]
        self.Ksp = 10**(-pKsp)


class GenerateTableEntry():
    def __init__(self, rs2filename, rs5filename, comptype, tempC):
        self.Output = LoadOutput(rs2filename, rs5filename)
        self.CalculateKs(tempC)
        self.CalculateChem(comptype)
        self.TableEntry(comptype, tempC)
    

    def CalculateKs(self, tempC):

        # ------------------ Thermodynamic Ksp ------------------ #  
        tempK = 273.15+tempC
        ThermoKspC = np.exp(303.1308 - np.divide(13348.09,tempK) -48.7537*np.log(tempK))
        ThermoKspA = np.exp(303.5363 - np.divide(13348.09,tempK) - 48.7537*np.log(tempK)) 

        # ------------------ Empirical Ks ------------------ #  
        S = 35
        IM = np.divide(19.924*S , (1000-(1.05*S)))
        K0_Dickson = np.exp(93.4517*(100/tempK) - 60.2409 + 23.3585*(np.log(tempK/100)) + S*(0.023517 - 0.023656*(tempK/100) + 0.0047036*(np.power((tempK/100),2))))
        K1_Dickson = np.power(10,((61.2172) + (-3633.86)/tempK + (-9.6777)*np.log(tempK) + (0.011555)*S + (-0.0001152)*S*S))
        K2_Dickson = np.power(10,((-471.78/tempK) - 25.9290 + 3.16967*(np.log(tempK)) + 0.01781*S - 0.0001122*(np.power(S,2))))
        KB_Dickson = np.exp((np.divide((-8966.9 - 2890.53*(np.power(S,0.5)) - 77.942*S + 1.728*(np.power(S,1.5)) - 0.0996*(np.power(S,2))),tempK)) + (148.0248 + 137.1942*(np.power(S,0.5)) + 1.62142*S) + ((-24.4344 - 25.085*(np.power(S,0.5)) - 0.2474*S)*np.log(tempK)) + 0.053105*(np.power(S,0.5))*tempK)
        KW_Dickson = np.exp(np.divide(-13847.26,tempK) + 148.9652 - 23.6521*np.log(tempK) + (np.divide(118.67,tempK) - 5.977 + 1.0495*np.log(tempK))*(np.power(S,0.5)) - 0.01615*S)
        KspC_Dickson = np.power(10,(-171.9065 - 0.077993*tempK + np.divide(2839.319,tempK) + 71.595*(np.log10(tempK)) + (-0.77712 + 0.0028426*tempK + np.divide(178.34,tempK))*(np.power(S,0.5)) - 0.07711*S + 0.0041249*(np.power(S,1.5))))
        KspA_Dickson = np.power(10,(-171.945 - 0.077993*tempK + np.divide(2903.293,tempK) + 71.595*(np.log10(tempK)) + (-0.068393 + 0.0017276*tempK + np.divide(88.135,tempK))*(np.power(S,0.5)) - 0.10018*S + 0.0059415*(np.power(S,1.5))))
        KS_Dickson = np.exp((np.divide(-4276.1,tempK)) + 141.328 - 23.093*(np.log(tempK)) + ( (np.divide(-13856,tempK) + 324.57 - 47.986*(np.log(tempK))) * (np.power((IM),0.5)) ) + ( (np.divide(35474,tempK) - 771.54 + 114.723*(np.log(tempK))) * (IM) ) - (np.divide(2698,tempK))*(np.power(IM,1.5)) + (np.divide(1776,tempK))*(np.power(IM,2)) + np.log(1-0.001005*S))

        # ------------------ Calculate Ks ------------------ #

        self.K0 = np.divide(self.Output.molCO2, self.Output.fCO2) # No internal MCS K0 calculation
        self.K1 = self.Output.K1
        self.K2 = self.Output.K2
        self.KB = self.Output.KB
        self.KW = self.Output.KW
        self.KspC = np.divide(ThermoKspC, np.multiply(self.Output.gammaCa, (self.Output.gammaCO3 * np.divide(self.Output.molCO3 ,(self.Output.molCO3 + self.Output.molCaCO3 + self.Output.molMgCO3 + self.Output.molSrCO3) )))) # Modify internal MCS KspC calculation, include ion pairing effects
        self.KspA = np.divide(ThermoKspA, np.multiply(self.Output.gammaCa, (self.Output.gammaCO3 * np.divide(self.Output.molCO3 ,(self.Output.molCO3 + self.Output.molCaCO3 + self.Output.molMgCO3 + self.Output.molSrCO3) )))) # No internal MCS KspA calculation, include ion pairing effects
        self.KS = self.Output.KS

        # ------------------ OPTIONAL bias correction ------------------ #

        # NOTE: OPTIONAL bias correction to remedy the (minor) offset between modern MCS Ks and empirical Ks (Dickson, 2010)
        # Eq. S2 from Hain et al. (2015), see reference for details
        # To toggle off and print only raw MCS Ks, comment out lines 194-215

        # Must provide modern MCS Ks for the specified temperature.
        # To use the bias correction for a temperature other than 25º or 0º, run MarChemSpec with modern SW composition and create a new list of modern K values at that temperature. Add a new elif statement the same as the ones below.
        K_MCS_modern_25 = [2.868592e-02,1.465750e-06,1.085208e-09,2.466113e-09,6.088776e-14,4.685759e-07,7.028884e-07,1.041160e-01]
        K_MCS_modern_0 = [6.423481e-02,7.587261e-07,3.747503e-10,1.157564e-09,5.035354e-15,4.609165e-07,6.913989e-07,2.245352e-01]
        if tempC == 25:
            self.K0 = K0_Dickson + self.K0 - K_MCS_modern_25[0]
            self.K1 = K1_Dickson + self.K1 - K_MCS_modern_25[1]
            self.K2 = K2_Dickson + self.K2 - K_MCS_modern_25[2]
            self.KB = KB_Dickson + self.KB - K_MCS_modern_25[3]
            self.KW = KW_Dickson + self.KW - K_MCS_modern_25[4]
            self.KspC = KspC_Dickson + self.KspC - K_MCS_modern_25[5]
            self.KspA = KspA_Dickson + self.KspA - K_MCS_modern_25[6]
            self.KS = KS_Dickson + self.KS - K_MCS_modern_25[7]
        elif tempC == 0:
            self.K0 = K0_Dickson + self.K0 - K_MCS_modern_0[0]
            self.K1 = K1_Dickson + self.K1 - K_MCS_modern_0[1]
            self.K2 = K2_Dickson + self.K2 - K_MCS_modern_0[2]
            self.KB = KB_Dickson + self.KB - K_MCS_modern_0[3]
            self.KW = KW_Dickson + self.KW - K_MCS_modern_0[4]
            self.KspC = KspC_Dickson + self.KspC - K_MCS_modern_0[5]
            self.KspA = KspA_Dickson + self.KspA - K_MCS_modern_0[6]
            self.KS = KS_Dickson + self.KS - K_MCS_modern_0[7]
        else:
            print('\nScript could not find modern MarChemSpec Ks at the specified tempC in order to compute a bias correction. Continuing with un-corrected (raw) Ks for any runs with tempC =/= 25º or 0ºC.')


    def CalculateChem(self, comptype):

        # ------------------ Salinity ------------------ #  
        self.Sal = (self.Output.molH*1.0078 + self.Output.molNa*22.9899 + self.Output.molMg*24.305 + self.Output.molCa*40.078 + self.Output.molK*39.098 + self.Output.molMgOH*58.32 + self.Output.molSr*87.62 + self.Output.molMgF*43.305 + self.Output.molCaF*59.078 + self.Output.molCl*35.45 + self.Output.molSO4*96.06 + self.Output.molHSO4*97.06 + self.Output.molOH*17.008 + self.Output.molBr*79.9 + self.Output.molHCO3*61.062 + self.Output.molCO3*60.01 + self.Output.molBOH4*78.84 + self.Output.molF*18.99 + self.Output.molBOH3*61.832 + self.Output.molCO2*44.01 + self.Output.molHF*20.01 + self.Output.molCaCO3*100.09 + self.Output.molMgCO3*84.32 + self.Output.molSrCO3*147.63)*0.96355343
        
        # ------------------ Ionic strength ------------------ #  
        m_z_H = self.Output.molH * 1
        m_z_Na = self.Output.molNa * 1
        m_z_Mg = self.Output.molMg * 4
        m_z_Ca = self.Output.molCa * 4
        m_z_K = self.Output.molK * 1
        m_z_Sr = self.Output.molSr * 4

        m_z_Cl = self.Output.molCl * 1
        m_z_SO4 = self.Output.molSO4 * 4
        m_z_OH = self.Output.molOH * 1
        m_z_Br = self.Output.molBr * 1
        m_z_HCO3 = self.Output.molHCO3 * 1
        m_z_CO3 = self.Output.molCO3 * 4
        m_z_BOH4 = self.Output.molBOH4 * 1
        m_z_F = self.Output.molF * 1

        input_ion_sum = m_z_H + m_z_Na + m_z_Mg + m_z_Ca + m_z_K + m_z_Sr + m_z_Cl + m_z_SO4 + m_z_OH + m_z_Br + m_z_HCO3 + m_z_CO3 + m_z_BOH4 + m_z_F
        self.IonicStr = 0.5 * (input_ion_sum)

        # ------------------ Carbonate chemistry ------------------ #  
        self.Omega = self.Output.molCO3*self.Output.molCa/self.KspC
        self.pHF = -np.log10(self.Output.molH)
        self.pHT = -np.log10(self.Output.molH+self.Output.molHSO4)
        self.ALK = 2388
        self.DIC = 2038
    
    def TableEntry(self, comptype, tempC):

        # ------------------ Create dataframe ------------------ #  

        data = [-np.log10(self.K0), -np.log10(self.K1), -np.log10(self.K2), -np.log10(self.KB), -np.log10(self.KW), -np.log10(self.KspC), -np.log10(self.KspA), -np.log10(self.KS), tempC, self.Sal, (self.Output.molCa+self.Output.molCaCO3+self.Output.molCaF), (self.Output.molMg+self.Output.molMgCO3+self.Output.molMgF), (self.Output.molSO4+self.Output.molHSO4), self.Output.molNa, self.Output.molCl, self.IonicStr, self.pHF, self.pHT, self.ALK, self.DIC, self.Omega, self.Output.pCO2*1e6]
        self.Column = pd.DataFrame(data, columns=[comptype], index=['pK0','pK1','pK2','pKB','pKH2O','pKspC','pKspA','pKHSO4','TempC','SalA','Ca2+ (total)','Mg2+ (total)','SO42- (total)','Na+','Cl-','IonicStr','pHF','pHT','ALK','DIC','Omega','pCO2'])


if __name__ == '__main__':

    # ------------------ Generate table entry for each composition ------------------ #

    def ReturnTableEntry(filename, comptype, tempC):
        ProcessedOutput = GenerateTableEntry(rs2filename = filename+'.rs2', rs5filename = filename+'.rs5', comptype=comptype, tempC=tempC)
        return ProcessedOutput.Column

    # NOTE: For user purposes, these lines may be commented out and new filename strings and composition headers provided (plus a temperature in deg C) to generate a new table for a different composition(s). 
    Column1 = ReturnTableEntry('MCS_RSW_25deg','RSW_25deg',25.0)
    Column2 = ReturnTableEntry('MCS_RSW_0deg','RSW_0deg',0.0)
    Column3 = ReturnTableEntry('MCS_ESW_CaMg_25deg','ESW_CaMg_25deg',25.0)
    Column4 = ReturnTableEntry('MCS_ESW_CaMg_0deg','ESW_CaMg_0deg',0.0)
    Column5 = ReturnTableEntry('MCS_ESW_CaMg_NaCl_25deg','ESW_CaMg_NaCl_25deg',25.0)
    Column6 = ReturnTableEntry('MCS_ESW_CaMg_NaCl_0deg','ESW_CaMg_NaCl_0deg',0.0)
    Column7 = ReturnTableEntry('MCS_ESW_CaMgSO4_NaCl_25deg','ESW_CaMgSO4_NaCl_25deg',25.0)
    Column8 = ReturnTableEntry('MCS_ESW_CaMgSO4_NaCl_0deg','ESW_CaMgSO4_NaCl_0deg',0.0)

    # ------------------ Concatenate and write to file ------------------ #
    df = pd.concat([Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8], axis=1)
    # NOTE: If using a different number of compositions, be sure to edit [Column 1, Column 2...] to reflect the correct number of columns.
    
    print('\n')
    print(df)
    print('\n')

    df.to_csv('Table.csv')


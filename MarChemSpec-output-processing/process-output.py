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
        self.CalculateChem()
        self.TableEntry(comptype, tempC)
    

    def CalculateKs(self, tempC):

        # ------------------ Thermodynamic Ksp ------------------ #  
        tempK = 273.15+tempC
        ThermoKspC = np.exp(303.1308 - np.divide(13348.09,tempK) -48.7537*np.log(tempK))
        ThermoKspA = np.exp(303.5363 - np.divide(13348.09,tempK) - 48.7537*np.log(tempK)) 

        # ------------------ Calculate Ks ------------------ #
        self.K0 = np.divide(self.Output.molCO2, self.Output.fCO2) # No internal MCS K0 calculation
        self.K1 = self.Output.K1
        self.K2 = self.Output.K2
        self.KB = self.Output.KB
        self.KW = self.Output.KW
        self.KspC = np.divide(ThermoKspC, np.multiply(self.Output.gammaCa, (self.Output.gammaCO3 * np.divide(self.Output.molCO3 ,(self.Output.molCO3 + self.Output.molCaCO3 + self.Output.molMgCO3 + self.Output.molSrCO3) )))) # Modify internal MCS KspC calculation
        self.KspA = np.divide(ThermoKspA, np.multiply(self.Output.gammaCa, (self.Output.gammaCO3 * np.divide(self.Output.molCO3 ,(self.Output.molCO3 + self.Output.molCaCO3 + self.Output.molMgCO3 + self.Output.molSrCO3) )))) # No internal MCS KspA calculation
        self.KS = self.Output.KS


    def CalculateChem(self):

        # ------------------ Salinity ------------------ #  
        self.Sal = self.Output.molH*1.0078 + self.Output.molNa*22.99 + self.Output.molMg*24.31 + self.Output.molCa*40.08 + self.Output.molK*39.10 + self.Output.molMgOH*41.318 + self.Output.molSr*87.62 + self.Output.molMgF*43.31 + self.Output.molCaF*59.08 + self.Output.molCl*35.45 + self.Output.molSO4*96.07 + self.Output.molHSO4*97.064 + self.Output.molOH*17.008 + self.Output.molBr*79.9 + self.Output.molHCO3*61.018 + self.Output.molCO3*60.009 + self.Output.molBOH4*78.84 + self.Output.molF*19 + self.Output.molBOH3*61.83 + self.Output.molCO2*44.01 + self.Output.molHF*20.008 + self.Output.molMgCO3*84.32 + self.Output.molCaCO3*100.087 + self.Output.molSrCO3*147.63

        # ------------------ Ionic strength ------------------ #  
        m_z_H = self.Output.molH * 1
        m_z_Na = self.Output.molNa * 1
        m_z_Mg = self.Output.molMg * 4
        m_z_Ca = self.Output.molCa * 4
        m_z_K = self.Output.molK * 1
        m_z_MgOH = self.Output.molMgOH * 1
        m_z_Sr = self.Output.molSr * 4
        m_z_MgF = self.Output.molMgF * 1
        m_z_CaF = self.Output.molCaF * 1

        m_z_Cl = self.Output.molCl * 1
        m_z_SO4 = self.Output.molSO4 * 4
        m_z_HSO4 = self.Output.molHSO4 * 1
        m_z_OH = self.Output.molOH * 1
        m_z_Br = self.Output.molBr * 1
        m_z_HCO3 = self.Output.molHCO3 * 1
        m_z_CO3 = self.Output.molCO3 * 4
        m_z_BOH4 = self.Output.molBOH4 * 1
        m_z_F = self.Output.molF * 1

        input_ion_sum = m_z_H + m_z_Na + m_z_Mg + m_z_Ca + m_z_K + m_z_MgOH + m_z_Sr + m_z_MgF + m_z_CaF + m_z_Cl + m_z_SO4 + m_z_HSO4 + m_z_OH + m_z_Br + m_z_HCO3 + m_z_CO3 + m_z_BOH4 + m_z_F
        self.IonicStr = 0.5 * (input_ion_sum)

        # ------------------ Omega ------------------ #  
        self.Omega = self.Output.molCO3*self.Output.molCa/self.KspC


    def TableEntry(self, comptype, tempC):

        # ------------------ Create dataframe ------------------ #  

        data = [self.K0, self.K1, self.K2, self.KB, self.KW, self.KspC, self.KspA, self.KS, tempC, self.Sal, self.IonicStr, self.Omega]
        self.Column = pd.DataFrame(data, columns=[comptype], index=['K0','K1','K2','KB','KW','KspC','KspA','KS','TempC','Sal','IonicStr','Omega'])


if __name__ == '__main__':

    # ------------------ Generate table entry for each composition ------------------ #

    def ReturnTableEntry(filename, comptype, tempC):
        ProcessedOutput = GenerateTableEntry(rs2filename = filename+'.rs2', rs5filename = filename+'.rs5', comptype=comptype, tempC=tempC)
        return ProcessedOutput.Column

    # NOTE: For user purposes, these lines may be commented out and new filename strings and composition headers provided (plus a temperature in deg C) to generate a new table for a different composition(s). 
    Column1 = ReturnTableEntry('MCS_RSW_25deg','RSW_25deg',25.0)
    Column2 = ReturnTableEntry('MCS_RSW_0deg','RSW_0deg',0.0)
    # Column3 = ReturnTableEntry('MCS_ESW_CaMg_25deg','ESW_CaMg_25deg',25.0)
    # Column4 = ReturnTableEntry('MCS_ESW_CaMg_0deg','ESW_CaMg_0deg',0.0)
    # Column5 = ReturnTableEntry('MCS_ESW_CaMg_NaCl_25deg','ESW_CaMg_NaCl_25deg',25.0)
    # Column6 = ReturnTableEntry('MCS_ESW_CaMg_NaCl_0deg','ESW_CaMg_NaCl_0deg',0.0)
    # Column7 = ReturnTableEntry('MCS_ESW_CaMgSO4_NaCl_25deg','ESW_CaMgSO4_NaCl_25deg',25.0)
    # Column8 = ReturnTableEntry('MCS_ESW_CaMgSO4_NaCl_0deg','ESW_CaMgSO4_NaCl_0deg',0.0)

    # ------------------ Concatenate and write to file ------------------ #
    df = pd.concat([Column1, Column2], axis=1)
    # NOTE: If using a different number of compositions, be sure to edit [Column 1, Column 2...] to reflect the correct number of columns.

    df.to_csv('Table1.csv')


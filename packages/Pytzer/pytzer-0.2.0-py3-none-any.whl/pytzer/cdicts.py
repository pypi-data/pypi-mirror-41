import autograd.numpy as np
from . import coeffs, data, jfuncs

class cdict:
    def __init__(self):
        self.dh    = {}
        self.bC    = {'H-OH': coeffs.bC_zero}
        self.theta = {}
        self.jfunc = []
        self.psi   = {}
        self.K     = {}
        
    # Get equilibrium equations
    def getKeq(self,T, mH=None, gH=None, mOH=None, gOH=None, 
               mHSO4=None, gHSO4=None, mSO4=None, gSO4=None):
        
        # Find which equilibria are stored in dict
        Klist = self.K.keys()
        
        # Initialise Keq equation
        Keq = np.zeros_like(T, dtype='float64')
        
        if 'H2O' in Klist:
            Keq = Keq + np.log(gH*mH * gOH*mOH) \
                - np.log(self.K['H2O'](T)[0])
        
        if 'HSO4' in Klist:
            Keq = Keq + np.log(gH*mH * gSO4*mSO4 \
                / (gHSO4*mHSO4)) \
                - np.log(self.K['HSO4'](T)[0])
            
        return Keq
    
    # Populate with zero-functions
    def add_zeros(self,eles):
        
        _,cats,anis,_ = data.ele2ions(eles)

        # Populate cdict with zero functions
        for cat in cats:
            for ani in anis:
                
                istr = cat + '-' + ani
                if istr not in self.bC.keys():
                    self.bC[istr] = coeffs.bC_zero
                
        for C0 in range(len(cats)):
            for C1 in range(C0+1,len(cats)):
                
                istr = cats[C0] + '-' + cats[C1]
                if istr not in self.theta.keys():
                    self.theta[istr] = coeffs.theta_zero
                
                for ani in anis:
                    
                    istr = cats[C0] + '-' + cats[C1] + '-' + ani
                    if istr not in self.psi.keys():
                        self.psi[istr] = coeffs.psi_zero
        
        for A0 in range(len(anis)):
            for A1 in range(A0+1,len(anis)):
                
                istr = anis[A0] + '-' + anis[A1]
                if istr not in self.theta.keys():
                    self.theta[istr] = coeffs.theta_zero
                
                for cat in cats:
                    
                    istr = cat + '-' + anis[A0] + '-' + anis[A1]
                    if istr not in self.psi.keys():
                        self.psi[istr] = coeffs.psi_zero
        

# === HUMPHREYS UNPUBLISHED ===================================================
        
MPH = cdict()

MPH.dh['Aosm'] = coeffs.Aosm_MPH
MPH.dh['AH'  ] = coeffs.AH_MPH

MPH.bC['Na-Cl'] = coeffs.bC_Na_Cl_A92ii
MPH.bC['K-Cl' ] = coeffs.bC_K_Cl_A99
MPH.bC['Ca-Cl'] = coeffs.bC_Ca_Cl_GM89
MPH.bC['Mg-Cl'] = coeffs.bC_Mg_Cl_PP87i

MPH.jfunc = jfuncs.P75_eq47

# === MOLLER 1988 =============================================================
M88 = cdict()

# Debye-Hueckel slope as cf.dh['Aosm']
M88.dh['Aosm'] = coeffs.Aosm_M88

# betas and Cs as cf.bC['cation-anion']
M88.bC['Ca-Cl' ] = coeffs.bC_Ca_Cl_M88
M88.bC['Ca-SO4'] = coeffs.bC_Ca_SO4_M88
M88.bC['Na-Cl' ] = coeffs.bC_Na_Cl_M88
M88.bC['Na-SO4'] = coeffs.bC_Na_SO4_M88

# thetas as cf.theta['cation1-cation2'] with cations in alph. order
# c-c'
M88.theta['Ca-Na' ] = coeffs.theta_Ca_Na_M88
# a-a'
M88.theta['Cl-SO4'] = coeffs.theta_Cl_SO4_M88

# Unsymmetrical mixing terms
M88.jfunc = jfuncs.P75_eq47

# psis as cf.psi['cation1-cation2-anion'] with cations in alph. order
#   or as cf.psi['cation-anion1-anion2']  with anions  in alph. order
# c-c'-a
M88.psi['Ca-Na-Cl' ] = coeffs.psi_Ca_Na_Cl_M88
M88.psi['Ca-Na-SO4'] = coeffs.psi_Ca_Na_SO4_M88
# c-a-a'
M88.psi['Ca-Cl-SO4'] = coeffs.psi_Ca_Cl_SO4_M88
M88.psi['Na-Cl-SO4'] = coeffs.psi_Na_Cl_SO4_M88

# Dissociation constants as cf.K['acid']
M88.K['H2O'] = coeffs.dissoc_H2O_M88

# === GREENBERG & MOLLER 1989 =================================================
GM89 = cdict()

# Debye-Hueckel slope
GM89.dh['Aosm'] = coeffs.Aosm_M88

# betas and Cs as cf.bC['cation-anion']
GM89.bC['Ca-Cl' ] = coeffs.bC_Ca_Cl_GM89
GM89.bC['Ca-SO4'] = coeffs.bC_Ca_SO4_M88
GM89.bC['K-Cl'  ] = coeffs.bC_K_Cl_GM89
GM89.bC['K-SO4' ] = coeffs.bC_K_SO4_GM89
GM89.bC['Na-Cl' ] = coeffs.bC_Na_Cl_M88
GM89.bC['Na-SO4'] = coeffs.bC_Na_SO4_M88

# thetas as cf.theta['cation1-cation2'] with cations in alph. order
# c-c'
GM89.theta['Ca-K'  ] = coeffs.theta_Ca_K_GM89
GM89.theta['Ca-Na' ] = coeffs.theta_Ca_Na_M88
GM89.theta['K-Na'  ] = coeffs.theta_K_Na_GM89
# a-a'
GM89.theta['Cl-SO4'] = coeffs.theta_Cl_SO4_M88

# Unsymmetrical mixing terms
GM89.jfunc = jfuncs.P75_eq47

# psis as cf.psi['cation1-cation2-anion'] with cations in alph. order
#   or as cf.psi['cation-anion1-anion2']  with anions  in alph. order
# c-c'-a
GM89.psi['Ca-K-Cl'  ] = coeffs.psi_Ca_K_Cl_GM89
GM89.psi['Ca-K-SO4' ] = coeffs.psi_Ca_K_SO4_GM89
GM89.psi['Ca-Na-Cl' ] = coeffs.psi_Ca_Na_Cl_M88
GM89.psi['Ca-Na-SO4'] = coeffs.psi_Ca_Na_SO4_M88
GM89.psi['K-Na-Cl'  ] = coeffs.psi_K_Na_Cl_GM89
GM89.psi['K-Na-SO4' ] = coeffs.psi_K_Na_SO4_GM89
# c-a-a'
GM89.psi['Ca-Cl-SO4'] = coeffs.psi_Ca_Cl_SO4_M88
GM89.psi['K-Cl-SO4' ] = coeffs.psi_K_Cl_SO4_GM89
GM89.psi['Na-Cl-SO4'] = coeffs.psi_Na_Cl_SO4_M88

# Dissociation constants as cf.K['acid']
GM89.K['H2O'] = coeffs.dissoc_H2O_M88

# === CLEGG ET AL 1994=========================================================
CRP94 = cdict()

CRP94.dh['Aosm'] = coeffs.Aosm_CRP94

CRP94.bC['H-HSO4'] = coeffs.bC_H_HSO4_CRP94
CRP94.bC['H-SO4' ] = coeffs.bC_H_SO4_CRP94

CRP94.theta['HSO4-SO4'] = coeffs.theta_HSO4_SO4_CRP94

CRP94.jfunc = jfuncs.P75_eq47

CRP94.psi['H-HSO4-SO4'] = coeffs.psi_H_HSO4_SO4_CRP94

CRP94.K['HSO4'] = coeffs.dissoc_HSO4_CRP94

# === MIAMI - MILLERO & PIERROT 1998 ==========================================
MIAMI = cdict()

MIAMI.dh['Aosm'] = coeffs.Aosm_M88

# Table A1
MIAMI.bC['Na-Cl' ] = coeffs.bC_Na_Cl_M88
MIAMI.bC['K-Cl'  ] = coeffs.bC_K_Cl_GM89
MIAMI.bC['K-SO4' ] = coeffs.bC_K_SO4_GM89
MIAMI.bC['Ca-Cl' ] = coeffs.bC_Ca_Cl_GM89
MIAMI.bC['Ca-SO4'] = coeffs.bC_Ca_SO4_M88
MIAMI.bC['Ca-SO3'] = coeffs.bC_Ca_SO4_M88
MIAMI.bC['Sr-SO4'] = coeffs.bC_Ca_SO4_M88

# Table A2
MIAMI.bC['Mg-Cl' ] = coeffs.bC_Mg_Cl_PP87i
MIAMI.bC['Mg-SO4'] = coeffs.bC_Mg_SO4_PP86ii

# Table A3
#MIAMI.bC['Na-HSO4'] = coefFs.bC_Na_HSO4_PM97
#MIAMI.bC['Na-HCO3'] = coeffs.bC_Na_HCO3_PP82
MIAMI.bC['Na-SO4' ] = coeffs.bC_Na_SO4_HPR93
#MIAMI.bC['Na-CO3' ] = coeffs.bC_Na_CO3_PP82
MIAMI.bC['Na-BOH4'] = coeffs.bC_Na_BOH4_SRRJ87
#MIAMI.bC['Na-HS'  ] = coeffs.bC_Na_HS_H88
#MIAMI.bC['Na-CNS' ] = coeffs.bC_Na_CNS_SP78
#MIAMI.bC['Na-SO3' ] = coeffs.bC_Na_SO3_M89
#MIAMI.bC['Na-HSO3'] = coeffs.bC_Na_HSO3_M89

# Table A4
#MIAMI.bC['K-HCO3 '] = coeffs.bC_K_HCO3_R83
#MIAMI.bC['K-CO3'  ] = coeffs.bC_K_CO3_S87a
MIAMI.bC['K-BOH4' ] = coeffs.bC_K_BOH4_SRRJ87
#MIAMI.bC['K-HS'   ] = coeffs.bC_K_HS_M95
#MIAMI.bC['K-H2PO4'] = coeffs.bC_K_H2PO4_SP78
#MIAMI.bC['K-CNS'  ] = coeffs.bC_K_CNS_SP78

# Table A5
#MIAMI.bC['Mg-Br'  ] = coeffs.bC_Mg_Br_SP78
#MIAMI.bC['Mg-BOH4'] = coeffs.bC_Mg_BOH4_S87b
#MIAMI.bC['Mg-ClO4'] = coeffs.bC_Mg_ClO4_SP78
#MIAMI.bC['Ca-Br'  ] = coeffs.bC_Ca_Br_SP78
#MIAMI.bC['Ca-BOH4'] = coeffs.bC_Ca_BOH4_S87b
#MIAMI.bC['Ca-ClO4'] = coeffs.bC_Ca_ClO4_SP78

# Table A6
#MIAMI.bC['Sr-Br'  ] = coeffs.bC_Sr_Br_SP78
#MIAMI.bC['Sr-NO3' ] = coeffs.bC_Sr_NO3_SP78
#MIAMI.bC['Sr-ClO4'] = coeffs.bC_Sr_ClO4_SP78
#MIAMI.bC['Sr-HSO3'] = coeffs.bC_Sr_HSO3_SP78
#MIAMI.bC['Sr-BOH4'] = coeffs.bC_Ca_BOH4_S87b

# Table A7
MIAMI.bC['Na-I'   ] = coeffs.bC_Na_I_MP98
MIAMI.bC['Na-Br'  ] = coeffs.bC_Na_Br_MP98
MIAMI.bC['Na-F'   ] = coeffs.bC_Na_F_MP98
MIAMI.bC['K-Br'   ] = coeffs.bC_K_Br_MP98
MIAMI.bC['K-F'    ] = coeffs.bC_K_F_MP98
MIAMI.bC['K-OH'   ] = coeffs.bC_K_OH_MP98
MIAMI.bC['K-I'    ] = coeffs.bC_K_I_MP98
#MIAMI.bC['Na-ClO3'] = coeffs.bC_Na_ClO3_MP98
#MIAMI.bC['K-ClO3' ] = coeffs.bC_K_ClO3_MP98
#MIAMI.bC['Na-ClO4'] = coeffs.bC_Na_ClO4_MP98
#MIAMI.bC['Na-BrO3'] = coeffs.bC_Na_BrO3_MP98
#MIAMI.bC['K-BrO3' ] = coeffs.bC_K_BrO3_MP98
#MIAMI.bC['Na-NO3' ] = coeffs.bC_Na_NO3_MP98
#MIAMI.bC['K-NO3'  ] = coeffs.bC_K_NO3_MP98
#MIAMI.bC['Mg-NO3' ] = coeffs.bC_Mg_NO3_MP98
#MIAMI.bC['Ca-NO3' ] = coeffs.bC_Ca_NO3_MP98
#MIAMI.bC['H-Br'   ] = coeffs.bC_H_Br_MP98
#MIAMI.bC['Sr-Cl'  ] = coeffs.bC_Sr_Cl_MP98
#MIAMI.bC['NH4-Cl' ] = coeffs.bC_NH4_Cl_MP98
#MIAMI.bC['NH4-Br' ] = coeffs.bC_NH4_Br_MP98
#MIAMI.bC['NH4-F'  ] = coeffs.bC_NH4_F_MP98

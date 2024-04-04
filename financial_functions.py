''' Engineering Economics Project
    MohammadHosein Mozafary Kermany
    810901107
'''
import pandas as pd
import numpy_financial as npf
class FinancialFactors:
    def __init__(self):
        pass
    def F_A_given_A(self,i, n, A):
        return A * (((1 + i) ** n - 1) / i)
    
    def F_P_given_P(self,i, n, P): 
        return P * ((1 + i) ** n)

    def P_F_given_F(self,i, n, F): 
        return F / ((1 + i) ** n)

    def A_F_given_F(self,i, n, F): 
        return F * (i / ((1 + i) ** n - 1))

    def A_P_given_P(self,i, n, P): 
        return P * (i*((1+i)**n))/((1+i)**n-1)

    def P_A_given_A(self,i, n, A):
        return A * ((1+i)**n-1)/(i*((1+i)**n))


    def Irr(self, cash_flows):
        
        
        irr=npf.irr(cash_flows)
        return irr
    
        





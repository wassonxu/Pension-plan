# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:46:31 2020

@author: Administrator
"""

# retirement pension / pension plan  calculation

import argparse

age = 44
MonthlyContributeAmount= 1000
Interest_Rate_Per_Year = 0.038
I_want_per_month=3300


retirement_time = 60
MoneyContributeTime= 12* (retirement_time-age)  # how many months
interest_Yearly = 0

for i in range(MoneyContributeTime):
    interest_Yearly += MonthlyContributeAmount * (1+Interest_Rate_Per_Year) **( i // 12 ) - MonthlyContributeAmount
    # print (interest_Yearly)
    
All_priciple = MoneyContributeTime * MonthlyContributeAmount

All_money_left= All_priciple+interest_Yearly


Yearlived= 98
Year_Get_pension = (Yearlived-retirement_time)
Month_Get_pension = (Yearlived-retirement_time)*12

def All_pension_deduction(All_money_left):
    All_pension_deduct = (I_want_per_month - (All_money_left* Interest_Rate_Per_Year)/12)*12
    All_money_left -= All_pension_deduct 
    return All_money_left

for i in range(Year_Get_pension):
    print (All_pension_deduction(All_money_left))
    All_money_left = All_pension_deduction(All_money_left)
    
    

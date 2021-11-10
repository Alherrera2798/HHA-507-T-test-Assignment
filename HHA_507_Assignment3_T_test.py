# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:30:28 2021

T-Test Assignmnet

@author: Alejandro Herrera
"""

## Importing any libraries that will be used in this test 

import pandas as pd
import scipy.stats as stats 
from scipy.stats import shapiro
from matplotlib import pyplot
from scipy.stats import spearmanr, pearsonr

from scipy.stats import ttest_ind
## importing our datasets from the github repo
'''
    We want to reduce the sample size of the dataset to 100.
    Opening the entire dataset will overwhelm our system
    The list() function will provide us a list of attributes the dataset contains 
        
'''
diabetic = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')
diabetic_small = diabetic.sample(100)
list(diabetic_small)

timeinhospital = diabetic['time_in_hospital']
labprocedures = diabetic['num_lab_procedures']

# Total count of procedures using dataset -> craeting variables from attributes 
# Displayed in the brackets

diabetic['totalCountProcedures'] = diabetic['num_procedures'] + diabetic['num_lab_procedures']
diabetic['totalCountProcedures'].describe()
totalCountProcedures = diabetic['totalCountProcedures'].array
""" 
TOTALCOUNTPROCEDURES.DESCRIBE()
count    101766.000000
mean         44.435371
std          19.846605
min           1.000000
25%          33.000000
50%          45.000000
75%          58.000000
max         135.000000
Name: totalCountProcedures, dtype: float64"""

#T-Test
#Differences 

# 1) Is there a difference between sex (M:F) and the number of days in hospital?
Female = diabetic[diabetic['gender']=='Female']
Male = diabetic[diabetic['gender']=='Male']

Female['totalCountProcedures'] = Female['num_procedures'] + Female['num_lab_procedures']
Male['totalCountProcedures'] = Male['num_procedures'] + Male['num_lab_procedures']
ttest_ind(Female['totalCountProcedures'], Male['totalCountProcedures'])

### Ttest_indResult(statistic=-0.6747218803792331, pvalue=0.4998540133474586)  ###

##There is no difference in average number of procedures between males and females 
##because the p-value is greater than 0.05, which means that we fail to reject the null hypothesis 

#### difference between gender (M:F) and the number of days in hospital

ttest_ind (Female['time_in_hospital'], Male['time_in_hospital'])
###statistic=9.542637042242887, pvalue=1.4217299655114968e-21

# 2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
Caucasian = diabetic[diabetic['race']=='Caucasian']
AfricanAmerican = diabetic[diabetic['race']=='AfricanAmerican']

ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

#Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)
##There is a significant difference in time in hospital between Caucasian and African America
#because the p-value is less than 0.05, which is allowing us to reject the null hypothesis 

# 3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
Asian = diabetic[diabetic['race']=='Asian']
AfricanAmerican = diabetic[diabetic['race']=='AfricanAmerican']
ttest_ind(Asian['totalCountProcedures'], AfricanAmerican['totalCountProcedures'])
###statistic=-3.7897663070631253, pvalue=0.00015123463923369748

##There is a significant difference in time in hospital between Asians and African Americans
#because the p-value is less than 0.05, which is allowing us to reject the null hypothesis 




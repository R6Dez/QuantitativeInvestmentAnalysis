#!/usr/bin/env python
# coding: utf-8

# 
# Chapter 6 Problems: 10

# 6.10
# A) H0: Variance before Oct. 1987 = Variance after Oct. 1987
#    H1: Variance before Oct. 1987 ≠ Variance after Oct. 1987
#     
# B) Test statistic = f-stat from the f-test
#    f-stat=larger variance/smaller variance
#    f-stat=22.367/15.795 = 1.416
#    df1 = 120, df2 = 120
#   
# C) critical value = 1.3519
#    Accept H0, since the critical value < than f-stat. 

# Python exercise

# Compare the performance of the following two mutual funds: <BR>
# Fidelity Magellan, ticker: FMGKX <br>
# Vanguard 500 Index Fund, ticker:VFINX <br>
# Read in adjusted close price for both funds from Yahoo finance. Use the earliest date possible when data are available for both funds

# In[21]:


import pandas as pd
import scipy.stats as sst
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

tickers = ['FMGKX', 'VFINX']
mydata = pd.DataFrame()

for t in tickers:
    mydata[t] = pdr.get_data_yahoo(t, start='1997-1-1')['Adj Close']


# Calculate the simple daily returns using Adj. Close

# In[18]:


simple_daily_return = mydata/mydata.shift(1)-1
simple_daily_return = simple_daily_return.dropna()
simple_daily_return


# Calculate mean and standard deviation of the daily returns

# In[19]:


simple_daily_return.mean()


# In[20]:


simple_daily_return.std()


# Answer the following questions using a 5% signficance interval

# Test whether the mean daily return of Fidelity Magellan is equal to 0 

# H0:statistic > 1.96
# H1:statistic < 1.96

# In[37]:


sst.ttest_1samp(a=simple_daily_return['FMGKX'],popmean=0)


# H1, accept the hypothesis

# Test whether the mean daily return of Fidelity Magellan is equal to 0.0004

# H0:statistic > 1.96
# H1:statistic < 1.96

# In[31]:


sst.ttest_1samp(a=simple_daily_return['FMGKX'],popmean=0.0004)


# H1, accept the hypothesis

# Test whether the mean daily return of Fidelity Maggellan and Vanguard 500 Index are equal

# In[39]:


sst.ttest_ind(a=simple_daily_return['FMGKX'],b=simple_daily_return['VFINX'],equal_var=False)


# Test whether the variance of daily return of Fidelity Maggellan are equal to 0.0001

# In[ ]:


H0:chi squared test result > critical value
H1:chi squared test result < critical value


# In[45]:


hyp_var=0.0001 #var under the null


# In[48]:


FMGKX_var=simple_daily_return['FMGKX'].var()


# In[46]:


df_FMGKX=simple_daily_return['FMGKX'].count()-1


# In[50]:


chi_squared_stat=df_FMGKX*FMGKX_var/hyp_var
chi_squared_stat


# In[53]:


critical_value=sst.chi2.ppf(q=0.95,df=df_FMGKX)
critical_value


# Reject null hypothesis, chi squared test result > critical value

# Test whether the variance of daily return are the same for Fidelity Maggellan and Vanguard 500 Index 

# In[57]:


F_stat=max(simple_daily_return['FMGKX'].var()/simple_daily_return['VFINX'].var(),
          simple_daily_return['VFINX'].var()/simple_daily_return['FMGKX'].var())
F_stat


# In[59]:


sst.f.ppf(0.95,dfn=simple_daily_return['FMGKX'].count()-1,dfd=simple_daily_return['VFINX'].count()-1)


# Reject the null hypothesis, f-stat > critival value

# Would your answer change if you use a 10% significance level?

# In[60]:


sst.f.ppf(0.9,dfn=simple_daily_return['FMGKX'].count()-1,dfd=simple_daily_return['VFINX'].count()-1)


# No, I would not change my answer.

# Calculate the Spearman rank correlation coefficient and its P-value. What do these numbers mean?

# In[61]:


sst.spearmanr(simple_daily_return)


# Correlation shows how correlated the two stocks are, P-value is the probability that any correlation is due to chance. 

# Calculate the Pearson correlation coefficient and its P-value. What do these numbers mean?

# In[62]:


sst.pearsonr(simple_daily_return['VFINX'],simple_daily_return['FMGKX'])


# The two stocks have very high correlation and there is high confidence due to the p-value being close to 0.

# You are considering investing in one or both of these funds. Do you prefer one fund to the other? Why?

# I would invest in VFINX since it has a higher mean and lower standard deviation, so the stock has a higher return for less risk. 

# Optional challenge: None <BR>
# Please start working on your final project

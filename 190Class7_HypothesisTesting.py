#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


# In[2]:


import scipy.stats as sst
import numpy as np


# In[3]:


#culumative distribution function, returns probability
#probability of everything to the left of 1.2 in a normal distribution
#to get everything to the right, compute (1 - cdf)
sst.norm.cdf(1.2)


# In[4]:


#perfent point function, returns critical value
#returns outcome, when given a probability (inverse of cdf)
sst.norm.ppf(0.975)


# In[5]:


sst.t.cdf(1.2, df=10)


# In[6]:


tickers = ['MSFT', 'AAPL']

sec_data=pd.DataFrame()

for t in tickers:
        sec_data[t]=pdr.get_data_yahoo(t, start='1997-1-1')['Adj Close']


# In[7]:


sec_data.head()


# In[8]:


sec_returns=(sec_data/sec_data.shift(1))-1
sec_returns


# In[9]:


sec_returns=sec_returns.dropna()
sec_returns


# In[10]:


sec_returns.mean()


# In[11]:


sec_returns.std()


# In[12]:


#for large samples, t-test and z-test give same results, if sample < 30, t-test is better
sst.ttest_1samp(a=sec_returns['MSFT'], popmean=0)


# 5% confidence interval, CV=1.96
# test statistic = 3.08
# test statistic > CV, reject null hypothesis that Microsoft average daily return is 0. 
# if pvalue is less than 5%, also reject the null hypothesis

# In[13]:


sst.ttest_1samp(a=sec_returns['AAPL'], popmean=0.000754)


# In[14]:


#Null hypothesis: MSFT return is the same as AAPL return
sst.ttest_ind(a=sec_returns['MSFT'],b=sec_returns['AAPL'],equal_var=False)


# In[15]:


sst.ttest_rel(a=sec_returns['MSFT'],b=sec_returns['AAPL'])


# In[16]:


#testing a single variance
hyp_std=0.02 #std under the null, denominator


# In[17]:


df_MSFT=sec_returns['MSFT'].count()-1


# In[18]:


MSFT_std=sec_returns['MSFT'].std()


# In[19]:


chi_squared_stat=df_MSFT*MSFT_std**2/hyp_std**2
chi_squared_stat


# In[20]:


critical_value=sst.chi2.ppf(q=0.95, df=df_MSFT)
critical_value


# chi_squared_stat < critical_value, accept the null hypothesis
# MSFT variance is less than 0.02^2
# 
# What is the null we're accepting?

# In[21]:


#Finding the higher variance ratio
F_stat=max(sec_returns['MSFT'].var()/sec_returns['AAPL'].var(), 
          sec_returns['AAPL'].var()/sec_returns['MSFT'].var())
F_stat


# In[22]:


CV = sst.f.ppf(0.95, dfn=sec_returns['MSFT'].count()-1, dfd=sec_returns['AAPL'].count()-1)
CV


# In[23]:


#Pearson correlation test
#implies correlation=0


# In[24]:


sst.pearsonr(sec_returns['MSFT'],sec_returns['AAPL'])
#(correlation coefficient(0-1), p-value from hypothesis test)


# In[25]:


#p-value is smaller than 5% and cv<f-stat, reject the null hypothesis
#Correlation is not 0


# In[26]:


sst.spearmanr(sec_returns)


# In[27]:


#Spearman uses a ranking order rather than numerical order, not influenced by outliers.
#Check if results are driven by crisis periods, or outliers


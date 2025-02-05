#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[6]:


import pandas as pd


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


import matplotlib.dates as mdates


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import datetime as dt


# In[11]:


import time


# In[12]:


import yfinance as yf


# In[27]:


def get_info_on_stock(ticker):
    stock = yf.Ticker(ticker)
    hist=stock.history(period="max")["Close"]
    #print(stock.major_holders)
    #print(stock.institutional_holders)
    #print(stock.financials)
    
    #print(stock.balance_sheet)
    #print(stock.cashflow)
    print(stock.recommendations)


# In[51]:


get_info_on_stock("GAIL.NS")


# In[ ]:





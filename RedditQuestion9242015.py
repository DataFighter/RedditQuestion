
# coding: utf-8

# In[46]:

# Needs requests and pandas. I've piped these in the past
# I also had to run 
# 'pip install --upgrade pyopenssl ndg-httpsclient pyasn1'
# To get this to work. I think that is because there was an issue with SSL
# Here is the StackOverflow question
# http://stackoverflow.com/questions/32755884/ssl-error-when-opening-link-in-python-works-fine-in-browser/32756035#32756035

import urllib2
from requests import get
import pandas as pd


# I'm not sure how high the urls go
# So just input the highest numbered URL to NumpPages
# for example if the highest page is 25 NumPages = 25

NumPages = 5
for i in range(NumPages):
    urlstr = 'https://api.cilabs.net/v1/conferences/ws15/info/attendees?page='+str(i)
    InputJson = get(urlstr)
    df = pd.DataFrame(InputJson.json()['attendees'])
    filestr = 'page'+str(i+1)+'.csv'
    df.to_csv(filestr,encoding = 'utf-8')
    
# output are csvs that go page1.csv, page2.csv and so on


# In[ ]:




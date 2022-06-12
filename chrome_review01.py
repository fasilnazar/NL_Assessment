#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit


# In[2]:


import pandas as pd
import streamlit as st


# In[3]:


import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# In[4]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent = SentimentIntensityAnalyzer()


# In[5]:


st.title("Chrome Reviews - positive reviews with low ratings")


# In[6]:


df=pd.read_csv("chrome_reviews.csv")
df.head()


# In[7]:


df.drop(["ID","Review URL", "User Name","Developer Reply", "Version","Review Date","App ID","Thumbs Up"],axis=1,inplace=True)


# In[8]:


df.head()


# In[9]:


df_1star=df[df.Star == 1]


# In[10]:


df_1star.head()


# In[11]:


polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in df_1star['Text']]


# In[12]:


df_1star['sentiment_score'] = polarity


# In[13]:


df_1star.head(10)


# In[14]:


df_final=df_1star[df_1star.sentiment_score >= .6]


# In[15]:


df_final.head(100)


# In[16]:


uploaded_file = st.file_uploader("Choose a file for checking review/rating discrepancy")
st.write("Waiting for input")
if uploaded_file is not None:
     df_test = pd.read_csv(uploaded_file)


# In[17]:


st.write("The list of reviews where the reviews and ratings probably don't match are as below")
print(df_final)


# In[ ]:





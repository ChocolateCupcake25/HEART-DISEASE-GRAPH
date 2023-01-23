#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name: Ziyah")
print("We will be cleaning heart disease data, and conclude which age group has high risk of heart stroke as per diabetes and hight blood pressure level")
print("We will also find which gender has the most not normal platelets count in blood, and plot a pie chart around it")


# # Task 1 - Find the diabetic and hight blood pressure patients across all age groups, and conclude the risk heart stroke is higher in which age group

# In[2]:


#Import libraries
import pandas as pd
import matplotlib.pyplot as plt 

#read the csv
df = pd.read_csv('heart_disease.csv')
df


# In[3]:


#Filter by diabetes(condition will be who has diabetes) and create new dataframe
diabetic_patient=df.loc[df["diabetes"]==1]
diabetic_patient


# In[18]:


#On this new data frame perform group operation as per age and create new dataframe 
diabetic = df.groupby('age')['diabetes'].mean().reset_index()
diabetic


# In[19]:


#Filter by high_blood_pressure(condition will be who has high_blood_pressure) and create new dataframe
high_blood_pressure=df.loc[df["high_blood_pressure"]==1]
high_blood_pressure

high_bp = df.groupby('age')['high_blood_pressure'].mean().reset_index()
high_bp


# In[20]:


#On this new data frame perform group operation as per age and create new dataframe 

groupbyage = df.groupby('age')[['diabetes','high_blood_pressure']].count().reset_index()
groupbyage


# In[21]:


#plot the scatter graph to show which age group is more prone to diabetes

age = groupbyage['age']
high_bp = groupbyage['high_blood_pressure']

plt.scatter(age, high_bp, label = "High bp")

diabetic = groupbyage['diabetes']

plt.scatter(age, diabetic, label = "Diabeties")
plt.legend()


# In[13]:


Conclusion -Both are the same


# In[ ]:


# Task 2 - Find as per gender who has not normal platelets level in blood


# In[23]:


#Filter by platelets(condition lesser then 150000 OR greater then 450000) and create new dataframe
platelets=df.loc[(df['platelets']<15000)|(df['platelets']>45000)]
platelets


# In[29]:


#On this new dataframe perform group operation as per gender and create new dataframe 
groupby_gender=platelets.groupby('gender')['platelets'].count().reset_index()
groupby_gender



# In[30]:


#Plot a pie chart as per the gender to show the percentage of male and female who has not normal platelets
value=groupby_gender['platelets']
label=groupby_gender['gender']
plt.pie(value,labels=label,autopct="%0.1f%%",radius=2)
plt.show()


# 

# In[ ]:





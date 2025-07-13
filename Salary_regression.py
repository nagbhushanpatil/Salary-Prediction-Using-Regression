#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import required libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Step 2: Load dataset
df = pd.read_csv("salary_dataset.csv")
df.head()


# In[2]:


# Step 3: Run multivariate regression

# Define independent and dependent variables
X = df[['YearsExperience', 'EducationLevel', 'PerformanceRating', 'Location']]
y = df['Salary']

# Convert categorical variables into dummy/indicator variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Add a constant (intercept) to the model
X_encoded = sm.add_constant(X_encoded)

# Fit OLS regression model
model = sm.OLS(y, X_encoded).fit()

# Display the full regression summary
model.summary()


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.regplot(data=df, x='YearsExperience', y='Salary')
plt.title('Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[4]:


df.groupby('EducationLevel')['Salary'].mean().sort_values().plot(kind='bar')
plt.title('Average Salary by Education Level')
plt.ylabel('Salary')
plt.xlabel('Education Level')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





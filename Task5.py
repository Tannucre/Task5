Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df=pd.read_csv('C:\\Users\\Pc\\Desktop\\tannu\\heart.csv')  #import the dataset
... 
>>> df.head()  #checking first five rows by calling df.head()
   age  sex  cp  trestbps  chol  fbs  ...  exang  oldpeak  slope  ca  thal  target
0   52    1   0       125   212    0  ...      0      1.0      2   2     3       0
1   53    1   0       140   203    1  ...      1      3.1      0   0     3       0
2   70    1   0       145   174    0  ...      1      2.6      0   0     3       0
3   61    1   0       148   203    0  ...      0      0.0      2   1     3       0
4   62    0   0       138   294    1  ...      0      1.9      1   3     2       0

[5 rows x 14 columns]
>>> df.tail()   #checking last five rows by calling df.tail()
      age  sex  cp  trestbps  chol  ...  oldpeak  slope  ca  thal  target
1020   59    1   1       140   221  ...      0.0      2   0     2       1
1021   60    1   0       125   258  ...      2.8      1   1     3       0
1022   47    1   0       110   275  ...      1.0      1   1     2       0
1023   50    0   0       110   254  ...      0.0      2   0     2       1
1024   54    1   0       120   188  ...      1.4      1   1     3       0

[5 rows x 14 columns]
>>> df.columns         #take a look at the column names(by indexing)
Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
      dtype='object')
>>> df.columns.values   #take a look at the column names(array form)
array(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
       'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
      dtype=object)
>>> df.isna().sum() #checking for null values
age         0
sex         0
cp          0
trestbps    0
chol        0
fbs         0
restecg     0
thalach     0
exang       0
oldpeak     0
slope       0
ca          0
thal        0
target      0
dtype: int64
df.info()  #concise thee summary of the datasheet
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1025 entries, 0 to 1024
Data columns (total 14 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1025 non-null   int64  
 1   sex       1025 non-null   int64  
 2   cp        1025 non-null   int64  
 3   trestbps  1025 non-null   int64  
 4   chol      1025 non-null   int64  
 5   fbs       1025 non-null   int64  
 6   restecg   1025 non-null   int64  
 7   thalach   1025 non-null   int64  
 8   exang     1025 non-null   int64  
 9   oldpeak   1025 non-null   float64
 10  slope     1025 non-null   int64  
 11  ca        1025 non-null   int64  
 12  thal      1025 non-null   int64  
 13  target    1025 non-null   int64  
dtypes: float64(1), int64(13)
memory usage: 112.2 KB


#plotting histogram of all the numeric values
df.hist(bins = 50, grid = False, figsize=(20,15))
array([[<AxesSubplot: title={'center': 'age'}>,
        <AxesSubplot: title={'center': 'sex'}>,
        <AxesSubplot: title={'center': 'cp'}>,
        <AxesSubplot: title={'center': 'trestbps'}>],
       [<AxesSubplot: title={'center': 'chol'}>,
        <AxesSubplot: title={'center': 'fbs'}>,
        <AxesSubplot: title={'center': 'restecg'}>,
        <AxesSubplot: title={'center': 'thalach'}>],
       [<AxesSubplot: title={'center': 'exang'}>,
        <AxesSubplot: title={'center': 'oldpeak'}>,
        <AxesSubplot: title={'center': 'slope'}>,
        <AxesSubplot: title={'center': 'ca'}>],
       [<AxesSubplot: title={'center': 'thal'}>,
        <AxesSubplot: title={'center': 'target'}>, <AxesSubplot: >,
        <AxesSubplot: >]], dtype=object)
plt.show()


#descriptive statistics
df.describe()
               age          sex  ...         thal       target
count  1025.000000  1025.000000  ...  1025.000000  1025.000000
mean     54.434146     0.695610  ...     2.323902     0.513171
std       9.072290     0.460373  ...     0.620660     0.500070
min      29.000000     0.000000  ...     0.000000     0.000000
25%      48.000000     0.000000  ...     2.000000     0.000000
50%      56.000000     1.000000  ...     2.000000     1.000000
75%      61.000000     1.000000  ...     3.000000     1.000000
max      77.000000     1.000000  ...     3.000000     1.000000

[8 rows x 14 columns]
questions=["1. Hw many people have heart disease and how many people doesn't have heart disease?",
           "2. People of which sex has most heart disease?",
           "3. People of which sex has has which type of chest pain?",
           "4. People with which chest pain are most prone to have a heart disease?"]
print(questions)
["1. Hw many people have heart disease and how many people doesn't have heart disease?", '2. People of which sex has most heart disease?', '3. People of which sex has has which type of chest pain?', '4. People with which chest pain are most prone to have a heart disease?']


#Let's find out the answer of question 1
df.target.value_counts()
1    526
0    499
Name: target, dtype: int64
#plotting bar chart
df.target.value_counts().plot(kind = 'bar' , color = ['orchid','salmon'])
<AxesSubplot: >
plt.title("Heart Disease Values")
Text(0.5, 1.0, 'Heart Disease Values')
plt.xlabel("1 = Heart Disease, 0 = No Heart Disease")
Text(0.5, 0, '1 = Heart Disease, 0 = No Heart Disease')
plt.ylabel("Amount")
Text(0, 0.5, 'Amount')
plt.show()
#plotting pie chart
df.target.value_counts().plot(kind = 'pie' , figsize = (8,6))
<AxesSubplot: ylabel='target'>
plt.legend(["Disease", "No Disease"])
<matplotlib.legend.Legend object at 0x000001A0199130D0>
plt.show()


#'0' represent 'Male'
#'1' represent 'Female'
#'0' represent 'No disease'
#'1' represent 'Disease'
#Let's check how many "Male" and "Female" are in the dataset
df.sex.value_counts()
1    713
0    312
Name: sex, dtype: int64
#plotting a pie chart
df.sex.value_counts().plot(kind = 'pie', figsize= (8,6))
<AxesSubplot: ylabel='sex'>
plt.title('Male Female Ratio')
Text(0.5, 1.0, 'Male Female Ratio')
plt.legend(['Male','Female'])
<matplotlib.legend.Legend object at 0x000001A01995A110>
plt.show()


#Lets find out the answer of 2nd question
#2. People of which sex has most heart disease?
pd.crosstab(df.target, df.sex)
sex       0    1
target          
0        86  413
1       226  300
sns.countplot(x = 'target', data = df, hue = 'sex')
<AxesSubplot: xlabel='target', ylabel='count'>
plt.title('Heart disease frequency for sex')
Text(0.5, 1.0, 'Heart disease frequency for sex')
plt.xlabel('0 = No Heart Disease, 1 = Heart Disease')
Text(0.5, 0, '0 = No Heart Disease, 1 = Heart Disease')
plt.show()


#Let's find out the answer of the qusetion 3
#3. People of which sex has has which type of chest pain?
df.cp.value_counts()
0    497
2    284
1    167
3     77
Name: cp, dtype: int64
#plotting a bar chart
df.cp.value_counts().plot(kind = 'bar', color = ['salmon', 'lightskyblue', 'red', 'khaki'])
<AxesSubplot: >
plt.title('Chest pain type vs Count')
Text(0.5, 1.0, 'Chest pain type vs Count')
plt.show()


#Find the types of chest pain
pd.crosstab(df.sex, df.cp)
cp     0    1    2   3
sex                   
0    133   57  109  13
1    364  110  175  64
pd.crosstab(df.sex, df.cp).plot(kind = 'bar', color = ['coral' , 'lightskyblue', 'plum', 'khaki'])
<AxesSubplot: xlabel='sex'>
plt.title('Types of chest pain for sex')
Text(0.5, 1.0, 'Types of chest pain for sex')
plt.xlabel('0 = Female ,1 = Male')
Text(0.5, 0, '0 = Female ,1 = Male')
plt.show()


#Most of 'Male' has 'type 0' chest pain and least of 'Male' has 'type 4' pain.          
#in case of 'Female' 'type 0' and 'type 2' percentage is almost same          
#find question 4
#4. People with which chest pain are most prone to have a heart disease?
pd.crosstab(df.cp, df.target)
target    0    1
cp              
0       375  122
1        33  134
2        65  219
3        26   51
sns.countplot(x = 'cp', data = df, hue = 'target')
<AxesSubplot: xlabel='cp', ylabel='count'>
plt.show()


#Most of the people have 'type 0' of chest pain has less chance of heart disease#And we see the opposite for other types           
#Now let's take look at our age column           
#Create a distribution plot with normal distribution curve
sns.displot(x = 'age', data = df, bins = 14, kde = True)
<seaborn.axisgrid.FacetGrid object at 0x000001A01CE97760>
plt.show()
#Let's plot another distribution plot for maximize heart rate
sns.displot(x = 'thalach' , data = df, bins = 20, kde = True, color = 'chocolate')
<seaborn.axisgrid.FacetGrid object at 0x000001A01A732B30>
plt.show()


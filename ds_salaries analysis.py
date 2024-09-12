import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:\\Users\\x\\python files\\ds_salaries.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)
print(data.dtypes)
data.drop_duplicates(inplace=True)
print(data.iloc[0])
print(data.isna().sum())
remote_salaries=data.copy()
remote_salaries=remote_salaries.groupby('remote_ratio')['salary_in_usd'].mean()
print(remote_salaries)
plt.figure()
remote_salaries.plot(kind='bar')
plt.show()

print(data['experience_level'].value_counts())
data['experience_level']=data['experience_level'].map(
            {'SE':'senior','MI':'mid','EN':'entry level','EX':'executive'})

experience_salaries=data.copy().groupby('experience_level'
                                        )['salary_in_usd'].mean()

plt.figure()
experience_salaries.sort_values().plot(kind='bar')
plt.show()

country_salaries=data.copy().groupby(['company_location']
                                     )['salary_in_usd'].mean()

grouped_titles=data.copy()
grouped_titles['job_title']=[
    'Data Scientist'  if 'Data Scientist' in j or 'Data Science' in j else
    'Data Engineer' if 'Data Engineer' in j else
    'Data Analyst' if 'Data Analyst' in j else
    'ML Specialist' if 'Machine Learning' in j or 'ML' in j
    else j for j in data['job_title']]
print(grouped_titles['job_title'].value_counts())

cj=list(grouped_titles['job_title'].value_counts().head(10).index)
common_jobs=grouped_titles[grouped_titles['job_title'].isin(cj)]
plt.figure()
common_jobs.groupby('job_title')['salary_in_usd'].mean().plot(kind='bar')
plt.show()
abroad=data.copy()
abroad['abroad']=['local' if data.loc[i]['employee_residence']==data.loc[i]['company_location'] else 'abroad' for i in data.index]
abroad['abroad']
plt.figure()
abroad.groupby('abroad')['salary_in_usd'].mean().plot(kind='bar')
plt.show()
























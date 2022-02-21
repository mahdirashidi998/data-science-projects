import pandas as pd



yearly = pd.read_csv('04-Dr. Semmelweis and the Discovery of Handwashing\yearly_deaths_by_clinic.csv.csv')#reading from a scv file
yearly['proportion_deaths'] = [i/j for i, j in zip(yearly['deaths'],yearly['births'])] # adding a column with all datas due to yearly itself
clinic_1 = yearly[yearly['clinic']=='clinic 1'] #separating clinic 1 from 2
clinic_2 = yearly[yearly['clinic']=='clinic 2']
print(yearly)
# Plot yearly proportion of deaths at the two clinics, error due to library problem with python 3.10
#ax = clinic_1.plot(x = 'year', y = 'proportion_deaths',label = 'clinic 1')
#clinic_2.plot(x = 'year', y = 'proportion_deaths',label = 'clinic 2', ax=ax, ylabel ="Proportion deaths" )
monthly = pd.read_csv('04-Dr. Semmelweis and the Discovery of Handwashing\monthly_deaths.csv',parse_dates = ['date']) #read new files
monthly['proportion_deaths'] = [i/j for i, j in zip(monthly['deaths'],monthly['births'])] #adding a column to monthly
print(monthly.head(n=1)) # printing first line 
#ax = monthly.plot(x='date', y = 'proportion_deaths',ylabel='Proportion deaths')
# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly['date'] < '1847-06-01']
after_washing = monthly[monthly['date'] >= '1847-06-01']

# Plot monthly proportion of deaths before and after handwashing
ax = before_washing.plot(x = 'date', y = 'proportion_deaths', label = 'before washing',ylabel = 'proportion deaths')
after_washing.plot(x = 'date', y = 'proportion_deaths', label = 'before washing',ylabel = 'proportion deaths',ax = ax)
# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_diff = after_proportion.mean() - before_proportion.mean()

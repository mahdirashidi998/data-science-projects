import datetime
import os

def  createNDaysList(N) :  #returns list of N objects of date
    dates = []
    for i in range(N) :
        dates.append(datetime.date.today()+datetime.timedelta(days=i))
    return dates

def  CSVsNDays(N): #creates month directory, in each week directories and in each of then day csv files
    i = 0
    j = 0
    x = 0

    hours = ''
    for k in range(24) :
        hours = hours + str(k) + ','
    dates = createNDaysList(N) 
    while x < N : #creates directories of year
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}'.format(year = dates[x].year))     
        except :
            pass
 #creates directories of month
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}'.format(year =dates[x].year, month = dates[x].month))
        except :
            pass
#creates directories of week
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}\{week}'.format(year =dates[x].year, month = dates[x].month, week = dates[x].isocalendar().week))
        except :
            pass
#creates csv files in appropriate directory
        f = open('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}\{week}\{day}.csv'.format(year =dates[x].year, month = dates[x].month, week = dates[x].isocalendar().week, day = dates[x].day ),'w')
        f.write(dates[x].isoformat() + ',')
        f.write(hours)
        f.close()
        x = x +1

CSVsNDays(100)



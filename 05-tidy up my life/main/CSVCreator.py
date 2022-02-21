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
    while x <= N : #creates directories of year
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}'.format(year = dates[x].year))
            x = x + 365 
        except :
            continue
    while j <= N : #creates directories of month
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}'.format(year =dates[j].year, month = dates[j].month))
            j = j + 28 
        except :
            continue
    while i <= N :#creates directories of week
        try : 
            os.mkdir('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}\{week}'.format(year =dates[i].year, month = dates[i].month, week = dates[i].isocalendar().week))
            i = i + 7
        except :
            continue
    for d in dates : #creates csv files in appropriate directory
        try :
            f = open('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}\{week}\{day}.csv'.format(year = d.year, month = d.month, week = d.isocalendar().week, day = d.day),'w')
            f.write(d.isoformat() + ',')
            f.write(hours)
            f.close()
        except :
            f = open('G:\My Drive\jahad\purposes\\find_job\data science projects\\05-tidy up my life\CSVs\{year}\{month}\{week}\{day}.csv'.format(year = d.year, month = d.month-1, week = d.isocalendar().week, day = d.day),'w')
            f.write(d.isoformat() + ',')
            f.write(hours)
            f.close()
CSVsNDays(100)



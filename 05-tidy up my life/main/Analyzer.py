import objectOrientor
import datetime

#presets
#calendar Id can be found in google calendar settings of your calendar.change this to yours
objectOrientor.calInterface.CALENDARID = 'ud47hcdqh6r9quhqigs2td1t8o@group.calendar.google.com'
ENDDATE= datetime.datetime.utcnow() # the date of the last event you want to extract
STARTDATE = ENDDATE - datetime.timedelta(days = 3 ) # the date of the first event you want to extract



Actions = objectOrientor.ActionsDicSaver(STARTDATE,ENDDATE) #actions in appropriate objects ready for you to analize as a dictionary in format {'2022-02-22T00:00:00+01:00': <Action.Sleep object at 0x0000025F29C42410>,}
print(Actions)


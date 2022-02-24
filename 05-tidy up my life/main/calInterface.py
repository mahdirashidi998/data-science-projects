from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



#presets
CALENDARID = 'ud47hcdqh6r9quhqigs2td1t8o@group.calendar.google.com'





# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


"""Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    service = build('calendar', 'v3', credentials=creds)
except HttpError as error:
    print('An error occurred: %s' % error)


def  events(startDate, endDate) :
        ''' gets the events from startDate till endDate in format datetime  
        returns a list of dictionary for each event in this format 
        {'kind': 'calendar#event', 'etag': '"3291247619350000"', 'id': '1o4okqke9htu7pf0ecgfs64pm5', 'status': 'confirmed', 
        'htmlLink': 'https://www.google.com/calendar/event?eid=MW80b2txa2U5aHR1N3BmMGVjZ2ZzNjRwbTUgdWQ0N2hjZHFoNnI5cXVocWlnczJ0ZDF0OG9AZw',
       'created': '2022-02-22T13:41:24.000Z', 'updated': '2022-02-23T13:43:29.675Z', 'summary': 'sleep', 'description': 'kose nanat', 
       'creator': {'email': 'mahdirashidi998@gmail.com'}, 'organizer': {'email': 'ud47hcdqh6r9quhqigs2td1t8o@group.calendar.google.com', 
       'displayName': 'recorder', 'self': True}, 'start': {'dateTime': '2022-02-22T00:00:00+01:00', 'timeZone': 'Europe/Rome'}, 
       'end': {'dateTime': '2022-02-22T08:15:00+01:00', 'timeZone': 'Europe/Rome'}, 'iCalUID': '1o4okqke9htu7pf0ecgfs64pm5@google.com', 
       'sequence': 0, 'reminders': {'useDefault': True}, 'eventType': 'default'}
        '''
        startDate = startDate.isoformat() + 'Z'  # 'Z' indicates UTC time
        endDate = endDate.isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming events')
        events_result = service.events().list(calendarId= CALENDARID, timeMin=startDate,timeMax = endDate, singleEvents=True,orderBy='startTime').execute()
        events = events_result.get('items', [])


        if not events:
            print('No upcoming events found.')
            return


        return events

import datetime

class Action :
    def  __init__(self, event) :
        self.event = event
        self.type = event['summary'].capitalize()
        self.datetime = datetime.datetime.fromisoformat(event['start']['dateTime'])
        self.duration = datetime.datetime.fromisoformat(event['end']['dateTime'])-datetime.datetime.fromisoformat(event['start']['dateTime'])
        
        if('description' in self.event) :
            self.description = event['description']
        else : 
            self.description = None

    def  __str__(self) :
        return self.type

    def  startDateStr(self) :
        '''returns start date in str format'''
        return self.datetime.isoformat()

    def discribe(self) :
        return None
            
class Work(Action) :
    pass

class Study(Work) : 
    pass

class Code(Work) :
    pass

class Sleep(Action) :

    def discribe(self) :
        if (self.datetime.hour >=0 and self.datetime.hour<=12) :#see if the sleep is night sleep or noon sleep
            self.noon = 0
        else : 
            self.noon = 1

    def  isNoonSleep(self):
        #if zero, it is nightsleep if 1 it is noon sleep
        return self.noon
        

class Pray(Action) :
    def discribe(self) :
        self.prayNames = ['morning','noon','evening','night']

        if (self.datetime.hour >=4 and self.datetime.hour<=8) :#calculate pray number, 0 is morning and 3 is the night pray
            self.prayNum = 0
        elif (self.datetime.hour >=11 and self.datetime.hour<=18): 
            self.prayNum = 1
        elif (self.datetime.hour >18 and self.datetime.hour<=24): 
            self.prayNum = 2
        else :
            self.prayNum = 3

    def  whichPray(self) :
        #returns the name of the pray
        return self.prayNames[self.prayNum]

class Eat(Action) :
    def discribe(self) :
        self.mealNames = ['breakfast','lunch','dinner']
        if (self.datetime.hour >=4 and self.datetime.hour<=11) :#calculate pray number, 0 is morning and 3 is the night pray
            self.mealNum = 0
        elif (self.datetime.hour > 11 and self.datetime.hour<=18): 
            self.mealNum = 1
        elif (self.datetime.hour >18 and self.datetime.hour<=24): 
            self.mealNum = 2
    def whichMeal(self) :
        return(self.mealNames[self.mealNum])

class SocialMedia(Action) :
    pass

class Socialize(Action) :
        
    def setPeople(self) :
        try :
            self.people = self.description.split(',')[1:]
        except :
            if(self.description == None) :
                print('no description found  in event {cls}, in date {date}'.format(date = self.startDateStr(),cls = self.type))
            else :  
                print('wrong format in event {cls}, in date {date}'.format(cls = self.type, date = self.startDateStr()))
    def  getPeople(self) :
        return self.people
    def  discribe(self) :
        self.setPeople()

class Educate(Action) :
    def  setSubject(self) :
        try :
            self.subject = self.description
        except :
            if(self.description == None) :
                print('no description found  in event {cls}, in date {date}'.format(date = self.startDateStr(),cls = self.type))
            else :  
                print('wrong format in event {cls}, in date {date}'.format(cls = self.type, date = self.startDateStr()))
    def  getSubject(self) :
        return self.subject
    def  discribe(self) :
        self.setSubject()
class Book(Educate) :
    def  setBookName(self,bookName):
        self.bookName = bookName
    def  getBookName(self) :
        return self.bookName


class Podcast(Educate) :
    def  setPodcastName(self, podcastName) :
        self.podcastName = podcastName
    def  getPodcastName(self) :
        return self.podcastName


class Web(Educate) :
    pass

        





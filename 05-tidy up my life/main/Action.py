from datetime import datetime
#scafolding :
d = datetime.now()

class Action :
    #Action class with date and time both in datetime object 
    def  __init__(self, dateTime) :
        self.datetime = dateTime

class Work(Action) :
    pass

class Study(Work) : 
    pass

class Code(Work) :
    pass

class Sleep(Action) :
    def  __init__(self, dateTime) :
        self.datetime = dateTime

        if (self.datetime.hour >=0 and self.datetime.hour<=12) :#see if the sleep is night sleep or noon sleep
            self.noon = 0
        else : 
            self.noon = 1
    def  isNoonSleep(self):
        #if zero, it is nightsleep if 1 it is noon sleep
        return self.noon
        

class Pray(Action) :
    def  __init__(self, dateTime) :
        self.datetime = dateTime
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
    def  __init__(self, dateTime) :
        self.datetime = dateTime
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
    def setPeople(self, peopleNameList) :
        self.people = peopleNameList
    def  getPeople(self) :
        return self.people

class Educate(Action) :
    def  setSubject(self, subject) :
        self.subject = subject
    def  getSubject(self) :
        return self.subject
    pass
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

        




#scafolding
w = Sleep(d)
print(w.isNoonSleep())

p = Pray(d)
print(p.whichPray())

e = Eat(d)
print(e.whichMeal())

s = Socialize(d)
s.setPeople(['abas','hossein'])
print(s.getPeople())

b = Book(d)
b.setBookName('harryPotter')
print(b.getBookName())

pc = Podcast(d)
pc.setPodcastName('defaAqlani')
print(pc.getPodcastName())
pc.setSubject('din')
print(pc.getSubject())

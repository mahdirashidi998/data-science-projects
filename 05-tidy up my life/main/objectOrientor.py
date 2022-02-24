import calInterface
import datetime
import Action
import pickle
def  ActionsList(startDate,endDate) :
    '''a function which creates our ActionsObjectList by using events extracted from google calendar '''
    startDate = startDate
    endDate = endDate
    events = calInterface.events(startDate,endDate)
    ActionsListf = []
    counter = 0
    for j in events :
        code = 'ActionsListf.append(Action.{cls}({j}))'.format(cls = j['summary'].capitalize(),j = j)
        try :
            exec(code)
        except :
            print('some error happened in creating {cls} object at {date}'.format(cls = j['summary'].capitalize(), date = j['start']['dateTime']))
    return ActionsListf

def  updateActionsDic(startDate, endDate,ActionsDic):
    '''updates but not replaces the tasks already exists, date formats are in datetime format'''
    ActionsListf = ActionsList(startDate, endDate)
    for i in ActionsListf:
        if i.startDateStr() not in ActionsDic :
            ActionsDic[i.startDateStr()] = i
    return ActionsDic
def  redoActionsDic(AstartDate, endDate):
    ActionsListf = ActionsList(startDate, endDate)
    for i in ActionDic :
        if i.datetime > startDate and i.datetime< endDate :
            ActionDic.pop(i.startDateStr())
    for i in ActionsListf :
        ActionDic[i.startDateStr()] = i
    return ActionsDic

def  ActionsDicSaver(startDate, endDate):
    with open('ActionsData.pkl', 'rb') as outp:
        try :
            ActionsDic = pickle.load(outp)
            pickle.PickleError
        except :
            print('an error in loading pickle file')
            ActionsDic = {}

        ActionsDic=updateActionsDic(startDate, endDate, ActionsDic)
    with open('ActionsData.pkl', 'wb') as outp:
        pickle.dump(ActionsDic, outp, pickle.HIGHEST_PROTOCOL)

    return ActionsDic



    

        

    







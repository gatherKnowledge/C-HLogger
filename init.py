import calendar
import datetime
import random

def getRandom(max):
    while True :
        rd = random.random() 
        st = str(rd)
        if int(st[3]) <= max :
            return st[3]
        else :
            continue 
def getIndex() :
    global gIndex
    global gDay
    global gHour 

    if (gDay % 7 == 1) and (gHour == 0) :
        gIndex = 1
    else :
        gIndex =  gIndex + 1
    return gIndex

def getMonth() :
    global gYear, gMonth
    month = gMonth
    if (lastDayOfMonth == gDay) and (is23Hour()) :
        gMonth = gMonth +1 
        if( gMonth == 13 ) : 
            gMonth = 1
            gYear += 1
    return month 

def getDay() :
    global gDay
    lDay = gDay 
    if (is23Hour()) :
        gDay = gDay + 1
        if ( lDay == lastDayOfMonth) :
             gDay = 1
    return lDay 

def getHour() :
    global gHour 
    lHour = gHour
    if is23Hour() :
        gHour = 0 
    else :
        gHour = gHour + 1

    return lHour

def is23Hour():
    if gHour == 23 :
        return True
    else : 
        return False

    
def getLine() :
    line = '' 
    lineIndex = getIndex()
    lineMonthInt = getMonth()
    lineMonth = str(lineMonthInt)
    
    if len(lineMonth) < 2:
        lineMonth = '0'+lineMonth 
    lineDay = str(getDay())
    if len(lineDay) < 2:
        lineDay = '0'+lineDay 
    
    lineDate = str(gYear) +'.' + lineMonth + '.' + str(lineDay)

    # 프로그램 종료 ( 다음 달 1일의 10시 시점)
    if (gHour == 10) and (gToday.month != lineMonthInt):
        return False 
    lineTime = str(getHour()) + ':00:00'
    
    #온도
    lineCel = str(2) + str(getRandom(4)) + '.' + str(getRandom(9))
    # 습도
    lineHumid = str(4) + str(getRandom(4)) + '.' + str(getRandom(9))

    lineString = str(lineIndex) +'. '+ lineDate +' '+ lineTime + ' '+ lineCel + ' ' + lineHumid 
    return lineString
    
def init(f) :
    while(True) :
        result = getLine()
        if not result :
            f.close()
            return 
        else :
            f.write(result+'\n')

def makeFile():
    f = open("data1.txt", "w")
    return f 


# globals
gToday = datetime.date.today()
# gToday = datetime.datetime(2018, 12, 1, 12, 30, 59, 0)

gIndex = 0
gYear = gToday.year
gMonth = gToday.month
gDay = 1
gHour = 10

lastDayOfMonth = calendar.mdays[gMonth]
beforeCel = 0 
beforeHumid = 0
line = '' 

f = makeFile()
init(f)



# print(lastDayofMonth)
# formatedToday = pToday.strftime("%Y.%m.%d")
# print(formatedToday)


# Check for and adjust month input if necessary
def validateMonth(month):
    if(month > 12 or month < 1):
        month = 1
    return month

# Check for and adjust day input if necessary
# (don't forget about leap year)
def validateDay(month, day, year):
    leap = 0
    if(year % 4 == 0):
        leap = 1
    if(year % 100 == 0 and year % 400 != 0):
        leap = 0

    if(day < 1 or day > 31):
        day = 1

    if(month == 4 or month == 6 or month == 9 or month == 11):
        if(day > 30):
            day = 1

    if(month == 2):
        if (leap == 1 and day > 29):
            day = 1
        if(leap == 0 and day > 28):
            day = 1
    return day

# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def printEvents():
    months = ["January","February","March","April","May","June","July", "August","September","October","November","December"]
    print("******************** List of Events ********************")
    for i in range(len(eventName)):
        print(eventName[i])
        print("Date: " + str(months[eventMonth[i]-1]) + " " + str(eventDay[i]) + ", " + str(eventYear[i]))


# This function is used to prompt, adjust and
# append values to the 4 parallel arrays
# Prompt the user for the event details
def addEvent():
    addName = input("What is the event: ")
    addMonth = int(input("What is the month (number): "))
    addDay = int(input("What is the date: "))
    addYear = int(input("What is the year: "))
    addMonth = validateMonth(addMonth)
    addDay = validateDay(addMonth, addDay, addYear)
    
    eventName.append(addName)
    eventMonth.append(addMonth)
    eventDay.append(addDay)
    eventYear.append(addYear)

#*********** MAIN **********
eventName = []
eventMonth = []
eventDay = []
eventYear = []

addEvent()
cont = input("Do you want to enter another date? NO to stop: ")
while(cont != "NO"):
    addEvent()
    cont = input("Do you want to enter another date? NO to stop: ")

printEvents()

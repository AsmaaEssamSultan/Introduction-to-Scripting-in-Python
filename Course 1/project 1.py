""""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """


    date1 = datetime.date(year,month,1)   #save the date of the given year and month

    #save the date of the given year and the next month
    if month == 12 :
        date2 = datetime.date(year+1,1,1)
    else:
        date2 = datetime.date(year,month+1,1)

    difference = date2 - date1  #cal the difference between the dates
    return difference.days        #return the number of days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise

    """

    #Check the vaild of the given date
    if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and ( 1 <= month <= 12)):
        if 1 <= day <= days_in_month(year, month):
            return True
        else:
            return False
    else:
        return False



def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    #Check the vaild of the given date 1
    if is_valid_date(year1, month1, day1):
        date1 = datetime.date(year1, month1, day1)
    else:
        return 0

    #Check the vaild of the given date 2
    if is_valid_date(year2, month2, day2):
        date2 = datetime.date(year2, month2, day2)
    else:
        return 0

    #Check that the date 2 ix more than date 1
    if date2 >= date1:
        difference = date2 - date1
        return difference.days
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """

    date_today = datetime.date.today()  #save the date of today
    year2 = date_today.year   #save the year of today date
    month2 = date_today.month  #save the month of today date
    day2 = date_today.day  #save the day of today date

    #check the vaild of the given date
    if is_valid_date(year, month, day) :
        date_brith = datetime.date(year, month, day)
    else:
        return 0

    #check that the today date more than or equal the given date
    if  date_today >= date_brith :
        return days_between(year, month, day, year2, month2, day2)
    else:
        return 0


#print("This program is design to calcuate your ages in days")
#year = int(input("Enter the year when you are brith: "))
#month = int(input("Enter the month when you are brith: "))
#day = int(input("Enter the day when you are brith: "))
#print(age_in_days(year, month, day))

import datetime
from dateutil import parser


def compare_dates(given_date):
    """" 
    Returns True if given date is greater the todays date
    otherwise return false provided date will be of following format:
    """

    today = datetime.datetime.today()

    today_year = today.year
    today_month = today.month
    today_day = today.day

    date_format = given_date.strip()

    
    if len(date_format) is 4:
        return True if today_year <= int(date_format) else False
        

    elif len(date_format) > 4:

        check = parser.parse(date_format)
        return True if today <= check else False
      
    else: 
        return False   


def dateFormatter(date):
    date.strip()

    if len(date) is 4:
        string = "The next season begins in {}".format(date)

    elif  len(date.split()) is 3: 
        formatted_date = parser.parse(date).strftime("%Y-%m-%d")

        return "The next episode airs on {}".format(formatted_date)

    else:
        return "The next episode airs on {}".format(date)

           




    
if __name__ == "__main__":
   
    test = [" 31 Oct. 2018 ", "2018 ", "2019 ", "Oct. 2018", "2 May 2017", "12 Oct 2018"]
    
    for t in test:
        print(compare_dates(t))

from UserInput import *
import fringe
from emailing import *
from database import *
import config

def main():
    
    user_email = input("Email address: ")
    user_series = input("TV Series: ")

    user = UserDetails(user_email,user_series)
    message = ''

    database = DatabaseEntry(config.DB_USERNAME,config.DB_PASSWORD,"testing")
    database.createTable("versionbeta")
    database.insertInto("versionbeta",user_email,user_series)

    for series in user.getSeries():
        next_date = fringe.getNextEpisodeDate(series)
        message += emailFormatter(series,next_date)

    email = Emailer(user.getEmail(),message)
    email.emailThis()



if __name__ == "__main__":
    main()
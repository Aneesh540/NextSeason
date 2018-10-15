from UserInput import *
import fringe
from emailing import *

def main():
    
    user_email = input("Email address: ")
    user_series = input("TV Series: ")

    user = UserDetails(user_email,user_series)
    message = ''

    for series in user.getSeries():
        next_date = fringe.getNextEpisodeDate(series)
        # print(next_date)

        message += emailFormatter(series,next_date)

    print(user.getEmail())
    print(message)
    email = Emailer(user.getEmail(),message)
    email.emailThis()



if __name__ == "__main__":
    main()
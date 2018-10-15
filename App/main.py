from UserInput import *


def main():
    
    user_email = input("Email address: ")
    user_series = input("TV Series: ")

    user = UserDetails(user_email,user_series)
    message = ''

    for series in user.getSeries():
        next_date = getNextEpisodeDate(series)

        message += emailFormatter(series,next_date)

    
    email = Emailer(user.getEmail(),message)
    email.emailThis()



if __name__ == "__main__":
    main()
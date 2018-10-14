from UserInput import *


def main():
    user_email = input("Email address: ")
    user_series = input("TV Series: ")

    user = UserDetails(user_email,user_series)
    datebase(user)

    for i in user.getSeries():
        x = getDates(i)

        (x, date)





    

    

if __name__ == "__main__":
    main()
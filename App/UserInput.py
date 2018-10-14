class UserDetails:

    def __init__(self,email,tvseries):
        self.email = email.strip()
        self.tvseries = [ x.strip() for x in tvseries.split(',')]

    def getEmail(self):
        return self.email


    def getSeries(self):   
        return self.tvseries
    


if __name__ == "__main__":
    x = UserDetail("aneesh@wer.com"," Got, Breaking bad, Naruto , One Piece   ")
    print(x.getEmail())
    print(x.getSeries())     
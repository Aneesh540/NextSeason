from smtplib import SMTP
import config 

def emailFormatter(tvseries,date):

    string = "\nTv series name: {0}\nStatus: {1}\n".format(tvseries,date)
    return string

class Emailer:

    def __init__(self,receiver,message):

        self.receiver = receiver
        self.message = message
        self.sender = config.SENDER 

    def getMessage(self):
        return self.message

    def getReceiver(self):
        return self.receiver

    def getSender(self):
        return self.sender

    def emailThis(self):   
        
        mail = SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(self.sender,config.PASSWORD)
        mail.sendmail(self.sender,self.receiver,self.message)
        mail.close()    
    
            


            



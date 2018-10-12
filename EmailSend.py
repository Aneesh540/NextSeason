import smtplib
import config

content = 'Hello worlds'
mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()
mail.starttls()
mail.login(config.EMAIL,config.PASSWORD)
  
mail.sendmail('aneeshjain203@gmail.com','16ucs036@lnmiit.ac.in',content)
mail.close()
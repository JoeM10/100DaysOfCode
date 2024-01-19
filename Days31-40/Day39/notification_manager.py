import smtplib
import os

#This class is responsible for sending notifications with the deal flight details.

class NotificationManager:

  def __init__(self):
    

    self.APP_PASSWORD = str(os.environ.get("GMAIL_1_APP_PASSWORD"))
    self.PORT_NUMBER = 587

    self.gmail = "smtp.gmail.com"
    self.fromEmail = "johnerr370@gmail.com"
    self.toEmail = "garrhj2464@outlook.com"
  
  def sendEmail(self, city:str, iata:str, price:int, flightSearchData):
    departure = flightSearchData[f"{iata}_departure"]
    arrival = flightSearchData[f"{iata}_arrival"]
    with smtplib.SMTP(self.gmail, port=self.PORT_NUMBER) as connection:
      connection.starttls()
      connection.login(user=self.fromEmail, password=self.APP_PASSWORD)
      connection.sendmail(from_addr=self.fromEmail, to_addrs=self.toEmail, 
                          msg=f"Low Flight Price Alert!!!\n\n\
                            Only ${price} to fly to {city}/{iata} from {departure} - {arrival}, has beat your previous low price!")
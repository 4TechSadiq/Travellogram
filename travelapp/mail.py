import smtplib

USER = "sadiqcp2023@gmail.com"
PASSWORD = "uajknfahhmfhisri"

def send_mail(mail:str, msg: str, name:str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=USER, msg=f"Subject:Travellogram\n\n Message: Sender Name:{name} Sender Mail: {mail} {msg}")
        
        return True
    
# send_mail("sadikcp2014@gmail.com","hello")
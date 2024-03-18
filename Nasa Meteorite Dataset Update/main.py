import requests
from bs4 import BeautifulSoup
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_addr, from_addr, password):

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))
    
 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()
    server.login(from_addr, password)
    server.send_message(msg)
    server.quit()

def fetch_last_update_date(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        last_update_str = "Votre sélecteur spécifique ici" 
       
        last_update_date = datetime.datetime.strptime(last_update_str, "%Y-%m-%d")
        
        return last_update_date
    else:
        print("Échec de la récupération de la page")
        return None
        
        
def main():
    from_addr = ""
    to_addr = ""
    email_password = ""
    
    
    url = "https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data"
    last_known_update = datetime.datetime.now()  
    
    while True:
        current_update = fetch_last_update_date(url)
        
        if current_update and current_update > last_known_update:
            print(f"La page a été mise à jour le {current_update.strftime('%Y-%m-%d %H:%M:%S')}")
            last_known_update = current_update
            
           
            subject = "Notification de mise à jour de la page"
            message = f"La page que vous surveillez a été mise à jour le {current_update.strftime('%Y-%m-%d %H:%M:%S')}."
            send_email(subject, message, to_addr, from_addr, email_password)
        
        time.sleep(3600)  

if __name__ == "__main__":
    main()

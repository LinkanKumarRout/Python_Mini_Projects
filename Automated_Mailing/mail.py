import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "Enter Senders Mail ID"

data = pd.read_csv("your file.csv") # Enter path of csv file containing email address
to_address = data['email'].to_list() # change 'email' column values to a list
names = data['name'].tolist() # change 'name' column values to a list

length = len(names)
email = "Your Email ID"
password = "Your mail ID Password"

for i in range(length):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address[i]
    msg['Subject'] = "Enter the Subject of Mail"
    body = f"Dear {names[i]}," + "\nEnter body of the mail"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address[i], text)
    server.quit()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "srinivasarao.sunnam29@gmail.com"
APP_PASSWORD = "lszd zhuu hptb atrd"

def send_email(news_content):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = "Your Daily News Brief 🗞️"

    msg.attach(MIMEText(news_content, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")

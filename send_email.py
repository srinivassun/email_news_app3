import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "srinivasarao.sunnam29@gmail.com"
    password = "lszd zhuu hptb atrd"


    receiver = "srinivasarao.sunnam29@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        #server.send_message(message)
        

#send_email("Hello, how are you?")

import smtplib

myEmail = "100daysofcodetesty@gmail.com"
password = "oqrynodvwlskiyow"
# oqry nodv wlsk iyow

# 'with' method means we dont have to close the connection once we are done
with smtplib.SMTP("smtp.gmail.com", 587) as connection: # create connection to server
    connection.starttls() # ensures that message is encrypted and connection is secure
    connection.login(user=myEmail, password=password)
    connection.sendmail(from_addr=myEmail, to_addrs="daysofcode100test@yahoo.com",
                        msg="Subject: Hello\n\nThis is the body of my email")


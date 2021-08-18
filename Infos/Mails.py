import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
# ACHTUNG: Vorher Einstellungen ändern: Run > Edit Configurations > Emulate terminal in output console > Apply
password = getpass.getpass('Please enter your password: ')
sender_email = "sender.fuer.alle@gmail.com"
receiver_email = "hernsteincoders@gmail.com"
message = """\
Subject: Hi there!

Greetings."""

# Send email here

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sender.fuer.alle@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)


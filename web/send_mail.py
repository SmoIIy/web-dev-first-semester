import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##############################
def send_verify_email(to_email):
    try:
        # Create a gmail fullflaskdemomail
        # Enable (turn on) 2 step verification/factor in the google account manager
        # Visit: https://myaccount.google.com/apppasswords
        # Copy the key : pdru ctfd jdhk xxci

        # Email and password of the sender's Gmail account
        sender_email = "janustest21@gmail.com"
        password = "nzja uqak lifq lkgc"  # If 2FA is on, use an App Password instead

        # Receiver email address
        receiver_email = to_email
        
        # Create the email message
        message = MIMEMultipart()
        message["From"] = "My company name"
        message["To"] = receiver_email
        message["Subject"] = "Test email | Please verify your account"

        # Body of the email
        body = f"""Well Done - Signup Successful"""
        message.attach(MIMEText(body, "html"))

        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

        return "email sent"
       
    except Exception as ex:
        pass
    finally:
        pass
import smtplib
import pandas as pd 
from email.message import EmailMessage

EMAIL = "surajp7275@gmail.com"
PASSWORD = "lata bdxi ooyr robc"

# READ CSV
data = pd.read_csv("data.csv")  

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

for i in range(len(data)):
    name = data.loc[i, "name"]
    to_email = data.loc[i, "email"]
    message_text = data.loc[i, "message"]
    attachment = data.loc[i, "attachment"]

    msg = EmailMessage()
    msg["Subject"] = "Internship Offer"
    msg['From'] = EMAIL
    msg['To'] = to_email

    msg.set_content(f"Hello {name}, \n\n{message_text}\n\nRegards,\nCompany")

    try:
        with open(attachment, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        server.send_message(msg)
        print(f"Email sent to {to_email}")
        data.loc[i, "status"] = "Sent"

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        data.loc[i, "status"] = "Failed"

data.to_csv("data.csv", index=False)
server.quit()
"""
import smtplib
import imaplib
import email
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration parameters
sender_email = "sender@example.com"
sender_password = "password"
recipient_email = "recipient@example.com"
smtp_server = "smtp.example.com"
imap_server = "imap.example.com"
keyword = "phishing"
attachment_file_path = "/path/to/attachment/file"

# Send an email with an attachment
def send_email():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Test Email with Attachment"
    with open(/jagaban/antenna.pdf, "rb") as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % attachment_file_path)
        msg.attach(p)
    text = msg.as_string()
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

# Check for emails with a specific keyword in the subject line
def check_email():
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(sender_email, sender_password)
    mail.select('inbox')
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    for i in reversed(id_list):
        typ, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg['subject']
                if re.search(keyword, subject):
                    print(f"Found an email with the keyword '{keyword}' in the subject line.")
                    print(f"Subject: {subject}")
                    print(f"Sender: {msg['from']}")
                    print(f"Date: {msg['date']}")
                    for part in msg.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get_content_maintype() == 'text':
                            body = part.get_payload(decode=True).decode()
                            print(f"Message body: {body}")
                        elif part.get_content_maintype() == 'application':
                            filename = part.get_filename()
                            attachment = part.get_payload(decode=True)
                            with open(filename, "wb") as f:
                                f.write(attachment)
    mail.close()
    mail.logout()

# Main function
if __name__ == '__main__':
    send_email()
    check_email()
"""

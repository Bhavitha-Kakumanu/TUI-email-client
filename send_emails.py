import smtplib
from string import Template
from email.message import EmailMessage
from email.headerregistry import Address

MY_ADDRESS = ''
PASSWORD = ''

def recipient_list():
 email_list = []
 with open('email_recipient.txt', 'r') as f:
   to_name, to_email = f.readline().split()
   username, domain = to_email.split('@')
   addr = Address(display_name=to_name, username=username, domain=domain)
   email_list.append(addr)
 return email_list

def get_template():
 with open('email_template.txt', 'r') as f:
   email_template = f.read()
 return Template(email_template)

def setup_smtp():
 s = smtplib.SMTP('smtp.gmail.com', port=587)
 s.starttls()
 s.login(MY_ADDRESS, PASSWORD)
 return s

def main():
 s = setup_smtp()
 for email_addr in recipient_list():
    msg = EmailMessage()
    msg['Subject'] = 'Birthday invitation!!!'
    msg['From'] = 'Yasoob <3'
    msg['To'] = email_addr
    msg.set_content(get_template().substitute(name=email_addr.display_name))
    s.send_message(msg)
    print("Message Sent to {}".format(email_addr.display_name))
 s.quit()

if __name__ == '__main__':
  main()
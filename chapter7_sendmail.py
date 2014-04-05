import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

# ----------------------------------------------------------
def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    headers = {} if headers is None else headers
    
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()
        
# ----------------------------------------------------------
class MailingList:
    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        return {e for (e,g) in self.email_map.items() if g & groups} 

    def send_mailing(self, subject, message, from_addr, *groups, **kwargs):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, **kwargs)

if __name__=='__main__':
    m = MailingList()
    m.add_to_group("friend1@example.com", "friends")
    m.add_to_group("friend2@example.com", "friends")
    m.add_to_group("family1@example.com", "family")
    m.add_to_group("pro1@example.com", "professional")

    m.send_mailing("A Party", "Friends and family only: a party",
                   "me@example.com", "friends", "family",
                   headers={"Reply-To": "me2@example.com"})
    

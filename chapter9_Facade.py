#python -m smtpd -n -c DebuggingServer localhost:1025
import smtplib
import imaplib

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not "@" in self.username:
            from_email = "{0}@{1}".format(self.username, self.host)
        else:
            from_email = self.username
        message = ("From: {0}\r\n"
                   "To: {1}\r\n"
                   "Subject: {2}\r\n\r\n{3}").format(
                       from_email,
                       to_email,
                       subject,
                       message)
        smtp = smtplib.SMTP(self.host, 1025)
        #smtp.login(self.username, self.password)
        smtp.sendmail(from_email, to_email, message)

    #now we are testing with DebuggingServer without username + password
    #inbox will not work (just an example of Facade Pattern)
    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(
            bytes(self.username, 'utf8'),
            bytes(self.password, 'utf8'))
        mailbox.select()
        x,data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split:
            x,message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])
        return messages

if __name__ == '__main__':
    mymail = EmailFacade("localhost", 'me@example.com', None)
    mymail.send_email('local@local.gr', 'The subject', 'The message')
    mymail.get_inbox()
    

from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

API_KEY = ''
SERVER_ID = ''

def read_email(email):
    client = MailosaurClient(API_KEY)
    criteria = SearchCriteria()
    criteria.sent_to = email + "." + SERVER_ID  +"@mailosaur.io"
    message = client.messages.get(SERVER_ID, criteria)
    return message.text.body

if __name__ == '__main__':
    message = read_email("bush-sugar")
    print(message)
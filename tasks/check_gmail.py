from RPA.Email.ImapSmtp import ImapSmtp

gmail_account = "your email"
gmail_password = "your password"
sender = gmail_account

mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)
mail.authorize(account=gmail_account, password=gmail_password)
mail.send_message(
    sender=gmail_account,
    recipients=gmail_account,
    subject="Message from RPA Python",
    body="RPA Python message body",
)

messages = mail.list_messages("SUBJECT RPA")
print(messages[0]['Body'].decode("utf-8"))
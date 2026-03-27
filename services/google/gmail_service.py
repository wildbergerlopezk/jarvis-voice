class GmailService:
    def __init__(self):
        self.service = None

    def get_unread_emails(self):
        return []

    def send_email(self, to, subject, body):
        print(f"📧 Enviando email a {to}")
        return True

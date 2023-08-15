from pathlib import Path
import re
import smtplib, ssl


class SMEmail:
    all = []

    def __init__(self, recipient: str, contents: str):
        assert self.validate_email(recipient), "Recipient email not valid"

        self.__recipient = recipient
        self.__body = contents

        SMEmail.all.append(self)

    @property
    def receipient(self):
        return self.__recipient

    @property
    def body(self):
        return self.__body

    @staticmethod
    def validate_email(email: str):
        email_reg = re.compile(r"^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$")
        if email_reg.match(email):
            return True
        return False

    def __load_cred(self):
        ENV_PATH = Path.cwd().parent / ".env"
        print(ENV_PATH)

    def __connect(self):
        self.__load_cred()
        port = 465  # SSL

    def send_email(self):
        self.__connect()

import re

class Email:
    all = []
    def __init__(self, recipient: str, contents: str):
        assert self.validate_email(recipient), "Recipient email not valid"

        self.__recipient = recipient
        self.__body = contents

        Email.all.append(self)

    @property
    def receipient(self):
        return self.__recipient
    
    @property
    def body(self):
        return self.__body
    
    @staticmethod
    def validate_email(email: str):
        email_reg = re.compile(r'^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$')
        if email_reg.match(email):
            return True
        return False
    
    def __connect(self):
        pass
    
    def send_email(self):
        self.__connect()
from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def receive(Self):
        pass

class Email(Mail):
    def __init__(self, email):
        self.__email = email
    def send(self):
        print(f"{self.__email} Email sent.")
    def receive(self):
        print("Email received.")

class Whatsapp(Mail):
    def __init__(self, Whatsapp_msg):
        self.__Whatsapp_msg = Whatsapp_msg
    def send(self):
        print(f"{self.__Whatsapp_msg} Whatsapp Message sent.")
    def receive(self):
        print("Whatsapp message received.")

class SMS(Mail):
    def __init__(self, sms):
        self.__sms = sms
    def send(self):
        print(f"{self.__sms} SMS sent.")
    def receive(self):
        print("SMS received.")

email_message = input("Enter the email : ")
Whatsapp_message = input("Enter the Whastapp message: ")
sms_message = input("Enyter the sms message: ")

email = Email(email_message)
whatsapp = Whatsapp(Whatsapp_message)
sms = SMS(sms_message)

email.send()
whatsapp.send()
sms.send()

email.receive()
whatsapp.receive()
sms.receive()
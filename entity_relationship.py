import random
import datetime

class Customers:
    def __init__(self, first_name, last_name):
        self.__customer_id = random.randint(111111111, 999999999)
        self.__first_name = first_name
        self.__last_name = last_name      
    def get_customer_id(self):
        return self.__customer_id
    def place_order(self, order_list):
        self.__order_list.append(order_list)
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name 

class Orders:
    def __init__(self, customer_id):
        self.__order_id = random.randint(111111111, 999999999)
        self.__customer_id = customer_id
        self.__order_date = datetime.datetime.now()
    def get_order_details(self):
        return self.__order_id, self.__customer_id, self.__order_date
        
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
customer = Customers(first_name, last_name)

order = Orders(customer.get_customer_id())
order_details = order.get_order_details()
print(f"The order ID is : {order_details[0]}")
print(f"The customer ID is : {order_details[1]}")
print(f"The date and time of order is : {order_details[2]}")

def main():
    # New User

main()

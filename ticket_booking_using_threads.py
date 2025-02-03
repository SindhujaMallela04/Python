import threading
import time

class ticketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()

    def book_ticket(self, name):        
        with self.lock:
            if self.available_tickets >0 :
                time.sleep(1)
                self.availabile_tickets -= 1
                print(f"{name} successfully booked the ticket.")
            else:
                print(f"Sorry {name}, No tickets available.")

ticket = ticketBooking(1)
users = ['Alice', 'Bob', 'Chris', 'Diana']
threads = []
for user in users:
    thread = threading.Thread(target=ticket.book_ticket, args=(user,))
    threads.append(thread)
    thread.start()



# import threading
# import time

# def single_task():
#     print("Task started")
#     time.sleep(2)
#     print("Task completed")

# def another_task():
#     print("ANother task started.")
#     time.sleep(2)
#     print("Another Task Completed.")

# thread = threading.Thread(target=single_task)
# thread1 = threading.Thread(target = another_task)
# thread.start()
# thread1.start()
#thread.join() #Wait for the thread to finish before exiting
# print("Main thread execution completed.")

import threading
import requests

#request is a package that connects to the outside world 

def fetch_url(url, results):
    response = requests.get(url)
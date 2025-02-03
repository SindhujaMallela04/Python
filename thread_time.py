import threading
import time
from datetime import datetime

def show_time():
    while True:
        print(datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)
        

time_thread = threading.Thread(target = show_time, daemon = True)
time_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:    
    print("Main thread exiting.")
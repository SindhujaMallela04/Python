import threading

def process(data):
    print(f"Sum of the list numbers is {sum(data)}")

data_list = [
    list(range(1000000)),
    list(range(2000000)),
    list(range(3000000)),
]

threads = []
for dl in data_list:
    thr = threading.Thread(target = process(dl))
    threads.append(thr)
    thr.start()

for th in threads:
    th.join()









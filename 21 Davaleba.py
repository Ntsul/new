###############
######Task1
###########

import json
import threading

json_data = [
    {"name": "Daviti", "age": 25, "city": "New York"},
    {"name": "Levani", "age": 30, "city": "Los Angeles"},
    {"name": "Tamari", "age": 35, "city": "Chicago"}
]

file_names = ["file1.json", "file2.json", "file3.json"]

for i, data in enumerate(json_data):
    with open(file_names[i], "w") as file:
        json.dump(data, file)

def parse_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        print(f"Data from {file_name}: {data}")

threads = []

for file_name in file_names:
    thread = threading.Thread(target=parse_json, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

###############
######Task2
###########

import threading
import queue
import time

def process_queue(q):
    while not q.empty():
        num = q.get()
        thread_name = threading.current_thread().name
        even = "even" if num % 2 == 0 else "odd"
        print(f"Thread {thread_name}: Retrieved {num} ({even})")
        q.task_done()

q = queue.Queue()

threads = []
for i in range(3):
    thread = threading.Thread(target=process_queue, args=(q,), name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

time.sleep(1)
numbers = [8, 3, 10, 5, 2, 15, 7]
for num in numbers:
    q.put(num)

for thread in threads:
    thread.join()

print("Sorted numbers:", sorted(numbers))
print("All tasks completed.")

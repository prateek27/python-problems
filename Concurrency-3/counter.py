import threading

class Counter:
    def __init__(self, initial_count):
        self._count = initial_count
        self._lock = threading.Lock()

    def incValue(self, offset):
        with self._lock:
            self._count += offset

    def getValue(self):
        with self._lock:
            return self._count

    def decValue(self, offset):
        with self._lock:
            self._count -= offset

# show sample usage
# Function for concurrent increment operation
def concurrent_inc(counter, offset):
    for _ in range(1000):
        counter.incValue(offset)

# Function for concurrent decrement operation
def concurrent_dec(counter, offset):
    for _ in range(1000):
        counter.decValue(offset)

# Create a Counter instance with initial value 0
counter = Counter(0)

# Create and start multiple threads for concurrent increment and decrement
threads = []
for _ in range(10):
    thread_inc = threading.Thread(target=concurrent_inc, args=(counter, 1))
    thread_dec = threading.Thread(target=concurrent_dec, args=(counter, 1))
    threads.append(thread_inc)
    threads.append(thread_dec)
    thread_inc.start()
    thread_dec.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Check the final value of the counter
# expected output : 0
print("Final counter value:", counter.getValue())
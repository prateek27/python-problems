import threading

class Foo:
    def __init__(self):
        # self.semaphore_first = threading.Semaphore(1)
        # todo : init the required semaphores
        self.semaphore_second = threading.Semaphore(0)
        self.semaphore_third = threading.Semaphore(0)
        # output will store the string values added by each function call
        self.output = []

    def first(self):
        # Todo: Add "first" in the output array when this function is called
        self.output.append("first")
        self.semaphore_second.release()

    def second(self):
        # Todo: Add "second" in the output array when this function is called
        with self.semaphore_second:
            self.output.append("second")
            self.semaphore_third.release()

    def third(self):
        # Todo: Add "third" in the output array when this function is called
        with self.semaphore_third:
            self.output.append("third")

# Sample Usage
def worker_foo(method, foo_instance):
    method_dict = {
        "first": foo_instance.first,
        "second": foo_instance.second,
        "third": foo_instance.third
    }
    method_dict[method]()

# Create a Foo instance
foo = Foo()

# Create threads for calling first(), second(), and third()
threads = []
for method in ["third", "second", "first"]:
    thread = threading.Thread(target=worker_foo, args=(method, foo))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Check the output sequence
print("Output sequence:", foo.output)
# Expected Output
# Output sequence: ['first', 'second', 'third']


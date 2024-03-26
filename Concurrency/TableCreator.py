import threading

# Ask the learners to complete the Table Creator Class

class TableCreator(threading.Thread):
    def __init__(self, num):
        #todo
        super().__init__()
        self.num = num

    def run(self):
        #todo
        for i in range(1, 11):
            result = self.num * i
            print(f"{self.num} times {i} is {result}")

class Client:
    @staticmethod
    def main():
        n = int(input("Enter a number: "))

        threads = []
        for i in range(1, n + 1):
            thread = TableCreator(i)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

import threading

class Adder(threading.Thread):
    def run(self):
        print("I am the Adder class")

class Subtractor(threading.Thread):
    def run(self):
        print("I am the Subtractor class")

class Client:
    @staticmethod
    def main():
        print("I am the main class")
        adder_thread = Adder()
        subtractor_thread = Subtractor()

        adder_thread.start()
        subtractor_thread.start()

        adder_thread.join()
        subtractor_thread.join()

if __name__ == "__main__":
    Client.main()
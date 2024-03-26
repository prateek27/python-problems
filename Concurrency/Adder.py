import threading
"""Write code to achieve the following
A class Client with a main method.
Client class shall take two numbers as input from the user.
Client class should create a new thread and invoke code in a class called Adder.
Client class shall pass two numbers (taken as input from the user) to the Adder class.
The Adder class should print the sum of two numbers passed to it.
"""


class Adder(threading.Thread):
    #Todo
    def __init__(self, num1, num2):
        super().__init__()
        self.num1 = num1
        self.num2 = num2

    #Todo
    def run(self):
        result = self.num1 + self.num2
        print(result)

class Client:
    @staticmethod
    def main():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Todo
        adder_thread = Adder(num1, num2)
        adder_thread.start()
        adder_thread.join()

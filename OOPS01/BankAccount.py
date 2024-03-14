import unittest

"""
Create a Bank Account class in python.
It should have 3 data members
accountNumber: String
balance: int
roi:double (Should represent rate of interest)
It should have 2 methods
getSimpleInterest: It should take time (in years) as a parameter. The data type of time should be int. It should return Simple Interest as a double.
getBalanceWithInterest: It should take time (in years) as a parameter. The data type of time should 
be int. It should return a new balance (including simple interest) as a double.
"""

class BankAccount:
    def __init__(self, accountNumber, balance, roi):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi

    def getSimpleInterest(self, time):
        return self.balance * self.roi * time / 100.0

    def getBalanceWithInterest(self, time):
        return self.balance + self.getSimpleInterest(time)


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890", 1000, 5)  # Sample account

    def test_getSimpleInterest(self):
        # Test for 1 year
        self.assertAlmostEqual(self.account.getSimpleInterest(1), 50.0)
        # Test for 2 years
        self.assertAlmostEqual(self.account.getSimpleInterest(2), 100.0)

    def test_getBalanceWithInterest(self):
        # Test for 1 year
        self.assertAlmostEqual(self.account.getBalanceWithInterest(1), 1050.0)
        # Test for 2 years
        self.assertAlmostEqual(self.account.getBalanceWithInterest(2), 1100.0)


if __name__ == '__main__':
    unittest.main()

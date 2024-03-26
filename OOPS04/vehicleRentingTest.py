# Unit tests
import unittest
from vehicleRenting import Car, Bicycle


class TestRentable(unittest.TestCase):
    def test_car_rent(self):
        car = Car("Toyota")
        self.assertFalse(car.is_rented)
        car.rent()
        self.assertTrue(car.is_rented)
        car.rent()  # Renting again should print "already rented"
        car.return_item()
        self.assertFalse(car.is_rented)
        car.return_item()  # Returning again should print "not rented"

    def test_bicycle_rent(self):
        bicycle = Bicycle("Mountain Bike")
        self.assertFalse(bicycle.is_rented)
        bicycle.rent()
        self.assertTrue(bicycle.is_rented)
        bicycle.rent()  # Renting again should print "already rented"
        bicycle.return_item()
        self.assertFalse(bicycle.is_rented)
        bicycle.return_item()  # Returning again should print "not rented"


if __name__ == '__main__':
    unittest.main()
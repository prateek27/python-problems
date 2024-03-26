import unittest
from moviebooking import MovieTicketBookingSystem, book_seats
import threading

class TestMovieTicketBookingSystem(unittest.TestCase):
    def test_reserve_seats(self):
        booking_system = MovieTicketBookingSystem(100)
        self.assertTrue(booking_system.reserve_seats(10))  # Booking 10 seats
        self.assertTrue(booking_system.reserve_seats(5))   # Booking 5 more seats
        self.assertFalse(booking_system.reserve_seats(100))  # Attempting to book more seats than available
        self.assertTrue(booking_system.reserve_seats(50))   # Booking remaining available seats

    def test_get_available_seats(self):
        booking_system = MovieTicketBookingSystem(100)
        self.assertEqual(booking_system.get_available_seats(), 100)  # Initially, all seats are available
        booking_system.reserve_seats(10)  # Booking 10 seats
        self.assertEqual(booking_system.get_available_seats(), 90)   # 10 seats are booked, 90 seats available
        booking_system.reserve_seats(20)  # Booking 20 more seats
        self.assertEqual(booking_system.get_available_seats(), 70)   # 30 seats are booked, 70 seats available

    def test_concurrent_booking(self):
        booking_system = MovieTicketBookingSystem(100)
        num_threads = 10
        seats_per_thread = 10
        threads = []

        # Create and start multiple threads for concurrent booking
        for _ in range(num_threads):
            thread = threading.Thread(target=book_seats, args=(booking_system,seats_per_thread))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check if total booked seats do not exceed total available seats
        total_booked_seats = 100 - booking_system.get_available_seats()
        self.assertLessEqual(total_booked_seats, 100)

if __name__ == "__main__":
    unittest.main()
# Unit tests for concurrent booking
import unittest
from trainreservation import TrainReservationSystem
import threading

class TestTrainReservationSystem(unittest.TestCase):
    def test_concurrent_booking(self):
        initial_seats = {
            "1AC": 50,
            "2AC": 100,
            "3AC": 150,
            "Sleeper": 200
        }
        reservation_system = TrainReservationSystem(initial_seats)
        num_threads = 5
        seats_per_thread = 5
        threads = []

        # Create and start multiple threads for concurrent booking
        for _ in range(num_threads):
            thread = threading.Thread(target=self.book_seats, args=(reservation_system, "1AC", seats_per_thread))
            threads.append(thread)
            thread.start()

        for _ in range(num_threads):
            thread = threading.Thread(target=self.book_seats, args=(reservation_system, "2AC", 2*seats_per_thread))
            threads.append(thread)
            thread.start()

        for _ in range(num_threads):
            thread = threading.Thread(target=self.book_seats, args=(reservation_system, "3AC", 7*seats_per_thread))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check if total booked seats do not exceed total available seats for 1AC
        total_booked_seats = 50 - reservation_system.get_available_seats("1AC")
        self.assertEqual(total_booked_seats, 25)

        total_booked_seats = 100 - reservation_system.get_available_seats("2AC")
        self.assertEqual(total_booked_seats, 50)

        total_booked_seats = 150 - reservation_system.get_available_seats("3AC")
        self.assertEqual(reservation_system.get_available_seats("3AC"),10)

    def book_seats(self, reservation_system, seat_type, num_seats):
        success = reservation_system.reserve_seats(seat_type, num_seats)


if __name__ == "__main__":
    unittest.main()

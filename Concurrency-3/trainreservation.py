import threading
import random


class TrainReservationSystem:
    def __init__(self, initial_seats):
        self.available_seats = initial_seats
        self.lock = threading.RLock()  # Reentrant Lock

    def reserve_seats(self, seat_type, num_seats):
        # todo
        with self.lock:
            if seat_type not in self.available_seats:
                print("Invalid seat type.")
                return False
            if num_seats > self.available_seats[seat_type]:
                print(f"Not enough {seat_type} seats available for booking.")
                return False
            self.available_seats[seat_type] -= num_seats
            print(
                f"{num_seats} {seat_type} seats booked successfully. Available {seat_type} seats: {self.available_seats[seat_type]}")
            return True

    def get_available_seats(self, seat_type):
        # todo
        with self.lock:
            if seat_type not in self.available_seats:
                print("Invalid seat type.")
                return -1
            return self.available_seats[seat_type]


# Example Use
# Create initial seat availability dictionary
initial_seats = {
    "1AC": 50,
    "2AC": 100,
    "3AC": 150,
    "Sleeper": 200
}

# Create an instance of TrainReservationSystem
reservation_system = TrainReservationSystem(initial_seats)


# Example usage: Concurrent Booking
# Function to perform concurrent booking
def concurrent_booking(reservation_system, num_threads, seats_per_thread):
    threads = []

    # Create and start multiple threads for concurrent booking
    for _ in range(num_threads):
        seat_type = random.choice(list(reservation_system.available_seats.keys()))
        thread = threading.Thread(target=book_seats, args=(reservation_system, seat_type, seats_per_thread))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


# Function for each thread to attempt booking seats
def book_seats(reservation_system, seat_type, num_seats):
    success = reservation_system.reserve_seats(seat_type, num_seats)
    if success:
        print(f"Successfully booked {num_seats} {seat_type} seats")
    else:
        print(f"Failed to book {num_seats} {seat_type} seats")


# Example usage: Concurrent booking
num_threads = 10  # Number of concurrent threads
seats_per_thread = 5  # Number of seats each thread attempts to book
concurrent_booking(reservation_system, num_threads, seats_per_thread)

# Check available seats after concurrent bookings
print("Available 1AC seats:", reservation_system.get_available_seats("1AC"))
print("Available 2AC seats:", reservation_system.get_available_seats("2AC"))
print("Available 3AC seats:", reservation_system.get_available_seats("3AC"))
print("Available Sleeper seats:", reservation_system.get_available_seats("Sleeper"))


class Flight:
    # Counter is a Class variable
    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
        self.passengers = []

        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        """ Method for printing specific attributes of flight object """
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        """ Adds delay in minutes to flight object's duration """
        self.duration += amount

    def add_passenger(self, p):
        """ Adds passenger to flight and
            writes flight number back to passenger object
        """
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:

    def __init__(self, name):
        self.name = name


def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")
    larry = Passenger("Larry")

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)
    f1.add_passenger(larry)

    f1.print_info()


if __name__ == "__main__":
    main()

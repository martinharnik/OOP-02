class TravelTicket:
    # The constructor initializes the attributes of the TravelTicket class
    def __init__(self, source, destination, date, price):
        self.source, self.destination, self.date, self.price = source, destination, date, price

    # Method to display ticket information
    def display_ticket_info(self):
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Date: {self.date}")
        print(f"Price: {self.price}")

# FlightTicket class inherits from TravelTicket
class FlightTicket(TravelTicket):
    # The constructor initializes the attributes of the FlightTicket class
    def __init__(self, source, destination, date, price, airline):
        # Call the constructor of the parent class
        super().__init__(source, destination, date, price)
        self.airline = airline
    
    # Method to display flight ticket information, overrides the method in the parent class
    def display_ticket_info(self):
        # Call the method from the parent class
        super().display_ticket_info()
        print(f"Airline: {self.airline}")

# Creating an instance of FlightTicket
flight_ticket = FlightTicket("NYC", "Prague", "05-12-2025", 7500, "Delta")

# Displaying flight ticket information
flight_ticket.display_ticket_info()

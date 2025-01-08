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

# TrainTicket class inherits from TravelTicket
class TrainTicket(TravelTicket):
    # The constructor initializes the attributes of the TrainTicket class
    def __init__(self, source, destination, date, price, train_name):
        # Call the constructor of the parent class
        super().__init__(source, destination, date, price)
        self.train_name = train_name
    
    # Method to display train ticket information, overrides the method in the parent class
    def display_ticket_info(self):
        # Call the method from the parent class
        super().display_ticket_info()
        print(f"Train name: {self.train_name}")

# Function to display ticket information, demonstrates polymorphism
def display_ticket_information(ticket):
    ticket.display_ticket_info()

# Creating instances of FlightTicket and TrainTicket
flight_ticket = FlightTicket("NYC", "Prague", "05-12-2025", 7500, "Delta")
train_ticket = TrainTicket("Bratislava", "Praha", "08-07-2025", 1000, "Slovenská strela")

tickets = [flight_ticket, train_ticket]
for ticket in tickets:
        display_ticket_information(flight_ticket)
        print("\n")
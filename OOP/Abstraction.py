from abc import ABC, abstractmethod

class TravelTicket(ABC):
    def __init__(self, source, destination, date, price):
        self.source, self.destination, self.date, self.price = source, destination, date, price

    @abstractmethod
    def display_ticket_info(self):
        pass

class FlightTicket(TravelTicket):
        def __init__(self, source, destination, date, price, airline):
            super().__init__(source, destination, date, price)
            self.airline = airline

        def display_ticket_info(self):
            print(f"Source: {self.source}")
            print(f"Destination: {self.destination}")
            print(f"Date: {self.date}")
            print(f"Price: {self.price}")
            print(f"Airline: {self.airline}")

class TrainTicket(TravelTicket):
        def __init__(self, source, destination, date, price, train_name):
            super().__init__(source, destination, date, price)
            self.train_name = train_name

        def display_ticket_info(self):
            print(f"Source: {self.source}")
            print(f"Destination: {self.destination}")
            print(f"Date: {self.date}")
            print(f"Price: {self.price}")
            print(f"Train name: {self.train_name}")

flight_ticket = FlightTicket("NYC", "Prague", "05-12-2025", 7500, "Delta")
train_ticket = TrainTicket("Bratislava", "Praha", "08-07-2025", 1000, "Slovenská strela")

flight_ticket.display_ticket_info()
print("\n")
train_ticket.display_ticket_info()
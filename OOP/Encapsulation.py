class TravelTicket:
    # The constructor initializes the attributes of the TravelTicket class
    def __init__(self, source, destination, date, price):
        self.source, self.destination, self.date, self.price = source, destination, date, price

    # Getter method for source attribute
    def get_source(self):
        return self.source
    
    # Setter method for source attribute
    def set_source(self, source):
        self.source = source

    # Getter method for destination attribute
    def get_destination(self):
        return self.destination
    
    # Setter method for destination attribute
    def set_destination(self, destination):
        self.destination = destination

    # Getter method for date attribute
    def get_date(self):
        return self.date
    
    # Setter method for date attribute
    def set_date(self, date):
        self.date = date
    
    # Getter method for price attribute
    def get_price(self):
        return self.price
    
    # Setter method for price attribute
    def set_price(self, price):
        self.price = price

# Creating an instance of TravelTicket
ticket = TravelTicket("Prague", "Barcelona", "15-05-2025", 5000)

# Accessing attributes using getter methods
print(f"Source: {ticket.get_source()}")
print(f"Destination: {ticket.get_destination()}")
print(f"Date: {ticket.get_date()}")
print(f"Price: {ticket.get_price()}")

# Modifying attributes using setter methods
ticket.set_destination("London")
ticket.set_date("20-07-2025")

# Accessing modified attributes using getter methods
print(f"Modified Destination: {ticket.get_destination()}")
print(f"Modified Date: {ticket.get_date()}")
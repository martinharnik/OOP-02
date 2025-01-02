class Superhero():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use_power(self):
        print(f"{self.name} is using {self.power} power!")

    def intro(self):
        print(f"I am {self.name} and I have the {self.power} power!")

    def save_day(self):
        print(f"{self.name} has saved the day!")

    def power_level(self):
        length = len(self.power)
        level = length * 10
        return level
    

class Flying(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} is flying at the speed of {self.speed} miles per hour.")

    def cal_distance(self, flight_time):
        distance = self.speed * flight_time
        return distance



batman = Superhero("Batman", "Strength")

batman.intro()
print(batman.power_level())

print()
superman = Flying("Clark Kent", "Flight", 250)
superman.intro()
superman.use_power()

flight_distance = 30
attack = superman.cal_distance(flight_distance)
print(f"{superman.name} can fly a distance of {attack} miles in {flight_distance} hours.")
class App:
    def __init__(self, username, storage):
        self.username = username
        self.storage = storage
    
    def login(self):
        if self.username == "owner":
            print(f"Hello {self.username}")
        else:
            print("Access denied!")

    def increase_capacity(self, number):
        self.storage += number
    
product01 = App("owner", 150)
product01.login()
product01.increase_capacity(50)
print(product01.storage)

product02 = App("Jeff", 100)
product02.login()
product02.increase_capacity(50)
print(product02.storage)

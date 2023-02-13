class user:
    def __init__(self,first_name, last_name, email, age):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.age= age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self, amount):
        print(f"Current Points: {self.gold_card_points}")

my_user = user("Sadie", "Flick", "sflick@codingdojo.com", 99)
my_user.display_info().enroll().display_info().spend_points(100).display_info()


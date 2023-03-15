class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is rewards member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        print(f"Congratulations {self.first_name} on your new membership!")
        return self
    
    def add_points(self, points):
        self.gold_card_points = self.gold_card_points + points
        print(f"{self.first_name}, your new points balance is: {self.gold_card_points}")
        return self

    def spend_points(self, deduct):
            if self.is_rewards_member == False:
                print(f"You are not yet a Gold Points Member. Would you like to enroll now?")
                return self
            elif self.gold_card_points >= deduct:
                self.gold_card_points -= deduct
                print(f"{self.first_name}, your remaining points total: {self.gold_card_points}")
                return self
            else:
                print(f"{self.first_name}, you do not have enough points to spend {deduct}. Your current balance is {self.gold_card_points}.")
                return self


user_1 = User("Ryan", "Harvey", "ryan@ryanharvey.codes", 32)
user_2 = User("James", "Keynan", "godlyvocals@gmail.com", 99)
user_3 = User("Bilbo", "Baggins", "shirefire@hob.net", 47)

user_1.display_info().spend_points(50)
user_2.display_info().enroll().add_points(150).spend_points(80)
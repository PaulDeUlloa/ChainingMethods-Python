class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("--------------------------")        
        print(f" First name:{self.first_name}")
        print(f" Last name:{self.last_name}")
        print(f" Email:{self.email}")
        print(f" Age:{self.age}")
        print(f" Member:{self.is_rewards_member}")
        print(f" Current Points:{self.gold_card_points}")
        print("--------------------------")
    def enroll(self):
        if(self.is_rewards_member):
            print("User already a member here.")
            return self
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("insuffient points")
            return False
        self.gold_card_points -= amount

Paul = User("Paul","De Ulloa","Pauld@CodingDojo.com",26)
Joe = User("Joe","Doodle","Joed@CodingDojo.com",62)

Paul.enroll().spend_points(50)
Joe.enroll().spend_points(80)

Paul.display_info()
Joe.display_info()


"""
class Car:
    pass

blue_car = Car()
blue_car.part = 5
blue_car.colour = "blue"

print(blue_car.part, blue_car.colour)
"""



class GoogleAccount:
    def __init__(self, username, user_id):
        self.name = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

account_1 = GoogleAccount("Rehan", "001")
account_2 = GoogleAccount("Ali", "002")

print(account_1.name, account_1.user_id)
print(account_2.name, account_2.user_id)

account_1.follow(account_2)

print(account_1.followers)
print(account_1.following)
print(account_2.followers)
print(account_2.following)


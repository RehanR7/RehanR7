import random
from game_data import data
from art import logo, vs


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, form {country}."

def check_answer(user_guess,check_a, check_b):
    if check_a > check_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
is_game_over = True
account_b = random.choice(data)

while is_game_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A{format_data(account_a)}")
    print(vs)
    print(f"Compare B{format_data(account_b)}")

    guess = input("Who has more followers. Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']

    is_correct = check_answer(guess, followers_a, followers_b)
    if is_correct:
        score += 1
        print(f"You're correct! Current score: {score}.")
    else:
        print(f"Sorry that's wrong. Final score: {score}.")
        is_game_over = False
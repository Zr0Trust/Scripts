
def game():
    print("=" * 30)
    print(" " * 10 + "HIGHER\n" + " " * 10 + "LOWER")
    print(" WHO HAS MORE INSTAGRAM FOLLOWERS")
    print("=" * 30)

def game_over():
    print("=" * 30)
    print(" " * 10 + "GAME\n" + " " * 10 + "OVER")
    print("=" * 30)

def keep_score():
    if correct == True:
        print("Correct!" + " Your score is: " + str(score))
    else:
        print("Incorrect! Your score is: " + str(score))
        game_over()
        exit()

game()

#define score
score = 0

#create list of higher or lower
#actual followers numbers are probably not accurate

people = [{"name": "Cristiano Ronaldo", "followers": 540000000}, {"name": "Lionel Messi", "followers": 430000000},
          {"name": "Kylie Jenner", "followers": 380000000}, {"name": "Kim Kardashian", "followers": 350000000},
          {"name": "Selena Gomez", "followers": 340000000}, {"name": "Ariana Grande", "followers": 250000000},
          {"name": "Dwayne Johnson", "followers": 251000000}, {"name": "Beyoncé", "followers": 240000000},
          {"name": "Justin Bieber", "followers": 230000000}, {"name": "Taylor Swift", "followers": 231000000}]

#create inputs requesting responses to questions

cristiano_followers = next(person["followers"] for person in people if person["name"] == "Cristiano Ronaldo")
selena_followers = next(person["followers"] for person in people if person["name"] == "Selena Gomez")
kylie_followers = next(person["followers"] for person in people if person["name"] == "Kylie Jenner")
kim_followers = next(person["followers"] for person in people if person["name"] == "Kim Kardashian")
lionel_followers = next(person["followers"] for person in people if person["name"] == "Lionel Messi")
ariana_followers = next(person["followers"] for person in people if person["name"] == "Ariana Grande")
dwayne_followers = next(person["followers"] for person in people if person["name"] == "Dwayne Johnson")
beyoncé_followers = next(person["followers"] for person in people if person["name"] == "Beyoncé")
justin_followers = next(person["followers"] for person in people if person["name"] == "Justin Bieber")
taylor_followers = next(person["followers"] for person in people if person["name"] == "Taylor Swift")

# Question 1

user_answer = input("Cristiano Ronaldo has 540 million followers. Does Selena Gomez have higher or lower followers? (Type 'higher' or 'lower'):\n")

# Check user answer
if user_answer.lower() == "higher":
    correct = selena_followers > cristiano_followers
    correct = False
elif user_answer.lower() == "lower":
    correct = selena_followers < cristiano_followers
    score += 1
else:
    correct = False

#keep score

keep_score()

# Question 2

user_answer = input("Justin Bieber has 230 million followers. Does Kim Kardashian have higher or lower followers? (Type 'higher' or 'lower'):\n")

# Check user answer
if user_answer.lower() == "higher":
    correct = kim_followers > justin_followers
    score += 1
elif user_answer.lower() == "lower":
    correct = justin_followers < kim_followers
    correct = False
else:
    correct = False

#keep score

keep_score()

# Question 3

user_answer = input("Lionel Messi has 430 million followers. Does Kylie Jenner have higher or lower followers? (Type 'higher' or 'lower'):\n")

# Check user answer
if user_answer.lower() == "higher":
    correct = lionel_followers > kylie_followers
    correct = False
elif user_answer.lower() == "lower":
    correct = kylie_followers < lionel_followers
    score += 1
else:
    correct = False

#keep score

keep_score()

# Question 4

user_answer = input("Dwayne Johnson has 251 million followers. Does Beyoncé have higher or lower followers? (Type 'higher' or 'lower'):\n")

# Check user answer
if user_answer.lower() == "higher":
    correct = dwayne_followers > beyoncé_followers
    correct = False
elif user_answer.lower() == "lower":
    correct = beyoncé_followers < dwayne_followers
    score += 1
else:
    correct = False

#keep score

keep_score()

# Question 5

user_answer = input("Taylor Swift has 231 million followers. Does Ariana Grande have higher or lower followers? (Type 'higher' or 'lower'):\n")

# Check user answer
if user_answer.lower() == "higher":
    correct = ariana_followers > taylor_followers
    score += 1
elif user_answer.lower() == "lower":
    correct = ariana_followers < taylor_followers
    correct = False
else:
    correct = False

#keep score

keep_score()

print("="* 30)

game_over()

print("Your final score is: " + str(score))

#if user gets one wrong, end game and provide score


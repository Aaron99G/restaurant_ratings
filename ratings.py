"""Restaurant rating lister."""


# put your code here
my_file = open("scores.txt", "r")
scores = sorted(list(my_file))


def see_scores():
    for line in scores:
        print(line)

def add_new():
    new_rest = input("What restaurant have you been to?")
    new_score = int(input("What score, out of 5, would you give it?"))

    while new_score > 5 or new_score < 1:
        print("Invalid score, try again:")
        new_score = int(input("What score, out of 5, would you give it?"))
        

    new_rating = (new_rest + ":" + str(new_score) + "\n")
    scores.append(new_rating)

    for line in scores:
        print(line)

    
user_choice = int(input("Would you like to 1) See current ratings? 2) Add a new restaurant? 3) Quit?\nEnter the number corresponding to the question:"))

while user_choice != 3:
    if user_choice == 1:
        see_scores()
    elif user_choice == 2:
        add_new()
    user_choice = int(input("Would you like to 1) See current ratings? 2) Add a new restaurant? 3) Quit?\nEnter the number corresponding to the question:"))
else:
    print("See ya later!")
    
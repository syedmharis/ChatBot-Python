from functions import *

# create chatbot 
home_bot = create_bot('RichBot')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
if identity == "Haris":
    print("Welcome, Haris. Happy to have you at home.")

elif identity == "Khalid":
    print("Haris is out right now, but you are welcome to the house.")

else:
    print("Your access is denied here.")
    exit()

# custom data
house_owner = [
    "Who is the owner of this house?",
    "Syed Haris is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
if identity == 'Haris':
    your_identity = [
        "Who is using this software?",
        "It is difficult to predict. I wish i could access the camera."
    ] 
    city_born = [
        "Where was I born?",
        "Haris, you were born in Karachi."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is MalcomX."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Interstellar more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved Football."
    ]
    my_uni = [
        "Where do i study?",
        "You are studying Software Engineering in Usman University."
    ]
    # train chatbot with your custom data
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sports)
    custom_train(home_bot, your_identity)
    custom_train(home_bot, my_uni)

# start chatbot
start_chatbot(home_bot)
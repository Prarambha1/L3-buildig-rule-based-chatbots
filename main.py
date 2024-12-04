import re
import random
from colorama import Fore, init
#init
init(autoreset=True)
# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities":["Tokyo","Paris","New York"]
    #add cities
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def greet_user():
    print(Fore.CYAN+"Hello, I am travel bot, your virtual travel assistant.")
    name=input(Fore.YELLOW+"May I know your name:")
    print(Fore.GREEN+f"Nice to meet you {name}. How can I assist you today?")
    return name

# Function to show help options
def show_help():
    print(Fore.MAGENTA+"\n I can assist you with the following:")
    print(Fore.GREEN+"\n Provide travel recommendation.")
    # print(Fore.GREEN+"\n Offer packing tips.")
    print(Fore.GREEN+"\n Tell travel jokes.")
    print(Fore.CYAN+"\n Just ask me a question or type 'Exit' to leave.")
    

# Function to process user input
def process_input(user_input):
    user_input=user_input.strip().lower()
    user_input=re.sub(r"\s+"," ",user_input)
    return user_input

# Function to provide travel recommendations
def provide_recomendation():
    print(Fore.CYAN+"Travel bot: Sure! Are you interested in beaches, mountains or cities?")
    preference=input(Fore.YELLOW+"You:")
    preference= process_input(preference)
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.GREEN+f"Travel bot: How about visiting {suggestion}")
    else:
        print(Fore.RED+f"Travel bot: I don't have any recommendations for that preference.")

# Function to check flight status (simulated)


# Function to offer packing tips


# Function to tell a joke
def tell_joke():
    joke=random.choice(jokes)
    print(Fore.YELLOW+f"Travel bot: {joke}")

# Main chat function
def chat():
    name=greet_user()
    show_help()
    while True:
        user_input=input(Fore.YELLOW+f"{name}:")
        processed_input=process_input(user_input)
        if "recommendation" in processed_input or "suggest" in processed_input:
            provide_recomendation()
        elif "joke" in processed_input or "funny" in processed_input:
            tell_joke()
        elif "Help" in processed_input:
            show_help()
        elif "Exit" in processed_input or "Bye" in processed_input:
            print(Fore.CYAN+f"Travel bot: Bye bye, {name}. Travel safe")
            break
        else:
            print(Fore.RED+f"Travel bot: I am sorry {name}.Could you please refresh that for me?")

# Start the chatbot
if __name__ == "__main__":
    chat()
    

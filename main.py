import re
import random
from colorama import Fore, init
#init
init(autoreset=True)
# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket","Fiji","Bora Bora", "Maui"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities":["Tokyo","Paris","New York","Seoul","Kathmandu","Brussels"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!",
    "Why was the computer cold? It left its Windows open!",
    "Why don't eggs tell jokes? They'd crack each other up"
]

flight_status = ["On time", "Delayed by 30 minutes", "Cancelled", "Boarding now", "Landed","Security check in progress","Arrived at the gate"]

# Function to greet the user
def greet_user():
    print(Fore.CYAN+"Hello, I am Travel bot, your virtual travel assistant.")
    name=input(Fore.YELLOW+"May I know your name:")
    print(Fore.GREEN+f"Nice to meet you {name}. How can I assist you today?")
    return name

# Function to show help options
def show_help():
    print(Fore.MAGENTA+"\n I can assist you with the following:")
    print(Fore.GREEN+"\n Provide travel recommendation.")
    print(Fore.GREEN+"\n Offer packing tips.")
    print(Fore.GREEN+"\n Tell travel jokes.")
    print(Fore.GREEN +"\n Check flight status.")
    print(Fore.CYAN+"\n Just ask me a question or type 'Exit' to leave.")
    

# Function to process user input
def process_input(user_input):
    user_input= user_input.strip().lower()
    user_input= re.sub(r"\s+", " ", user_input)
    return user_input

# Function to provide travel recommendations
def provide_recommendation():
    print(Fore.CYAN + "Travel Bot: Sure! Are you interested in beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = process_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travel Bot: How about visiting {suggestion}?")
        print(Fore.GREEN + "Do you like this suggestion (yes/no)?")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(Fore.GREEN + f"Travel Bot: Great! Have an amazing time in {suggestion}!")
        elif response == "no":
            print(Fore.RED + "Travel Bot: No worries! Let's find another place.")
            provide_recommendation()  
            return  
        else:
            print(Fore.RED + "Travel Bot: I didn't catch that. Let's start over.")
            provide_recommendation()  
            return  
    else:
        print(Fore.RED + "Travel Bot: Sorry, I don't have any recommendations for that preference.")

    print("\n" + Fore.CYAN + "Do you need help with anything else?")
    show_help()

# Function to check flight status (simulated)
def check_flight_status():
    while True:
        print(Fore.CYAN + "Travel Bot: Please enter your flight number (e.g., AB123):")
        flight_number = input(Fore.YELLOW + "You: ").strip().upper()
        if re.match(r"^[A-Z]{2}\d{1,4}$", flight_number):
            status = random.choice(flight_status) 
            print(Fore.GREEN + f"Travel Bot: The status of flight {flight_number} is: {status}.")
            break  
        else:
            print(Fore.RED + "Travel Bot: Invalid flight number format. Please use the format (e.g., AB123).")

    print("\n" + Fore.CYAN + "Do you need help with anything else?")
    show_help()

# Function to offer packing tips
def offer_packing_tips():
    while True:
        print(Fore.CYAN + "Travel Bot: Where are you travelling to?")
        destination = input(Fore.YELLOW + "You: ").strip()
        if not destination.isalpha():  
            print(Fore.RED + "Travel Bot: Please enter a valid destination name (letters only).")
        else:
            break  
    while True:
        print(Fore.CYAN + "Travel Bot: How many days will you be staying?")
        days = input(Fore.YELLOW + "You: ").strip()
        if not days.isdigit():  
            print(Fore.RED + "Travel Bot: Please enter a valid number for the days.")
        else:
            days = int(days) 
            break  
    print(Fore.GREEN + f"Travel Bot: Packing tips for {days} days in {destination}:")
    print(Fore.GREEN + "- Pack versatile clothing items.")
    print(Fore.GREEN + "- Don't forget travel adapters and chargers.")
    print(Fore.GREEN + "- Check the weather forecast before packing.")
    print(Fore.GREEN + "- Bring a lightweight backpack and place heavy items at the base of your luggage.")
    print(Fore.GREEN + "- Organize your liquid bags and keep travel essentials easy to access. Do not overpack.")
    print("\n" + Fore.CYAN + "Do you need help with anything else?")
    show_help()

# Function to tell a joke
def tell_joke():
    joke=random.choice(jokes)
    print(Fore.YELLOW+f"Travel bot: {joke}")
    print("\n" + Fore.CYAN + "Do you need help with anything else?")
    show_help()

# Main chat function
def chat():
    name=greet_user()
    show_help()
    while True:
        user_input=input(Fore.YELLOW+f"{name}:")
        processed_input=process_input(user_input)
        if "recommendation" in processed_input or "suggest" in processed_input or "travel" in processed_input:
            provide_recommendation()
        elif "joke" in processed_input or "funny" in processed_input or "jokes" in processed_input:
            tell_joke()
        elif "pack" in processed_input or "packing" in processed_input or "tips" in processed_input:
            offer_packing_tips()
        elif "flight" in processed_input or "flight status" in processed_input or "status" in processed_input:
            check_flight_status()
        elif "help" in processed_input:
            show_help()
        elif "exit" in processed_input or "bye" in processed_input:
            print(Fore.CYAN+f"Travel bot: Bye bye, {name}. Travel safe")
            break
        else:
            print(Fore.RED+f"Travel bot: I am sorry {name}. Could you please rephrase that for me?")

# Start the chatbot
if __name__ == "__main__":
    chat()
    
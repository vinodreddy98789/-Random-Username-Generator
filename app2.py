import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Kartik","Sachin","Happy", "Cool", "Brave", "Witty", "Loyal", "Chill", "Fierce", "Jolly", "Mighty", "Swift"]
nouns = ["Gali","Hiremat","Tiger", "Dragon", "Phoenix", "Panther", "Falcon", "Shark", "Wolf", "Eagle", "Bear", "Cobra"]

def generate_username(include_number=True, include_special=False, custom_addition=""):
    """Generates a random username with customization options."""
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adjective + noun

    if include_number:
        username += str(random.randint(10, 999))  # Adds a random number between 10-999

    if include_special:
        username += random.choice(string.punctuation)  # Adds a random special character

    if custom_addition:
        username += custom_addition  # Adds user-defined custom characters

    return username

def get_user_preferences():
    """Gets user preferences for customization."""
    
    include_number = input("Do you want to include numbers in the username? (yes/no): ").strip().lower() == "yes"
    include_special = input("Do you want to include special characters? (yes/no): ").strip().lower() == "yes"
    custom_addition = input("Enter any custom characters or numbers to add (or press Enter to skip): ").strip()
    
    return include_number, include_special, custom_addition

def save_to_file(usernames, filename="usernames.txt"):
    """Saves generated usernames to a file."""
    
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    
    print(f"\nUsernames saved to {filename}!")

def main():
    """Main function to run the interactive username generator."""
    
    print("🎉 Welcome to the Interactive Random Username Generator! 🎉\n")

    include_number, include_special, custom_addition = get_user_preferences()
    
    num_usernames = int(input("How many usernames would you like to generate? "))

    usernames = []

    print("\nHere are your generated usernames:")
    for _ in range(num_usernames):
        username = generate_username(include_number, include_special, custom_addition)
        usernames.append(username)
        print(f"🔹 {username}")

    save_choice = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        save_to_file(usernames)

if __name__ == "__main__":
    main()

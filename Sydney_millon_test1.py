from datetime import datetime

def process_input(user_input):
    if is_palindrome(user_input.replace(" ", "").lower()):
        return "Bien dit!", "Well said!", "Хорошо сказано!"
    else:
        return user_input

def is_palindrome(s):
    return s == s[::-1]

def get_time_based_greeting():
    current_hour = datetime.now().hour
    if 8 <= current_hour < 13:
        return "Bonjour", "Good morning", "Доброе утро"
    elif 13 <= current_hour < 19:
        return "Bonne après-midi", "Good afternoon", "Добрый день"
    elif 19 <= current_hour < 23:
        return "Bonsoir", "Good evening", "Добрый вечер"
    elif 23 <= current_hour or current_hour < 5:
        return "Bonne insomnie", "Good night", "Доброй ночи"
    else:
        return "Bon réveil", "Good awakening", "Доброе утро"

def get_time_based_farewell():
    current_hour = datetime.now().hour
    if 8 <= current_hour < 13:
        return "Au revoir, bonne matinée, Goodbye, good morning, До свидания, доброе утро"
    elif 13 <= current_hour < 19:
        return "Au revoir, bonne après-midi, Goodbye, good afternoon, До свидания, добрый день"
    elif 19 <= current_hour < 23:
        return "Au revoir, bonne soirée, Goodbye, good evening, До свидания, приятного вечера"
    else:
        return "Au revoir, bonne nuit, Goodbye, good night, До свидания, спокойной ночи"

def main():
    print(*get_time_based_greeting(), sep="\n")

    while True:
        user_input = input("Enter a text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print(get_time_based_farewell())
            break
        elif is_palindrome(user_input.replace(" ", "").lower()):
            print("Bien dit!", "Well said!", "Хорошо сказано!")
        else:
            print(user_input)

if __name__ == "__main__":
    main()

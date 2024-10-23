import subprocess

def open_app(command):
    try:
        if "notepad" in command.lower():
            subprocess.Popen('notepad.exe')
            return "Opening Notepad..."
        elif "calculator" in command.lower():
            subprocess.Popen('calc.exe')
            return "Opening Calculator..."
        elif "settings" in command.lower():
            subprocess.Popen('start ms-settings:', shell=True)
            return "Opening Windows Settings..."
        else:
            return "Sorry, I don't recognize that command."
    except Exception as e:
        return f"An error occurred: {e}"

def chatbot():
    print("Chatbot is running... Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = open_app(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()

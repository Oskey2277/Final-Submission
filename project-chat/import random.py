import random
import json
import datetime

# Load chatbot configurations (keywords and responses) from a file
def load_chatbot_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

# Generate a random assistant name
def get_random_assistant_name(assistant_names):
    return random.choice(assistant_names)

# Get a suitable response based on user input
def fetch_response(user_message, chatbot_config):
    user_message = user_message.lower()

    # Search for relevant responses based on keywords in the user message
    for topic, responses in chatbot_config["chat_responses"]["topics"].items():
        if topic in user_message:
            return random.choice(responses)

    # Return a default response if no matching topic is found
    return random.choice(chatbot_config["chat_responses"]["default_responses"])

# Save the conversation log to a file
def save_chat_log(user_name, assistant_name, conversation_history, log_file="chat_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as log:
        log.write(f"\n--- Chat started on {timestamp} ---\n")
        for log_entry in conversation_history:
            log.write(f"{log_entry}\n")
        log.write("--- Chat ended ---\n")

# Main chatbot functionality
def virtual_assistant():
    # File path for chatbot configurations
    config_file_path = r'C:\Users\oskar\Downloads\Oskar\project-chat\json.json'
    chatbot_config = load_chatbot_config(config_file_path)

    # Define assistant names and exit keywords
    assistant_names = ["Chris", "Sam", "Taylor", "Jordan", "Alex"]
    exit_keywords = ["goodbye", "end", "exit", "quit"]

    # Greet the user
    user_name = input("Hi there! What's your name? ")
    print(f"Nice to meet you, {user_name}!")
    assistant_name = get_random_assistant_name(assistant_names)
    print(f"My name is {assistant_name}. I'm here to assist you. Type 'goodbye', 'quit', or 'exit' anytime to end the chat.")

    # Start the conversation log
    conversation_history = [f"{assistant_name}: Nice to meet you, {user_name}!"]

    while True:
        user_message = input(f"{user_name}: ")
        conversation_history.append(f"{user_name}: {user_message}")

        # Check for exit commands
        if user_message.lower() in exit_keywords:
            farewell = f"{assistant_name}: Goodbye, {user_name}! Take care!"
            print(farewell)
            conversation_history.append(farewell)
            break

        # Simulate random disconnections (5% chance)
        if random.random() < 0.05:
            disconnect_message = f"{assistant_name}: Oh no! It seems we've been disconnected. Please try again later."
            print(disconnect_message)
            conversation_history.append(disconnect_message)
            break

        # Fetch and print the response
        response = fetch_response(user_message, chatbot_config)

        # Personalize the response by inserting the user's name if needed
        if "{user_name}" in response:
            response = response.replace("{user_name}", user_name)

        print(f"{assistant_name}: {response}")
        conversation_history.append(f"{assistant_name}: {response}")

    # Save the conversation log to a file
    save_chat_log(user_name, assistant_name, conversation_history)

# Run the virtual assistant if this script is executed directly
if __name__ == "__main__":
    virtual_assistant()

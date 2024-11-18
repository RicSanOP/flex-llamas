import os

#from groq import Groq

from langchain_community.llms import Ollama
# Set your Anthropic API key

llm = Ollama(model="llama3.2:latest", base_url="http://127.0.0.1:42069/")


def badchat():
    # Create a client using the API key
 #   client = Groq(api_key="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")

    # Initialize chat history

    chat_history = ''
    while True:
        # Get user input
        user_input = input("You: ")




        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Append the user input to the conversation
        chat_history += f"User: {user_input}  "






        try:

            response = llm.invoke(chat_history)


            # Extract Claude's reply
            assistant_reply = response

            # Append Claude's reply to the conversation
            chat_history += f"Claude: {assistant_reply}"

            # Display the reply
            print(f"Claude: {assistant_reply}")

        except Exception as e:
            print(f"An error occurred: {e}")
            break






# Append the user input to the conversation
if __name__ == "__main__":
    badchat()



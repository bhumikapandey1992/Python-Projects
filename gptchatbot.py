# GPT chatbot

# Step 1: import libraries
import openai
from openai import OpenAI

# Step 2: set API Key
client = OpenAI(api_key="your-openai-secret-key")

# Step 3: Create chat history
chat_history = [
    {"role":"system", "content":"You are a helpful assistant."}
]

# Step 4: define chat function
def chat_with_GPT(user_input):
    chat_history.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
        temperature=0.7
    )
    reply = response.choices[0].message.content
    chat_history.append({"role":"assitant", "content":reply})
    return reply

# Step 5: chat loop
print("GPT chatbot: Hello! Type 'exit' to quit.")
while True:
    user_input = input("You:")
    if user_input.lower() == 'exit':
        break
    reply = chat_with_GPT(user_input)
    print("GPT:",reply)
    
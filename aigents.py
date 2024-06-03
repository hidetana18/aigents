import requests

# Replace with your OpenAI API key
API_KEY = os.environ["OPENAI_API_KEY"]

# Function to get a response from ChatGPT with conversation history
def get_chatgpt_response(messages):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': 'gpt-4o',  # Use the appropriate model name
        'messages': messages
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Initial messages
messages = [
    {"role": "user", "content": "Hello, how are you?"}
]

# Number of exchanges
num_exchanges = 5

# Simulate a conversation
for i in range(num_exchanges):
    print(f"ChatGPT A: {messages[-1]['content']}")
    response_a = get_chatgpt_response(messages)
    print(f"ChatGPT B: {response_a}")
    
    # Add response to messages
    messages.append({"role": "assistant", "content": response_a})
    
    # Alternate the conversation with a varied user input
    if i % 2 == 0:
        user_input = "That's interesting. Can you tell me more about AI?"
    else:
        user_input = "Thanks for sharing! What are your thoughts on machine learning?"

    print(f"ChatGPT A: {user_input}")
    messages.append({"role": "user", "content": user_input})

    # Pause if you want to avoid too many requests in a short period
    # import time
    # time.sleep(1)

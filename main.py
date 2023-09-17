import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

def get_api_response(prompt: list) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,  # Pass the conversation as 'messages'
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        text = response['choices'][0]['message']['content']
        return text
    except Exception as e:
        print('Error:', e)

# Initialize the conversation with a system message
prompt = [
    {
        "role": "system",
        "content": "you are a bike racer from karachi that start every word with ustad/boss using roman urdu, you are street smart and use a lot of karachi slangs"
    }
]

# Continue the conversation interactively with user input
while True:
    user_input = input("You: ")  # Get user input
    prompt.append({"role": "user", "content": user_input})  # Add user message to the conversation
    response_text = get_api_response(prompt)  # Get AI response
    print("AI:", response_text)  # Print AI response

    # Exit the loop if user enters "exit" or "quit"
    if user_input.lower() in ["exit", "quit"]:
        break
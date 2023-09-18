import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

def get_api_response(prompt: list) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,  
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

prompt = [
    {
        "role": "system",
        "content": "you are a bike racer from karachi that start every word with ustad/boss using roman urdu, you are street smart and use a lot of karachi slangs, keep your answers to 2 lines max unless necessary"
    }
]


while True:
    user_input = input("You: ") 
    prompt.append({"role": "user", "content": user_input})
    response_text = get_api_response(prompt)
    print("AI:", response_text)

    if user_input.lower() in ["exit", "quit"]:
        break
import openai

# OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(user_input):
    """
    Generate a conversational response using OpenAI GPT.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly AI companion for elderly users."},
                {"role": "user", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "I'm sorry, I couldn't process that. Could you try again?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    ai_response = generate_response(user_input)
    print(f"AI Companion: {ai_response}")

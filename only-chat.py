# Load GPT
from nomic.gpt4all import GPT4All
with GPT4All() as bot:
    while True:
        line = input("Me: ")
        response = bot.prompt(line)
        # avoid the error : AttributeError: 'str' object has no attribute 'sub'
        print("Bot: " + str(response).replace(r'[^a-zA-Z0-9\s.,!?]', ''))

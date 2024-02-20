from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.storage import SQLStorageAdapter

# Kreiranje novog chat bota sa SQLite bazom podataka
chatbot = ChatBot(
    'Moj ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    response_selection_method=get_most_frequent_response
)

# Kreiranje novog trenera za chat bot
trainer = ListTrainer(chatbot)

# Definisanje konverzacija
konverzacija1 = [
    "Zdravo",
    "Zdravo, kako mogu da pomognem?",
    "Koje je vrijeme?",
    "Oprostite, ja sam chat bot i nemam pristup realnom vremenu."
]

konverzacija2 = [
    "Kako se zoveš?",
    "Ja sam Moj ChatBot."
]

# Trening chat bota
trainer.train(konverzacija1)
trainer.train(konverzacija2)

while True:
    user_input = input("Korisnik: ")
    if user_input.lower() == 'kraj':
        break

    response = chatbot.get_response(user_input)
    print(f"ChatBot: {response}")

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
bot = ChatBot(
    "QABot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, I do not understand. Could you rephrase that?",
            "maximum_similarity_threshold": 0.90,
        }
    ],
)
list_trainer = ListTrainer(bot)
list_trainer.train([
    "Good morning! How are you doing?",
    "I am doing very well, thank you for asking.",
    "You're welcome.",
    "Do you like hats?",
])
list_trainer.train([
    "Hello",
    "Hi there!",
    "What is your name?",
    "My name is QABot. I am a chatbot built with ChatterBot.",
    "What can you do?",
    "I can chat with you and answer simple questions.",
])
try:
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english.greetings",
                         "chatterbot.corpus.english.conversations")
except Exception as e:
    print(f"(Skipping corpus training: {e})")

# 4. Terminal chat loop
print("\nQABot is ready. Type 'quit' to exit.\n")
while True:
    try:
        user_input = input("user: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nbot: Goodbye!")
        break

    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit", "bye"):
        print("bot: Goodbye!")
        break

    response = bot.get_response(user_input.lower())
    print(f"bot: {response}")
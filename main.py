from dotenv import load_dotenv

load_dotenv()

print(dotenv_values("env").get("OPENAI_API_KEY"))
print("hello world")
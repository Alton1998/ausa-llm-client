import requests

inputs = {"input": {"question": "Tell me 3 ways given to prevent heart disease", "chat_history": []}}
response = requests.post("http://localhost:8000/invoke", json=inputs)

print(response.text)
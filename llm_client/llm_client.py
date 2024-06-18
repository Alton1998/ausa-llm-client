import requests

inputs = {"input": {"question": "how does maslows triangle help?", "chat_history": []}}
response = requests.post("http://localhost:8000/invoke", json=inputs)

print(response.text)
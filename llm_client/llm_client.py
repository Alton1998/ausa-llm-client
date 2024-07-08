import requests

inputs = {"input": {"question": "What is Heart Disease", "chat_history": []}}
inputs1 = {"input": {"question": "For Patty Johnson get me the last 5 encounters."}}
# response = requests.post("http://localhost:8000/general_info/invoke", json=inputs)
response1 = requests.post("http://localhost:8000/summarize_user_reports/invoke", json=inputs1)
# response = requests.post("http://104.197.203.11:8000/invoke", json=inputs)
# print(response.text)
print(response1.text)
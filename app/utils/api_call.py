import requests
from app.confing import API_KEY, API_END_POINT

HEADERS = {"Content-Type": "application/json",
           "Authorization": f"Bearer {API_KEY}"}


def chat_gpt_query(query):
    return_data = ""
    request_data = {
      "model": "gpt-3.5-turbo",
      "prompt": query,
      "max_tokens": 50,
      "temperature": 0.5,
    }
    response = requests.post(API_END_POINT, headers=HEADERS, json=request_data)
    if response.status_code == 200:
        response_data = response.json()
        for data in response_data.get("choices"):
            print(f"{data.get('text')}")
            return_data = return_data + data.get('text')
    else:
        print(f"Error[{response.status_code}]: {response.json()}")
        return_data = response.json().get("error").get("message")

    return return_data

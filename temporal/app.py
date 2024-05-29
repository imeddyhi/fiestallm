#este código permitirá conectar APIs

import requests
import json

uri = 'http://localhost:11434/api/generate'
data = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
}
response = requests.post(uri, json = data)

response = json.loads(response.text)


print(response['response'])
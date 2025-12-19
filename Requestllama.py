import requests
import json

#setup the base URL for the local Ollama server
url="http://127.0.0.1:11500/api/chat"

#define the payload for the request
payload = {
    "model": "llama2",
    "messages": [
        {"role": "user", "content": "what is python?"}
    ]
}

#send the POST request to the Ollama server with streaming enabled
response = requests.post(url, json=payload, stream=True)
print("Response status code:", response.status_code)
#check if the request was successful
if response.status_code == 200:

    for line in response.iter_lines(decode_unicode=True):
        if line: #ignore empty lines
            
            print("Received line:", line)
            try:
                data = json.loads(line)
                if 'choices' in data:
                    for choice in data['choices']:
                        if 'delta' in choice and 'content' in choice['delta']:
                            print(choice['delta']['content'], end='', flush=True)
            except json.JSONDecodeError:
                print("Failed to decode JSON:", line)   

import ollama

#init ollama client
client = ollama.Client() #(host="http://localhost:11500")


#define the model and the input prompt
model="mario"
prompt="what is python?"

response = client.generate(model=model, prompt=prompt)

print(response)
print("Response from Ollama model:", response.response)
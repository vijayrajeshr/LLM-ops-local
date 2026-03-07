import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3.2"  # Replace with your model name
prompt = input('\nHi Vijay! How can I help you Today ???  : ')

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("\nLlama3.2 Response  :   -----------------------------")
print(response.response)


import requests

# Endpoint și cheie API
endpoint = "" # insert the provided endpoint here
api_key = "" # insert the provided api key here

# Header-ul pentru request
headers = {
    "Content-Type": "application/json",
    "api-key": api_key,
}

# Datele pentru request
data = {
    "messages": [
        {"role": "system", "content": "Tu esti un asistent AI."},
        {"role": "user", "content": "Scrie-mi o poezie de 2 versuri"}
    ]
}

# Trimitere request
response = requests.post(endpoint, headers=headers, json=data)

# Afisare raspuns
result = response.json()
print(result["choices"][0]["message"])
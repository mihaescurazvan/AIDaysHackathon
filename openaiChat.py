import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = "", # insert the provided endpoint here 
  api_key="", # insert the provided api key here  
  api_version="2024-08-01-preview"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Tu esti un asistent AI."},
        {"role": "user", "content": "Scrie-mi o poezie de 2 versuri"}
    ]
)

print(response.choices[0].message.content)
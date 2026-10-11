import requests

while True:
    question = input("Hi, how can I help you? ")
    question = question.lower().strip()

    if question == "exit":
        break

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": question,
                "stream": False
            }
        )

        print(response.json()["response"])

    except:
        print("Something went wrong. Please check if Ollama is running.")
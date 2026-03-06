import ollama


def pass_to_model(text):
    response = ollama.chat(model='gemma3:4b', messages=[{'role' : 'user', 'content': text}])
    return response['message']['content']
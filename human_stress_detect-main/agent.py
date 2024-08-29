import ollama

def tips(query):
    paragraph_buffer = ""  # Initialize a buffer to store paragraph text
    
    response = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': query}],
        stream=True
    )

    for chunk in response:
        paragraph_buffer += chunk['message']['content'] # Add newline for clarity
    

    return paragraph_buffer

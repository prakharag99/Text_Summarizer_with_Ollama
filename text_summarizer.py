import click
import requests
import json

# The Ollama runs on the localhost port number 11434 and below is the url of the api we are using:
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2:0.5b"

def summarize_text(text):

    # Setting a generalized prompt for both text input and file(.txt) input:
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload)
    # Successful generation of the summary:
    if response.status_code == 200:
        result = json.loads(response.text)
        return result['response'].strip()
    # Error:
    else:
        return f"Error: Unable to generate summary. Status code: {response.status_code}"

# Using the click library in Python to take input from comand line.
@click.command()
@click.option('--file', '-f', type=click.File('r'), help='Input text file')
@click.option('--text', '-t', help='Input text')

def main(file, text):
    
    # Input in the form of a text file:
    if file:
        content = file.read()
    # Direct text input from the command line:
    elif text:
        content = text
    else:
        click.echo("Please provide either a file or text input.")
        return
    # Generated summary:
    summary = summarize_text(content)
    click.echo(summary)

if __name__ == '__main__':
    main()
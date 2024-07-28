# Text_Summarizer_with_Ollama

This Text Summarizer is a command line tool to generate summary of given text using the Python's Click library and the Qwen2 0.5B model of Ollama. 
The input can be in the form of a text file or direct text input.

Pre-requisite for running the tool:
--> Download Ollama from the official site according to your Operating System, ie, Windows, Linux or mac.
--> Install Ollama. Note that it is to be run locally on your machine so do not use Jupyter Notebook. Use an IDE like VS Code.
--> Pull the Qwen2 0.5B model of Ollama by writing the following command in the command prompt: 
    ollama pull qwen2:0.5b
--> Make sure it is running on: http://localhost:11434/
--> Install the required Python libraries. In your VS Code terminal, run: pip install click requests

Steps after completing the pre-requisites:
--> Open a terminal in VS Code (Terminal > New Terminal) and make sure you're in the directory containing your script.
--> Run the script using the command line as described:
    For text file as input: python text_summarizer.py --file your_file.txt
    For direct text as input: python text_summarizer.py --text "Your long text goes here."

Next, you will get a very accurate summary of your input in the terminal itself.

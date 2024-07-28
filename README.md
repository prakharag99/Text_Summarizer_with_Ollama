# Text_Summarizer_with_Ollama

This is a command-line tool for summarizing text using the Qwen2 0.5B model hosted locally. The tool can summarize text provided directly as an argument or from a text file.

Features
1. Summarize text from a file.
2. Summarize text provided directly as input.
3. Utilizes the Qwen2 0.5B model for generating summaries.

Requirements
1. Python 3.x
2. requests library and click library
3. Qwen2 0.5B model running locally on http://localhost:11434/

Installation
1. Clone the repository: git clone https://github.com/yourusername/text-summarization-tool.git
2. Install the required Python libraries: pip install requests click
3. Ensure the Qwen2 0.5B model is running locally on http://localhost:11434/.

Usage
1. Summarizing Text from a File: use the --file option followed by the path to the file.
2. Summarizing Direct Text Input: use the --text option followed by your text.

Example commands to use:
1. For summarizing text from a File: python text_summarizer.py --file test.txt
2. For summarizing direct text input: python text_summarizer.py --text "Your long text goes here.

Files:
1. text_summarizer.py: Contains the code and logic used for summarization.
2. test.txt: Contains sample text for summarization.

Acknowledgements
1. Qwen2 0.5B Model
2. Click Library
3. Requests Library




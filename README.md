# AI-Quiz-Generator

AI-powered quiz generator that creates multiple-choice questions (MCQs) from given text using the Groq AI model. Built with Streamlit for an interactive UI.

## Features
- Automatically generates MCQs from input text.
- Supports different difficulty levels (Easy, Medium, Hard).
- Allows users to select and submit answers.
- Displays quiz scores and correct answers.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Groq API
- **Environment Management**: dotenv

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/MananHere576/AI-Quiz-Generator.git
   cd AI-Quiz-Generator
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```
     API_KEY=your_groq_api_key_here
     ```

## Usage

Run the Streamlit app:
```sh
streamlit run quiz_app.py
```

## Project Structure
```
AI-Quiz-Generator/
│── quiz_app.py             # Main Streamlit application
│── requirements.txt   # Python dependencies
│── .env               # Environment variables
│── README.md          # Project documentation
```

## Contributing
Feel free to fork the repository and contribute via pull requests!

## Contact
For queries, reach out via [GitHub Issues](https://github.com/MananHere576/AI-Quiz-Generator/issues).

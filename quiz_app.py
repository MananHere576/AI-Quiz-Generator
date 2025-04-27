import streamlit as st
import json
import os
from dotenv import load_dotenv
from groq import Groq  # Import Groq client

load_dotenv()  # Load environment variables

# Set page title
st.set_page_config(page_title="AI Quiz Generator")

# Initialize Groq client
groq_client = Groq(api_key=os.getenv("API_KEY"))

@st.cache_data
def fetch_questions(text_content, quiz_level, num_questions):
    RESPONSE_JSON = {
        "mcqs": [
            {
                "mcq": "multiple choice question1",
                "options": {
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4",
                },
                "correct": "a"
            }
        ]
    }

    PROMPT_TEMPLATE = f"""
    Text: {text_content}
    You are an expert in generating MCQ quizzes. Create {num_questions} multiple-choice questions based on the text above with {quiz_level} difficulty.
    Ensure the format strictly follows this JSON example:
    {json.dumps(RESPONSE_JSON, indent=4)}
    """

    # Make API request
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE}],
        temperature=0.3,
        max_tokens=1000
    )

    extracted_response = response.choices[0].message.content
    print("Raw API Response:", extracted_response)  # Debugging

    # Parse response
    try:
        parsed_response = json.loads(extracted_response)
        return parsed_response.get("mcqs", [])
    except json.JSONDecodeError as e:
        print("JSON Parsing Error:", str(e))
        return []

def main():
    st.title("Quiz Generator App")
    text_content = st.text_area("Paste the text content here:")
    quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=20, value=3, step=1)

    if "quiz_generated" not in st.session_state:
        st.session_state.quiz_generated = False
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "selected_options" not in st.session_state:
        st.session_state.selected_options = {}

    if st.button("Generate Quiz") or not st.session_state.quiz_generated:
        st.session_state.questions = fetch_questions(text_content, quiz_level, num_questions)
        st.session_state.selected_options = {}
        st.session_state.quiz_generated = True

    if st.session_state.questions:
        st.subheader("Your Quiz:")
        for idx, question in enumerate(st.session_state.questions):
            options = question.get("options", {})
            selected_option = st.radio(
                question["mcq"],
                list(options.values()),
                index=None,
                key=f"q{idx}"
            )
            st.session_state.selected_options[idx] = selected_option

        if st.button("Submit"):
            score = 0
            for idx, question in enumerate(st.session_state.questions):
                options = question.get("options", {})
                correct_answer = options.get(question.get("correct"))
                user_answer = st.session_state.selected_options.get(idx, "Not Answered")
                if user_answer == correct_answer:
                    score += 1
            
            st.subheader(f"🎉 You scored {score} out of {len(st.session_state.questions)}!")
            
            st.subheader("Quiz Results:")
            for idx, question in enumerate(st.session_state.questions):
                options = question.get("options", {})
                correct_answer = options.get(question.get("correct"))
                user_answer = st.session_state.selected_options.get(idx, "Not Answered")

                st.write(f"**{question['mcq']}**")
                st.write(f"✅ Correct Answer: {correct_answer}")
                st.write(f"🎯 Your Answer: {user_answer}")

if __name__ == "__main__":
    main()

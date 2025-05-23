# 🤖 AnyShift AI Screening Assistant

An AI-powered screening assistant that analyzes candidate free-text responses and evaluates their fit for a specific job shift using OpenAI GPT-4 and LangChain.

---

## 📖 Overview

This project automates candidate screening by:

- Parsing open-text candidate responses (skills, availability, location, experience)  
- Extracting key structured info via an LLM prompt  
- Scoring candidate-job fit on a 0-100 scale  
- Providing a brief evaluation and explanation for the score  
- Supporting file uploads or direct copy-paste inputs for easy testing  

Built with **FastAPI** for API and **Streamlit** for a web UI, plus containerized via Docker.

---

## ⚙️ Setup & Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Ashishlathkar77/Anyshift-AI-Screening.git
   cd Anyshift-AI-Screening
   ```

2. **Create a .env file in the root folder with your OpenAI API key:**
   
  ```bash
  OPENAI_API_KEY=your_openai_api_key_here
  ```

3. **Install dependencies (recommended: use a virtual environment):**

  ```bash
  pip install -r requirements.txt
  ```



## 🚀 Running the Project

  FastAPI API Server
  Run the FastAPI backend:
  
  ```bash
  uvicorn api.main:app --reload
  ```

- Open http://localhost:8000/docs to access the interactive API docs.
- You can upload a JSON input file or paste input text directly to the /screen endpoint to get candidate screening results.

## Streamlit Web UI

  Run the Streamlit frontend:

  ```bash
  streamlit run streamlit_app.py
  ```

- Open the provided local URL (usually http://localhost:8501) in your browser.
- You can either upload a JSON file or paste your input JSON directly.
- Click Screen Candidate to get the evaluation and score.


## 🧪 Testing

Use app/sample_input.json or additional test inputs provided in sample_inputs/.

Example output JSON format:

json{
  "score": 92,
  "evaluation": "Great fit!",
  "reasoning": "Meets all requirements and lives nearby. Only concern is evening-only availability."
}

## 🐳 Docker (Optional)

Build and run the Docker container:
    bashdocker build -t screening-assistant .
    docker run -p 8000:8000 --env-file .env screening-assistant
    The API will be accessible at http://localhost:8000.

## 🛠️ How it Works (Summary)

The screen_candidate function uses a LangChain LLMChain with a prompt template that ingests candidate responses and job posting details.
The prompt instructs the LLM to extract information, score the match (0-100), and provide reasoning.
The API and UI serve as wrappers allowing easy user input.
Modular design supports adding more input types or scaling to batch processing.


## 📞 Contact
Feel free to reach out for questions or improvements!
Thank you for checking out the AI Screening Assistant! 🚀

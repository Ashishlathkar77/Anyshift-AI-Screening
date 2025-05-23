🤖 AI Screening Assistant
An AI-powered screening assistant that analyzes candidate free-text responses and evaluates their fit for a specific job shift using OpenAI GPT-4 and LangChain.

📖 Overview
This project automates candidate screening by:

Parsing open-text candidate responses (skills, availability, location, experience)
Extracting key structured info via an LLM prompt
Scoring candidate-job fit on a 0-100 scale
Providing a brief evaluation and explanation for the score
Supporting file uploads or direct copy-paste inputs for easy testing

Built with FastAPI for API and Streamlit for a web UI, plus containerized via Docker.

🗂️ Project Structure
ai_screening_assistant/
├── app/
│   ├── __init__.py
│   ├── screen_candidate.py    # Core LLM screening logic
│   ├── utils.py               # Helpers to load inputs
│   ├── prompt_template.txt    # LLM prompt template
│   └── sample_input.json      # Sample test input
├── main.py                    # FastAPI app entry point
├── streamlit_app.py           # Streamlit UI app
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (OpenAI API key)
├── Dockerfile                 # Containerization setup
└── README.md                  # This file

⚙️ Setup & Installation

Clone the repo:
bashgit clone https://github.com/yourusername/ai_screening_assistant.git
cd ai_screening_assistant

Create a .env file in the root folder with your OpenAI API key:
bashOPENAI_API_KEY=your_openai_api_key_here

Install dependencies (recommended: use a virtual environment):
bashpip install -r requirements.txt



🚀 Running the Project
FastAPI API Server
Run the FastAPI backend:
bashuvicorn main:app --reload

Open http://localhost:8000/docs to access the interactive API docs.
Upload JSON input or paste input text directly to /screen endpoint to get candidate screening results.

Streamlit Web UI
Run the Streamlit frontend:
bashstreamlit run streamlit_app.py

Open the provided local URL (usually http://localhost:8501)
You can either upload a JSON file or paste your input JSON directly.
Click Screen Candidate to get the evaluation and score.


🧪 Testing

Use app/sample_input.json or the additional test inputs provided in sample_inputs/.
The output JSON will include:

json{
  "score": 92,
  "evaluation": "Great fit!",
  "reasoning": "Meets all requirements and lives nearby. Only concern is evening-only availability."
}

🐳 Docker (Optional)
Build and run the container:
bashdocker build -t screening-assistant .
docker run -p 8000:8000 --env-file .env screening-assistant
The API will be accessible at http://localhost:8000.

🛠️ How it Works (Summary)

The screen_candidate function uses a LangChain LLMChain with a prompt template that ingests candidate responses and job posting details.
The prompt instructs the LLM to extract info, score match (0-100), and provide reasoning.
The API and UI serve as wrappers allowing easy user input.
Modular design supports adding more input types or scaling to batch processing.


📞 Contact
Feel free to reach out for questions or improvements!
Thank you for checking out the AI Screening Assistant! 🚀
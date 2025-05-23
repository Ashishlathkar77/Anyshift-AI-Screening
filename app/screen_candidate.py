from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0, model_name="gpt-4")

with open(os.path.join(os.path.dirname(__file__), "prompt_template.txt")) as f:
    TEMPLATE = f.read()

prompt = PromptTemplate(
    input_variables=["name", "responses", "title", "location", "schedule", "requirements"],
    template=TEMPLATE,
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

def screen_candidate(input_data: dict) -> dict:
    candidate = input_data['candidate_responses']
    job = input_data['shift_posting']

    result = llm_chain.run(
        name=candidate["name"],
        responses=json.dumps(candidate["responses"]),
        title=job["title"],
        location=job["location"],
        schedule=job["schedule"],
        requirements="; ".join(job["requirements"])
    )

    return json.loads(result)
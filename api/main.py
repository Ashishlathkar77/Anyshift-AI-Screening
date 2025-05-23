from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import Any
import json

from app.utils import load_input
from app.screen_candidate import screen_candidate

app = FastAPI()

@app.post("/screen_file")
async def screen_file(file: UploadFile = File(...)):
    contents = await file.read()
    input_data = json.loads(contents)
    result = screen_candidate(input_data)
    return result

@app.post("/screen_text")
async def screen_text(json_text: str = Form(...)):
    try:
        input_data = json.loads(json_text)
        result = screen_candidate(input_data)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"status": "OK"}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow your frontend to call it
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    role: str
    requirements: List[str]

@app.post("/evaluate")
def evaluate(data: InputData):
    # Replace this with your LangChain or AI logic
    result = f"Evaluating for role: {data.role} with {len(data.requirements)} requirements."
    return {"response": result}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Allow frontend to connect (CORS)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvaluationRequest(BaseModel):
    job_role: str
    requirements: List[str]  # Accepts list from frontend form

@app.post("/evaluate")
def evaluate(request: EvaluationRequest):
    result = run_genai_evaluation(request.job_role, request.requirements)
    return {"response": result}

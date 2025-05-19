# backend/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cvalign_engine import run_cvalign  # You'll define this in cvalign_engine.py

app = FastAPI()

# Enable CORS to allow frontend requests (e.g. from React app on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected input schema
class JobRequest(BaseModel):
    job_role: str
    requirements: str

# Define the POST endpoint for job evaluation
@app.post("/evaluate")
def evaluate_job(data: JobRequest):
    result = run_cvalign(data.job_role, data.requirements)
    return {"response": result}

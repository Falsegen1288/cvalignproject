@app.post("/evaluate")
def evaluate(request: EvaluationRequest):
    result = run_genai_evaluation(request.job_role, request.requirements)
    
    if "accepted" in result.lower():
        status = "Shortlisted for interview"
    else:
        status = "Rejected"

    return {
        "response": result,
        "status": status
    }

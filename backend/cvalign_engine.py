# backend/cvalign_engine.py

# Adjust these imports to match where you define your vectorstore and llm_chain
from experiment.vectorstore_loader import vectorstore
from experiment.llm_chain_loader import llm_chain

def run_cvalign(job_role: str, requirements: str):
    # Retrieve relevant CVs based on job role
    retrieved_docs = vectorstore.similarity_search(job_role, k=5)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Run through your LLM chain with context, role, and requirements
    response = llm_chain.run({
        "context": context,
        "job_role": job_role,
        "requirements": requirements
    })

    return response

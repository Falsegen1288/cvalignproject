def run_genai_evaluation(job_role: str, requirements: List[str]) -> str:
    query = f"{job_role} - {'; '.join(requirements)}"
    
    retrieved_docs = vectorstore.similarity_search(query, k=5)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    response = llm_chain.run({
        "context": context,
        "job_role": job_role,
        "requirements": "\n".join(requirements)
    })

    return response

import json
from eval_prompt import structured_evaluator
from langchain_core.prompts import ChatPromptTemplate


def evaluate_job(job_posting: dict, profile_data: dict):
    system_prompt = """
    You are an expert executive recruiter and career strategist. 
    Evaluate the candidate's background against the following job posting.
    Be objective: penalize heavily if location requirements or core tool prerequisites are missing.
    Highlight where the candidate's dual expertise in "your field" creates strong leverage.
    """

    # Escape single curly braces by doubling them so LangChain doesn't treat them as template variables
    json_profile_str = json.dumps(profile_data, indent=2).replace("{", "{{").replace("}", "}}")

    user_prompt = f"""
    CANDIDATE PROFILE:
    {json_profile_str}

    JOB POSTING DETAILS:
    Title: {job_posting.get('title')}
    Company: {job_posting.get('company_name')}
    Location: {job_posting.get('location')}
    Description: {job_posting.get('description')}
    """

    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", user_prompt)]
    )

    chain = prompt | structured_evaluator
    return chain.invoke({})

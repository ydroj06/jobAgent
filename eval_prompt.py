import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()


# Define structured output model
class JobEvaluation(BaseModel):
    job_title: str = Field(description="Title of the job")
    company_name: str = Field(description="Name of the hiring company")
    match_score: int = Field(
        description="Overall match score from 0 to 100 based on candidate fit"
    )
    fit_summary: str = Field(
        description="2-3 sentence summary explaining why this job fits or doesn't fit"
    )
    matching_skills: list[str] = Field(
        description="Candidate skills directly relevant to this posting"
    )
    skill_gaps: list[str] = Field(
        description="Key skills or qualifications required that the candidate lacks"
    )
    recommendation: str = Field(
        description="Apply immediately, Consider, or Skip"
    )


# Instantiate the model and evaluator
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_evaluator = llm.with_structured_output(JobEvaluation)
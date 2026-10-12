import json
import os
import time
from dotenv import load_dotenv

# Import functions/classes from your custom modules
from job_fetcher import fetch_job_postings
from job_matching import evaluate_job
from storage_automation import save_matches_to_db

# Load environment variables (.env file containing SERPAPI_API_KEY and OPENAI_API_KEY)
load_dotenv()


def load_profile(file_path: str = "profile.json") -> dict:
    """Loads candidate profile data from a local JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Could not find {file_path}. Ensure it is present in the project directory."
        )

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_pipeline():
    print("🚀 Starting AI Job Search Agent Pipeline...\n")

    # 1. Load Candidate Profile Context
    print("📄 Loading candidate profile...")
    profile = load_profile("profile.json")

    # Extract target queries from profile or fall back to default list
    target_roles = profile.get(
        "target_roles",
        ["Data Analyst", "Sales Operations Manager", "Business Intelligence"],
    )
    location = profile.get("location_preference", "Austin, TX")

    all_evaluated_jobs = []

    # 2. Fetch & Evaluate Jobs per Target Role
    for role in target_roles:
        print(f"\n🔍 Searching for postings matching: '{role}' in '{location}'...")
        raw_jobs = fetch_job_postings(query=role, location=location)
        print(f"   Found {len(raw_jobs)} job postings.")

        for job in raw_jobs:
            job_title = job.get("title", "Unknown Role")
            company = job.get("company_name", "Unknown Company")
            print(f"   ── Evaluating: {job_title} at {company}...")

            try:
                # 3. Pass job and profile context to the evaluation engine
                evaluation_result = evaluate_job(
                    job_posting=job, profile_data=profile
                )
                all_evaluated_jobs.append(evaluation_result)
                # Pause 4 seconds between API calls (keeps you under 15 requests/min)
                time.sleep(4)
            except Exception as e:
                print(f"      ⚠️ Error evaluating job {job_title}: {e}")

    # 4. Save/Automate Storage
    if all_evaluated_jobs:
        print(
            f"\n💾 Saving {len(all_evaluated_jobs)} evaluated postings to database..."
        )
        save_matches_to_db(all_evaluated_jobs)
        print("✅ Pipeline execution completed successfully!")
    else:
        print("❌ No job postings were processed.")


if __name__ == "__main__":
    run_pipeline()
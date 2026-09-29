import requests
import os


def fetch_job_postings(query: str, location: str = "Austin, TX"):
    """Fetches job listings using SerpAPI or a custom job board endpoint."""
    api_key = os.getenv("SERPAPI_API_KEY")
    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_jobs",
        "q": f"{query} {location}",
        "hl": "en",
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data.get("jobs_results", [])
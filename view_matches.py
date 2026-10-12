import duckdb
import pandas as pd

# Set display options so pandas doesn't truncate output columns
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 1000)


def view_stored_jobs():
    # Connect to local database file
    con = duckdb.connect("job_matches.db")

    # Query all records sorted by highest match score
    df = con.execute(
        "SELECT job_title, company_name, match_score, recommendation, fit_summary FROM matches ORDER BY match_score DESC"
    ).df()

    print(f"\n--- TOTAL EVALUATED JOBS: {len(df)} ---\n")
    print(df)

    con.close()


if __name__ == "__main__":
    view_stored_jobs()
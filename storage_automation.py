import duckdb
import pandas as pd


def save_matches_to_db(evaluated_jobs: list):
    con = duckdb.connect("job_matches.db")

    # Convert list of Pydantic objects to DataFrame
    df = pd.DataFrame([job.dict() for job in evaluated_jobs])

    # Store or append to table
    con.execute("CREATE TABLE IF NOT EXISTS matches AS SELECT * FROM df WHERE 1=0")
    con.execute("INSERT INTO matches SELECT * FROM df")

    print(f"Successfully saved {len(df)} records to local DuckDB instance.")
    con.close()
import os

import psycopg


def main() -> None:
    host = os.getenv("POSTGRES_HOST", "")
    port = os.getenv("POSTGRES_PORT", "")
    name = os.getenv("POSTGRES_DB", "")
    user = os.getenv("POSTGRES_USER", "")
    password = os.getenv("POSTGRES_PASSWORD", "")

    conn_info = (
        f"host={host} "
        f"port={port} "
        f"dbname={name} "
        f"user={user} "
        f"password={password}"
    )

    with psycopg.connect(conn_info) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            print(f"Connected to PostgreSQL successfully. Health query result: {result}")
            return

    raise SystemExit("Unable to connect to PostgreSQL after retries.")


if __name__ == "__main__":
    main()

import argparse
import uvicorn

from app.db.init_db import init_db
from app.db.seed import seed_db


def main():
    parser = argparse.ArgumentParser(description="AI Product Agent")
    parser.add_argument("--seed", action="store_true", help="Initialize DB and insert sample data")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    args = parser.parse_args()

    init_db()
    if args.seed:
        seed_db()
        print("✅ Database initialized and seeded.")

    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=True)


if __name__ == "__main__":
    main()

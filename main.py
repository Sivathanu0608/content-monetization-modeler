import os
from src.database import create_database, create_table, load_csv
from src.train_model import train_models


def main():
    print("STEP 1: Creating database...")
    create_database()

    print("STEP 2: Creating table...")
    create_table()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "data", "youtube_data.csv")

    print("STEP 3: Loading CSV...")
    load_csv(csv_path)

    print("STEP 4: Training models...")
    results = train_models()

    print("\nAll models trained successfully")


if __name__ == "__main__":
    main()
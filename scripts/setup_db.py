# scripts/setup_db.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    
    with open('lib/db/schema.sql') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()

    
    from lib.db.seed import seed_data
    seed_data()

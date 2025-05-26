from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    
    authors = ['Chimamanda Ngozi Adichie', 'Haruki Murakami', 'Zadie Smith']
    for name in authors:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))

  
    magazines = [('The New Yorker', 'Literature'), ('National Geographic', 'Science'), ('Rolling Stone', 'Music')]
    for name, category in magazines:
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))

    
    articles = [
        ('Americanah Insights', 1, 1),  
        ('Kafka on the Shore Review', 2, 2), 
        ('White Teeth Analysis', 3, 3) 
    ]
    for title, author_id, magazine_id in articles:
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                       (title, author_id, magazine_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")

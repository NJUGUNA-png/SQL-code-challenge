# lib/models/author.py
from lib.db.connection import get_connection

class Author:
    def __init__(self, name, bio=None, id=None):
        self.id = id
        self.name = name
        self.bio = bio

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO authors (name, bio) VALUES (?, ?)",
                (self.name, self.bio)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE authors SET name = ?, bio = ? WHERE id = ?",
                (self.name, self.bio, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row["name"], row["bio"], row["id"])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row["name"], row["bio"], row["id"])
        return None

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_author(self.id)

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def __repr__(self):
        return f"<Author {self.name} (ID: {self.id}) Bio: {self.bio}>"

# run.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
import ipdb

def main():
    
    author1 = Author(name="John Doe", bio="A passionate writer")
    author1.save()

    magazine1 = Magazine(name="Tech Times", category="Technology")
    magazine1.save()

    article1 = Article(
        title="AI in 2025",
        content="Exciting trends!",
        author_id=author1.id,
        magazine_id=magazine1.id
    )
    article1.save()

    
    found_author = Author.find_by_id(author1.id)
    found_magazine = Magazine.find_by_id(magazine1.id)
    found_article = Article.find_by_id(article1.id)

    print("== Sample Data ==")
    print(found_author)
    print(found_magazine)
    print(found_article)

    ipdb.set_trace()

    if __name__ == "__main__":
        main()

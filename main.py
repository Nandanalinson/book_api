from flask import Flask, jsonify, render_template, request
import requests
import psycopg2

app = Flask(__name__)


API_KEY = "714dca957ba54eb9b6a4c3a9f71586b4"

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/get_similar', methods=['POST'])
def get_similar_books():

    data = request.get_json(silent=True)
    favorite_book = data.get("favorite_book", "").strip()


    headers = {"x-api-key": API_KEY}
    params = {"query": favorite_book, "number": 5}

    response = requests.get("https://api.bigbookapi.com/search-books", headers=headers, params=params)
    response.raise_for_status()

    api_data = response.json()
    books_nested = api_data.get("books", [])
    similar_books = []
    for book_list in books_nested:
        if isinstance(book_list, list) and len(book_list) > 0:
            book = book_list[0] 
            title = book.get("title", "No Title")
            authors = book.get("authors", [])
            author_name = authors[0]["name"] if authors else "Unknown"

            similar_books.append({
                "title": title,
                "author": author_name
            })

    author_name = similar_books[0]["author"] if similar_books else "Unknown"

    connect = psycopg2.connect(database="haiku", 
                        user="myuser",
                        password="mypassword", 
                        host="localhost", port="5433")
    cur = connect.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY,book_name TEXT,author TEXT)")

    add_book = "INSERT INTO books (book_name, author) VALUES (%s, %s)"
    cur.execute(add_book, (favorite_book, author_name))
    cur.execute("""
    CREATE TABLE IF NOT EXISTS similar_books (
    id SERIAL PRIMARY KEY,
    book_name TEXT,
    similar_title TEXT,
    similar_author TEXT)""")

    for item in similar_books:
        cur.execute("INSERT INTO similar_books (book_name, similar_title, similar_author) VALUES (%s, %s, %s)",(favorite_book, item["title"], item["author"]))
    connect.commit()
    connect.close()

    return jsonify({"similar_books": similar_books})


if __name__ == '__main__':
    app.run(debug=True)

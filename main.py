from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

API_KEY = "*****************************"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_similar', methods=['POST'])
def get_similar_books():
    data = request.get_json(silent=True)
    favorite_book = data.get("favorite_book", "").strip()

    if not favorite_book:
        return jsonify({"error": "No book provided"}), 400

    headers = {"x-api-key": API_KEY}
    params = {"query": favorite_book, "number": 5}

    try:
        response = requests.get("https://api.bigbookapi.com/search-books", headers=headers, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": f"API request failed: {e}"}), 500

    api_data = response.json()
    print("API Response:", api_data) 

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

    return jsonify({"similar_books": similar_books})



if __name__ == '__main__':
    app.run(debug=True)

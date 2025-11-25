from flask import Flask, jsonify, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("BOOKS_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.get_json(silent=True)

    book_name = data.get("favorite_book")

    print(f"book name : {book_name}")

    url = "https://api.bigbookapi.com/search-books"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "book_name": book_name,
        "num_recommendations": 5
    }

    response = requests.post(url, json=payload, headers=headers)
 

    return jsonify(response.text)



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.get_json(silent=True)

    book_name = data.get("favorite_book")

    print(f"book name : {book_name}")

    url = f"https://api.bigbookapi.com/book/{book_name}/similar"

    headers = {
        "x-api-key": "714dca957ba54eb9b6a4c3a9f71586b4"
    }

    params = {
        "num_recommendations": 5
    }

    response = requests.get(url, headers=headers, params=params)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

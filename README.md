📚 Books Recommendation API

A simple web application that recommends **5 similar books** based on a user-provided book title.
The project is built using **Flask**, **PostgreSQL**, and a lightweight frontend using **HTML, CSS, and JavaScript**.
It also uses a **Big Books API** dataset to populate book and similarity data.

---

## 🚀 Features

* User enters a **book title** through an HTML form.
* Backend fetches **5 similar books** from PostgreSQL.
* Displays recommended books with their **titles and authors**.
* Clean separation of concerns: Flask API + Books Database + Simple UI.

---

## 🗂️ Database Structure

### **1. books Table**

Stores the master list of books.

| Column    | Type     | Description       |
| --------- | -------- | ----------------- |
| id        | INT (PK) | Unique book ID    |
| book_name | TEXT     | Title of the book |
| author    | TEXT     | Author name       |

### **2. similar_books Table**

Stores similarity relationships generated from Big Books API.

| Column         | Type     | Description                    |
| -------------- | -------- | ------------------------------ |
| id             | INT (PK) | Unique record ID               |
| input_book     | TEXT     | Book provided as input         |
| similar_book   | TEXT     | Recommended book title         |
| similar_author | TEXT     | Author of the recommended book |

---

## ⚙️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS, JavaScript
* **API/Data Source:** Big Books API

---

## 🧠 How It Works

1. The user enters a **book name** in the HTML form.
2. The frontend sends the input to `/get_similar` using **POST (JSON)**.
3. Flask receives the request and queries PostgreSQL:

   ```sql
   SELECT similar_book, similar_author 
   FROM similar_books 
   WHERE input_book = %s 
   LIMIT 5;
   ```
4. Flask returns the top 5 similar books as JSON.
5. JavaScript updates the UI to display the recommendations.

---

## 📁 Project Structure

```
/project
│── app.py
│── templates/
│     └── index.html
│── static/
│     ├── styles.css
│     └── script.js
│── requirements.txt
└── README.md
```

---

## 🔥 API Endpoint

### **POST /get_similar**

Returns 5 similar books.

#### Request Body:

```json
{
  "favorite_book": "Harry Potter"
}
```

#### Response:

```json
{
  "similar_books": [
    {"title": "Percy Jackson", "author": "Rick Riordan"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    ...
  ]
}
```

---

## 🖥️ Running the Project Locally

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2. Set Up PostgreSQL Tables**

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    book_name TEXT,
    author TEXT
);

CREATE TABLE similar_books (
    id SERIAL PRIMARY KEY,
    input_book TEXT,
    similar_book TEXT,
    similar_author TEXT
);
```

### **3. Start Flask**

```bash
python app.py
```

### **4. Open UI**

Visit:

```
http://localhost:5000
```

---

## 📝 Future Improvements

* Add ML-based similarity instead of static API mapping
* Add search suggestions
* Add book covers and ratings
* Deploy to cloud (Render/Heroku)

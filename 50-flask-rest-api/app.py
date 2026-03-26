from flask import Flask, jsonify, request
import uuid
from functools import wraps

app = Flask(__name__)

# Very basic in-memory database
books_db = [
    {"id": "1", "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": "2", "title": "Clean Code", "author": "Robert C. Martin", "year": 2008}
]

# Simple API Key authentication decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # In a real app, this key would be checked against a database of active keys
        api_key = request.headers.get('x-api-key')
        if api_key and api_key == "super-secret-key-123":
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized. Please provide a valid x-api-key header."}), 401
    return decorated_function


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the Flask Library API!",
        "endpoints": {
            "GET /api/books": "List all books",
            "GET /api/books/<id>": "Get a specific book",
            "POST /api/books": "Add a new book (Requires x-api-key header)",
            "DELETE /api/books/<id>": "Delete a book (Requires x-api-key header)"
        }
    })

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({"books": books_db, "total": len(books_db)}), 200

@app.route('/api/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books_db if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route('/api/books', methods=['POST'])
@require_api_key
def add_book():
    request_data = request.get_json()
    
    # Basic validation
    if not request_data or not 'title' in request_data or not 'author' in request_data:
        return jsonify({"error": "Missing required fields: 'title' and 'author'"}), 400
        
    new_book = {
        "id": str(uuid.uuid4())[:8],
        "title": request_data["title"],
        "author": request_data["author"],
        "year": request_data.get("year", "Unknown")
    }
    
    books_db.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

@app.route('/api/books/<book_id>', methods=['DELETE'])
@require_api_key
def delete_book(book_id):
    global books_db
    initial_length = len(books_db)
    books_db = [b for b in books_db if b["id"] != book_id]
    
    if len(books_db) < initial_length:
        return jsonify({"message": f"Book {book_id} deleted successfully."}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    # Running on port 5000 in debug mode for development
    app.run(debug=True, port=5000)

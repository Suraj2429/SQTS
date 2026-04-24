from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

faq = {
    "courses": "We offer Python, AI, and Web Development courses.",
    "fees": "Fees depend on course. Contact us for details.",
    "duration": "Courses range from 3 to 6 months."
}

# DB setup
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        name TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# UI Route
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    for key in faq:
        if key in message:
            return jsonify({"response": faq[key]})

    return jsonify({"response": "Sorry, I didn't understand."})

# Lead API
@app.route("/lead", methods=["POST"])
def lead():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Lead saved!"})

if __name__ == "__main__":
    app.run(debug=True)
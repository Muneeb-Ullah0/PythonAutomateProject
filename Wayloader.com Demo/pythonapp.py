from flask import Flask, render_template_string, request, redirect, flash, session
import sqlite3

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your_database_name'
db = SQLAlchemy(app)
# Database creation
def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add user to the database
def add_user(username, email, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Registration</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <style>
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: url('https://images.unsplash.com/photo-1556761175-4b46a572b786') no-repeat center center/cover;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            display: flex;
            width: 90%;
            max-width: 1000px;
            height: 80vh;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
        }
        .form-container {
            width: 50%;
            background: rgba(255, 255, 255, 0.85);
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            animation: fadeIn 1.5s ease-in-out;
            backdrop-filter: blur(10px);
        }
        .form-container h2 {
            text-align: center;
            color: #333;
            font-size: 24px;
        }
        #map {
            width: 50%;
            height: 100%;
        }
        input, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 16px;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: #0056b3;
        }
        .message {
            text-align: center;
            color: red;
            font-weight: bold;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
                height: auto;
            }
            .form-container, #map {
                width: 100%;
                height: 50vh;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form-container">
            <h2>Register</h2>
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                {% for message in messages %}
                    <p class="message">{{ message }}</p>
                {% endfor %}
              {% endif %}
            {% endwith %}
            <form method="POST">
                <input type="text" name="username" placeholder="Enter Username" required>
                <input type="email" name="email" placeholder="Enter Email" required>
                <input type="password" name="password" placeholder="Enter Password" required>
                <button type="submit">Register</button>
            </form>
        </div>
        <div id="map"></div>
    </div>
    <script>
    var map = L.map('map').setView([33.6844, 73.0479], 10);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    var marker = L.marker([33.6844, 73.0479]).addTo(map);
    </script>
</body>
</html>
"""

# Dashboard Page
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            background: #f4f4f4;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
            display: inline-block;
            border-radius: 10px;
        }
        h1 {
            color: #333;
        }
        .logout {
            padding: 10px 20px;
            background: red;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ username }}</h1>
        <p>You have successfully registered!</p>
        <a href="/logout" class="logout">Logout</a>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if add_user(username, email, password):
            session["username"] = username
            return redirect("/dashboard")
        else:
            flash("❌ Email already registered!")

    return render_template_string(HTML_TEMPLATE)

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/")
    return render_template_string(DASHBOARD_TEMPLATE, username=session["username"])

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    create_database()
    app.run(debug=True)

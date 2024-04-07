import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
import random
from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Example User class


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# This callback is used to reload the user object from the user ID stored in the session


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Function to enumerate a list in Jinja2 template
def my_enumerate(iterable):
    return enumerate(iterable)


@app.context_processor
def utility_processor():
    return dict(my_enumerate=my_enumerate)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Existing login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@login_required
def index():
    """Show Leaderboard"""
    # Fetch all user scores from the database, ordered by score (descending)
    user_scores = db.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
    return render_template("index.html", user_scores=user_scores)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Ensure username and password were submitted
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", message="Please provide both username and password.")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template("login.html", message="Invalid username and/or password.")

        # Create User object and login
        user = User(rows[0]["id"])
        login_user(user)

        # Set user_id in the session
        session["user_id"] = user.id

        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()

    # Clear the user_id from the session upon logout
    session.pop("user_id", None)

    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("username / password is empty")

        if password != confirmation:
            return apology("password do not match confirmation")

        hashed = generate_password_hash(password)
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed
            )
        except:
            return apology("username already exists")
        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/play", methods=["GET", "POST"])
@login_required
def play():
    images_and_answers = {
        "/static/imgs/img1.png": "columnar basalt",
        "/static/imgs/img2.png": "laterite",
        "/static/imgs/img3.png": "angular unconformity",
        "/static/imgs/img4.png": "ripple marks",
        "/static/imgs/img5.png": "dike",
    }

    if request.method == "POST":
        user_guess = request.form.get(
            "user_guess"
        ).lower()  # Convert guess to lowercase for case-insensitive comparison

        selected_image_url = session.get("selected_image_url")
        correct_answer = images_and_answers.get(selected_image_url)

        if user_guess == correct_answer:
            user_id = session["user_id"]

            # Fetch the user's current score from the database
            user_data = db.execute("SELECT score FROM users WHERE id = ?", user_id)
            current_score = user_data[0]["score"]

            # Increment the score by 1 for a correct guess
            updated_score = current_score + 1

            # Update the user's score in the database
            db.execute(
                "UPDATE users SET score = ? WHERE id = ?", updated_score, user_id
            )

            flash(
                "Congratulations! Your guess is correct. Your score has been updated.",
                "success",
            )

        # Generate a new image URL and store it in the session after processing the user's guess
        images_and_answers_keys = list(images_and_answers.keys())
        new_selected_image_url = random.choice(images_and_answers_keys)
        while new_selected_image_url == selected_image_url:
            new_selected_image_url = random.choice(images_and_answers_keys)

        # Store the new selected image URL in the session
        session["selected_image_url"] = new_selected_image_url

    elif "selected_image_url" not in session or session["selected_image_url"] is None:
        images_and_answers_keys = list(images_and_answers.keys())
        selected_image_url = random.choice(images_and_answers_keys)

        # Store the initial selected image URL in the session
        session["selected_image_url"] = selected_image_url

    return render_template("play.html", image_url=session.get("selected_image_url"))


if __name__ == "__main__":
    app.run(debug=True)

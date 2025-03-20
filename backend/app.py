from flask import Flask, render_template, request, redirect, url_for, session
from database import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management
app.config.from_object('config.Config')
db.init_app(app)

# -------------------- Home Route --------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------- User Registration --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        role = request.form["role"]

        new_user = User(username=username, email=email, password_hash=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("login"))

    return render_template("register.html")

# -------------------- User Login --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["username"] = user.username
            session["role"] = user.role
            return redirect(url_for("dashboard"))
        return "Invalid Credentials"

    return render_template("login.html")

# -------------------- User Dashboard --------------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

# -------------------- Reports Page --------------------
@app.route("/reports")
def reports():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("reports.html")

# -------------------- Trading Page --------------------
@app.route("/trade")
def trade():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("trade.html")

# -------------------- Logout --------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------- Run the Application --------------------
if __name__ == "__main__":
    app.run(debug=True)

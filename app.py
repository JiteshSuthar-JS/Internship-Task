# from flask import Flask, redirect, render_template, request
# from flask_sqlalchemy import SQLAlchemy

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

# Secret Key
app.config["SECRET_KEY"] = "your_secret_key"

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -----------------------------
# Flask Login Setup
# -----------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -----------------------------
# Models
# -----------------------------

# User Model (Authentication)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    role = db.Column(db.String(20), default="user")  # user or admin


# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), nullable=False)

    subject = db.Column(db.String(200), nullable=False)

    message = db.Column(db.Text, nullable=False)


# -----------------------------
# Create Database
# -----------------------------
with app.app_context():
    db.create_all()


# -----------------------------
# Routes
# -----------------------------

@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/about')
def About():
    return render_template('about.html')


# -----------------------------
# Register
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists"

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("Home"))
        else:
            return "Invalid username or password"

    return render_template("login.html")


# -----------------------------
# Logout
# -----------------------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# -----------------------------
# Admin Panel (Protected)
# -----------------------------
@app.route("/admin")
@login_required
def admin():

    if current_user.role != "admin":
        return "Access Denied"

    contacts = Contact.query.all()
    users = User.query.all()   # 👈 ADD THIS LINE

    return render_template(
        "admin.html",
        contacts=contacts,
        users=users            # 👈 PASS USERS TO TEMPLATE
    )

# -----------------------------
# Contact Page
# -----------------------------
@app.route('/contact', methods=["GET", "POST"])
def Contact_page():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        db.session.add(new_contact)
        db.session.commit()

        return render_template("contact.html", success=True)

    return render_template("contact.html")


# -----------------------------
# Delete Contact (Admin Only)
# -----------------------------
@app.route("/delete/<int:id>")
@login_required
def delete(id):

    if current_user.role != "admin":
        return "Access Denied"

    contact = Contact.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return redirect("/admin")


# -----------------------------
# Edit Contact (Admin Only)
# -----------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):

    if current_user.role != "admin":
        return "Access Denied"

    contact = Contact.query.get_or_404(id)

    if request.method == "POST":

        contact.name = request.form["name"]
        contact.email = request.form["email"]
        contact.subject = request.form["subject"]
        contact.message = request.form["message"]

        db.session.commit()

        return redirect("/admin")

    return render_template("edit.html", contact=contact)


# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
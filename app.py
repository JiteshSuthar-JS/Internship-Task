from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Create Table (Model)
class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), nullable=False)

    subject = db.Column(db.String(200), nullable=False)

    message = db.Column(db.Text, nullable=False)


# Create DB
with app.app_context():
    db.create_all()


@app.route("/admin")
def admin():
    contacts = Contact.query.all()

    return render_template(
        "admin.html",
        contacts=contacts
    )


@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def Contact_page():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        # Save to DB
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

@app.route("/delete/<int:id>")
def delete(id):

    contact = Contact.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return redirect("/admin")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    contact = Contact.query.get_or_404(id)

    if request.method == "POST":

        contact.name = request.form["name"]
        contact.email = request.form["email"]
        contact.subject = request.form["subject"]
        contact.message = request.form["message"]

        db.session.commit()

        return redirect("/admin")

    return render_template("edit.html", contact=contact)

if __name__ == '__main__':
    app.run(debug=True)
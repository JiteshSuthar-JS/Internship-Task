

## 🎯 About

A simple web application built using Flask and SQLAlchemy that allows users to submit a contact form and provides an admin dashboard to view, edit, and delete submitted messages.

---

## ✨ Features

- 📝 Contact form with POST submission
- 💾 SQLite database using SQLAlchemy ORM
- 🔧 Admin dashboard to view all messages
- ✏️ Edit and delete messages (CRUD operations)
- 🎨 Clean UI using HTML/CSS

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Backend Language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | Web Framework |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=python&logoColor=white) | ORM |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white) | Database |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) | Markup |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) | Styling |

</div>

---

## 📦 Installation
```bash
# 1️⃣ Clone the repository
git clone https://github.com/JiteshSuthar-JS/Internship-Task.git

# 2️⃣ Navigate to project directory
cd Internship-Task

# 3️⃣ Create virtual environment (recommended)
python -m venv venv

# 4️⃣ Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Run the application
python app.py
```

---

## ▶️ Usage

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 🌐 Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Home page |
| `GET/POST` | `/contact` | Contact form |
| `GET` | `/admin` | Admin panel |
| `GET/POST` | `/edit/<id>` | Edit message |
| `POST` | `/delete/<id>` | Delete message |

---

## 📁 Project Structure
```
Internship-Task/
│
├── 📄 app.py                 # Main application file
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
│
├── 📁 static/               # Static files (CSS, JS, images)
├── 📁 templates/            # HTML templates
└── 📁 instance/             # Database files
```

---

## 📧 Contact

**Jitesh Suthar**

[![GitHub](https://img.shields.io/badge/GitHub-JiteshSuthar--JS-181717?style=for-the-badge&logo=github)](https://github.com/JiteshSuthar-JS)

**Project Link:** [https://github.com/JiteshSuthar-JS/Internship-Task](https://github.com/JiteshSuthar-JS/Internship-Task)

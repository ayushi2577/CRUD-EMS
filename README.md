# 🗂️ Employee Management System

> Hire. Edit. Fire. Repeat — all from one sleek page.

A **Flask + MySQL** powered CRUD app to manage employee records with zero friction. No frameworks, no bloat — just clean Python and vanilla JS doing exactly what they need to.

---

## ⚡ Get Running in 60 Seconds

```bash
git clone https://github.com/your-username/CRUD-main.git
cd CRUD-main
pip install -r requirements.txt
```

Set your MySQL credentials:

```bash
export MYSQLHOST=... MYSQLUSER=... MYSQLPASSWORD=... MYSQLDATABASE=... MYSQLPORT=3306
```

```bash
python app.py   # or: gunicorn app:app
```

Visit `http://localhost:5000` — the table creates itself. ✨

---

## 🛠️ What It Does

| Action | How |
|--------|-----|
| ➕ Add employee | Fill the form, hit Add |
| ✏️ Edit inline | Click Edit on any row |
| 🗑️ Delete | One click, gone |
| 🔍 Search & Filter | By name, salary, or join date |
| 💣 Nuke all records | Clear All (with a safety prompt) |

---

## 🏗️ Stack

`Python` · `Flask` · `MySQL` · `Vanilla JS` · `Gunicorn`

```
app.py              ← all the backend magic
templates/crud.html ← the entire frontend, one file
```

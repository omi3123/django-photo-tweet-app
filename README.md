# Django Photo Tweet App 📸🐦

A Django-based microblogging application that allows users to upload photos with descriptions, view them, and delete them — similar to a simple version of Twitter or Instagram.

---

## 📌 Features

- 📝 Create "tweets" with a photo and description  
- 🗑️ Delete existing posts  
- 👁️ View all shared posts in list format  
- 📸 Media file handling for images  
- 🔧 Built with Django MVC (Model-View-Template) structure

---

## 🧠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, Django Templates  
- **Database:** SQLite (default)  
- **Forms:** Django Forms for image & text input  
- **Media Uploads:** Configured for photo uploads via `MEDIA_ROOT` and `MEDIA_URL`

---

## 🧱 Core Concepts Used

- `models.Model` – For defining tweet/photo entries  
- `forms.Form` – For user input with image and text  
- `views.py` – Handles add/view/delete operations  
- `urls.py` – URL routing  
- Templates (`.html`) – Frontend UI  
- Static and Media file handling  
- CRUD operations

---

## 🚀 Setup Instructions

```bash
git clone https://github.com/your-username/django-photo-tweet-app
cd django-photo-tweet-app

# Create virtual environment
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

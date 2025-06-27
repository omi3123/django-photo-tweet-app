📸🐦 **Django Photo Tweet App**

A Django-based **microblogging photo app** that lets users post "tweets" with images and descriptions.  
Inspired by platforms like **Twitter** and **Instagram**, this app allows users to create, view, and delete image-based posts through a clean interface.

---

## 📌 Features

- 📝 Create "Tweets" with a Photo and Description  
- 🗑️ Delete Existing Posts  
- 👁️ View All Shared Posts in List Format  
- 📸 Media File Handling for Image Uploads  
- 🔧 Built with Django MVC (Model–View–Template) Structure

---

## 🧠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, Django Templates  
- **Database:** SQLite (Default)  
- **Forms:** Django Forms for Image & Text Input  
- **Media Uploads:** Handled via `MEDIA_ROOT` and `MEDIA_URL`

---

## 🧱 Core Concepts Used

- `models.Model` – Defines Tweet/Photo Entries  
- `forms.Form` – Handles User Input (Text + Image)  
- `views.py` – Add, View, and Delete Logic  
- `urls.py` – URL Routing and Mapping  
- `.html` Templates – Frontend UI using Django Template Language  
- **Static & Media File Handling**  
- Full **CRUD Operations**

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-photo-tweet-app
cd django-photo-tweet-app
2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Migrations
bash
Copy
Edit
python manage.py migrate
5. Start the Server
bash
Copy
Edit
python manage.py runserver
Now open your browser and visit:
👉 http://127.0.0.1:8000/

🧾 Folder Structure (Example)
csharp
Copy
Edit
django-photo-tweet-app/
├── media/                     # Uploaded images
├── static/                    # Static files (CSS, JS)
├── photoapp/                  # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── manage.py
├── db.sqlite3
└── README.md
👨‍💻 Author
Muhammad Umair Bashir
📧 umairbashir0319@gmail.com

🪪 License
This project is open-source and available for learning, educational, and personal use.
Feel free to modify and share with proper credit.

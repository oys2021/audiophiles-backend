🎧 Audiophile Store API
A Django REST Framework-based backend for an e-commerce audio store. This API provides endpoints to fetch and filter audio products like speakers, headphones, and earphones, as well as create customer orders. the link to the deployed app is https://audiophiles.up.railway.app/ and https://audiophiles.up.railway.app/api/docs/ is the documentation in swagger.

📦 Features
✅ List all products

🆕 Filter new products 

🔊 Category filters: Speakers, Headphones, Earphones

📄 Detailed product view via slug

🛒 Create an order


## 🚀 Technologies Used
- Python 3.11+

- Django 4.x

- Django REST Framework

- Gunicorn (for production)

- Whitenoise (static files)

- PostgreSQL or SQLite

- Railway / Nixpacks (deployment)

---


## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/oys2021/audiophiles-backend.git
cd audiophiles-backend
```

2. **Create & Activate a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate
```


3.**Install Dependencies**
```bash
pip install -r requirements.txt
```

4.**Apply Migrations**
```bash
python manage.py migrate.
Note : connect to your prefered Database before applying migrations.This current code uses Postgresql
```

5. 📘 **Swagger Docs**
Visit http://localhost:8000/api/docs/ for interactive Swagger documentation.

To enable Swagger, make sure you've installed and configured drf-yasg.
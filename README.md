# Poki.al

**Poki.al** is a web platform designed to support parents in the early detection of Autism Spectrum Disorder (ASD) and help them find solutions for everyday challenges. The platform combines a predictive system with a forum to create a supportive environment for families.

🔗 [Live Demo](https://poki-al.vercel.app)


## 🧠 Features

- ✅ **ASD Prediction Tool** – Helps parents assess early signs of ASD in children. ML model was trained on data from AQ-10 Test.
- 💬 **Forum** – Connect with other parents and professionals for discussion and mutual support.


## 🛠 Tech Stack

| Layer       | Tech                        |
|------------|-----------------------------|
| Frontend    | HTML, CSS, JavaScript       |
| Backend     | Python (Django)             |
| Deployment  | Vercel                      |


## 📁 Project Structure

poki-al/ 
├── Doctor/ # Views and models related to the doctor section 
├── Forum/ # Community forum features 
├── Poki/ # Main prediction logic 
├── PokiBase/ # Core app base models and admin 
├── Test/ # For testing purposes 
├── account/ # User authentication and profiles 
├── poki-app/ # Django app settings and URLs 
├── static/ # Static assets (CSS, JS) 
├── staticfiles/ # Collected static files for deployment 
├── templates/ # HTML templates 
├── db.sqlite3 # SQLite database 
├── manage.py # Django entry point 
├── requirements.txt # Python dependencies 
├── runtime.txt # Python version for deployment 
├── vercel.json # Vercel deployment config

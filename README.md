# AI-Based Course Intelligent Recommendation System 🎓🤖

An intelligent, AI-powered learning path and course recommendation platform built with **Django** and **Scikit-Learn**. The system helps learners navigate career domains, discover tailored learning paths, and access curated resources across top learning platforms.

---

## ✨ Features

- **AI-Powered Recommendation Engine**: Utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization and **Cosine Similarity** to match user queries and interests with the best-suited tech domains.
- **Interactive Roadmaps**: Step-by-step learning progression with curated phases, key skills, and learning goals for each domain.
- **Curated Learning Resources**: Direct access to courses on YouTube, Coursera, freeCodeCamp, and GUVI for every domain and milestone.
- **Dynamic Step Explorer**: Interactive modal interface providing focused step breakdowns, learning objectives, and search links.
- **Domain Dashboard**: Overview catalog displaying all available technology tracks, required skills, and course counts.
- **Pre-loaded Database**: Comes pre-configured with 35+ diverse domains across software development, data science, cybersecurity, cloud computing, and more.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12+, Django 5+
- **Machine Learning / NLP**: Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity)
- **Database**: SQLite3
- **Frontend**: HTML5, Modern CSS3 (Dark/Glassmorphism theme), Vanilla JavaScript

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bmega-ai/Ai-based-on-course-intelligent-recommendation-system.git
   cd Ai-based-on-course-intelligent-recommendation-system
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup** (the repo includes `db.sqlite3` with pre-populated domains):
   If you ever want to reset or re-populate the database:
   ```bash
   python manage.py migrate
   python manage.py load_domains
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📂 Project Structure

```
ai_course_rec/
├── manage.py                     # Django management script
├── requirements.txt              # Project dependencies
├── db.sqlite3                    # Pre-loaded SQLite database
├── ai_course_rec/                # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── recommender/                  # Core recommendation app
│   ├── models.py                 # Domain database model
│   ├── views.py                  # Search & detail views
│   ├── services.py               # TF-IDF AI recommendation logic
│   ├── roadmap_data.py           # Detailed milestone descriptions
│   └── management/commands/
│       └── load_domains.py       # Seed script for 35+ domains
├── static/                       # Static assets
│   ├── style.css                 # Base styling & components
│   ├── roadmap.css               # Roadmap tree styling
│   └── js/
│       └── roadmap.js            # Interactive modal & node logic
└── templates/                    # HTML Templates
    ├── home.html                 # Landing & search page
    ├── results.html              # Recommendation search results
    ├── domain_detail.html        # Interactive roadmap view
    └── dashboard.html            # All-domains dashboard
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

# Academic Issue Tracking System (AITS)

AITS is a web-based platform for Makerere University that streamlines the process of reporting, tracking, and resolving academic record issues. It provides a transparent workflow for students, lecturers, and administrators to manage academic concerns efficiently.

---

## 🚀 Features

- **Issue Logging:** Students can submit issues related to courses, grades, or missing records.
- **Issue Tracking:** All users can monitor the real-time status of submitted issues.
- **Role-Based Access:** Students, Lecturers, and Registrars have tailored dashboards and permissions.
- **RESTful API:** Backend powered by Django REST Framework.
- **Modern UI:** Built with React and styled for clarity and usability.
- **Authentication:** Secure login and session management.
- **Statistics:** Lecturers and admins can view issue statistics and summaries.
- **Extensible:** Designed for easy future enhancements (e.g., file uploads, notifications).

---

## 🏗️ Tech Stack

| Component      | Technology                |
| -------------- | ------------------------ |
| Backend        | Django REST Framework    |
| Frontend       | React                    |
| Styling        | CSS                      |
| Database       | SQLite                   |
| Authentication | Django Auth, JWT (planned)|
| Deployment     | Render, Netlify    |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```sh
git clone (https://github.com/CharmiPanchal17/GroupF-Project.git)
cd aits-project
```

### 2. Backend Setup (Django)

```sh
cd backend
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate   # On macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Frontend Setup (React)

```sh
cd ../frontend
npm install
npm start
```

---

## 🎯 Usage

- **Students:** Log in to report academic issues and track their resolution.
- **Lecturers:** View assigned issues, update their status, and provide feedback.
- **Registrar/Admin:** Oversee all reported issues, assign them, and ensure timely resolution.

---

## 📁 Project Structure

```
aits-project/
│
├── backend/      # Django backend (API, models, migrations)
│   └── ...
└── frontend/     # React frontend (components, pages)
    └── ...
```

---

## 🤝 Contributing

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes.
4. Open a pull request.

---

## 📜 License

This project is for educational purposes at Makerere University.

---

## 👥 Authors

- **Group F**
- KOBUMANZI PRISCILLA LINAH 
- BYAMUGISHA ANTHONY  
- KICONCO JULIA  
- IGA AALIYAH 
- PANCHAL CHARMI
- AINAMAANI GRACIOUS


---

## 📌 Notes

- For demo/testing, default credentials may be provided in the backend.
- Planned features: file attachments, notifications, advanced analytics.

---

## 📞 Support

For questions or support, please contact the project maintainers.

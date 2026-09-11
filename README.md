# 🎓 Student Management System

A web-based **Student Management System** built with **Python and Flask**, designed to manage student information, profile photos, and grades through a clean and intuitive interface.

This project was developed as a practical application to explore backend development with Flask, server-side rendering with Jinja2, file uploads, JSON data persistence, and frontend styling with HTML and CSS.

---

## ✨ Features

### 👩‍🎓 Student Management

- Add new students
- View all registered students
- View individual student profiles
- Edit student information
- Delete students
- Prevent duplicate student names
- Validate student names

### 📸 Photo Management

- Upload student profile photos
- Display student photos throughout the system
- Replace existing photos
- Remove student photos
- Support for PNG, JPG, JPEG, and WEBP
- Maximum file size of 4 MB

### 📝 Grade Management

- Add grades to students
- View student grades
- Edit existing grades
- Delete grades
- Validate grades between 0 and 10

### 🎨 User Interface

- Clean and modern interface
- Sidebar navigation
- Student profile pages
- Organized forms
- Visual feedback messages
- Responsive layout
- Custom CSS styling
- Friendly visual elements

---

## 🖥️ Preview

<img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/e15072f2-e178-4cf3-b4e3-f58d2d48cc8b" />


---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend programming |
| 🌶️ Flask | Web framework |
| 🧩 Jinja2 | Server-side HTML templating |
| 🌐 HTML5 | Page structure |
| 🎨 CSS3 | Styling and layout |
| 📄 JSON | Data persistence |
| 📦 Git | Version control |
| 🐙 GitHub | Repository hosting |

---

## 📂 Project Structure

```text
sistema-de-alunos-web/
│
├── app.py
├── alunos.json
│
├── static/
│   ├── style.css
│   └── uploads/
│
├── templates/
│   ├── aluno.html
│   ├── alunos.html
│   ├── cadastrar.html
│   ├── editar.html
│   ├── editar_nota.html
│   ├── index.html
│   └── notas.html
│
└── README.md
```

### Main Files

**`app.py`**

Contains the Flask application and the main backend logic, including routes, student management, grade management, photo uploads, photo deletion, JSON data handling, form validation, and error handling.

**`alunos.json`**

Stores student data, including names, grades, and photo filenames.

**`templates/`**

Contains the HTML templates rendered by Flask using Jinja2.

**`static/style.css`**

Contains the custom styling for the application.

**`static/uploads/`**

Stores uploaded student profile photos.

---

## 🚀 Getting Started

Follow the instructions below to run the project locally.

### Prerequisites

Make sure you have installed:

- Python 3
- Git
- pip

Check your Python installation:

```bash
python3 --version
```

Check your Git installation:

```bash
git --version
```

---

## 📥 Installation

### 1. Clone the repository

Using SSH:

```bash
git clone git@github.com:juliamabel-dev/sistema-de-alunos.git
```

Or using HTTPS:

```bash
git clone https://github.com/juliamabel-dev/sistema-de-alunos.git
```

### 2. Navigate to the project directory

```bash
cd sistema-de-alunos
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Linux / WSL:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the application

```bash
python app.py
```

The application will start locally.

Open your browser and access:

```text
http://127.0.0.1:5000
```

---

## 🧭 Application Navigation

The application is organized into three main sections:

### 🏠 Home

<img width="1917" height="903" alt="image" src="https://github.com/user-attachments/assets/8602459a-a033-4f92-ade9-dcde1e138808" />

The home page provides access to the main features of the system.

### 👩‍🎓 Students

<img width="1917" height="907" alt="image" src="https://github.com/user-attachments/assets/3cd04381-ffad-4a67-9974-6dc1901629bd" />

The students section allows users to:

- View all students
- Open individual student profiles
- Add new students
- Edit student information
- Delete students
- Add or replace profile photos
- Remove profile photos

### 📝 Grades

<img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/785bd28f-fcdd-43e0-82b9-c37d7ab95577" />


The grades section allows users to:

- Add grades
- View grades
- Edit grades
- Delete grades
- Validate grades between 0 and 10

---

## 🔄 Student Workflow

```text
Add Student
     │
     ▼
Student Profile
     │
     ├── Edit Information
     │
     ├── Add / Replace Photo
     │
     ├── Remove Photo
     │
     └── Manage Grades
              │
              ├── Add Grade
              ├── Edit Grade
              └── Delete Grade
```

---

## 📸 Photo Management

The application includes a file upload system for student profile photos.

Supported formats:

```text
PNG
JPG
JPEG
WEBP
```

Maximum file size:

```text
4 MB
```

When a new photo replaces an existing photo, the previous file is removed from the uploads directory.

Photos can also be removed independently from a student's profile.

---

## 📝 Grade Validation

Grades are validated before being saved.

<img width="1917" height="905" alt="image" src="https://github.com/user-attachments/assets/3364db28-903a-424f-9c41-14a78a87f2af" />


The accepted range is:

```text
0.0 → 10.0
```

Values outside this range are rejected by the application.

---

## 💾 Data Storage

The current version uses a JSON file for data persistence:

```text
alunos.json
```

Each student can contain information such as:

```json
{
    "nome": "Example Student",
    "foto": "example.png",
    "notas": [
        9.0,
        8.5
    ]
}
```

This approach keeps the project simple and easy to understand while developing the application's core functionality.

---

## 🔐 Data & Security

The project currently uses local JSON storage and local file uploads.

The repository contains **fictional student data and images** for development and demonstration purposes.

For a production environment, additional security measures would be required, including:

- User authentication
- Authorization
- Secure file handling
- Database security
- Input sanitization
- Protection of personal information
- Secure deployment configuration

---

## 🧪 Project Status

### Completed

- [x] Dashboard with statistics
- [x] Student registration
- [x] Student listing
- [x] Student profiles
- [x] Student editing
- [x] Student deletion
- [x] Student filtering
- [x] Student photo upload
- [x] Student search
- [x] Photo replacement
- [x] Photo removal
- [x] Grade averages
- [x] Grade registration
- [x] Grade editing
- [x] Grade deletion
- [x] Grade validation
- [x] Form validation
- [x] Custom interface
- [x] Git version control
- [x] GitHub repository

---

## 🔮 Future Improvements

Possible future improvements include:

- [ ] User authentication
- [ ] Login system
- [ ] Different user roles and permissions
- [ ] Database integration
- [ ] Sorting options
- [ ] Academic performance charts
- [ ] Improved mobile responsiveness
- [ ] Automated testing
- [ ] Production deployment
- [ ] Cloud storage for uploaded images

---

## 🎯 Project Goals

The main goals of this project are to practice and demonstrate:

- Python programming
- Flask application development
- Backend development
- Routing
- HTTP methods
- HTML forms
- Server-side rendering
- Jinja2 templates
- File uploads
- Data validation
- JSON data persistence
- CRUD operations
- Frontend styling
- Git and GitHub workflows

---

## 📚 What I Learned

Through this project, I practiced building a complete web application from the backend to the user interface.

Some of the main concepts explored were:

- Creating Flask routes
- Handling `GET` and `POST` requests
- Processing HTML forms
- Rendering dynamic pages with Jinja2
- Managing uploaded files
- Updating and deleting stored data
- Working with JSON files
- Validating user input
- Structuring a Flask project
- Using virtual environments
- Managing versions with Git
- Working with GitHub and SSH

---

## 💻 Development Environment

The project was developed using:

```text
Python
Flask
Jinja2
HTML5
CSS3
WSL
Git
GitHub
```

---

## 🤝 Contributing

This project was created as a personal learning and development project.

Suggestions, ideas, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📄 License

This project is currently intended for educational and portfolio purposes.

---

## 👩‍💻 Author

### Julia Mabel

Personal project developed to practice **Python, Flask, web development, Git, and GitHub workflows**.

---

⭐ If you found this project interesting, feel free to explore the code and follow its development!

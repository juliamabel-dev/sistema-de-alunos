# Student Management System

A web-based student management system built with Python and Flask, designed to manage student information, profile photos, and grades through a clean and intuitive interface.

## Features

### Student Management

- Add new students
- View all registered students
- View individual student profiles
- Edit student information
- Delete students
- Prevent duplicate student names
- Validate student names

### Photo Management

- Upload student profile photos
- Display student photos throughout the system
- Replace existing photos
- Remove student photos
- Support for PNG, JPG, JPEG, and WEBP
- Maximum file size of 4 MB

### Grade Management

- Add grades to students
- View student grades
- Edit existing grades
- Delete grades
- Validate grades between 0 and 10

### User Interface

- Clean and modern interface
- Sidebar navigation
- Student profile pages
- Organized forms
- Visual feedback messages
- Responsive layout

## Preview

<img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/e15072f2-e178-4cf3-b4e3-f58d2d48cc8b" />

## Technologies

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| Jinja2 | Server-side HTML templating |
| HTML5 | Page structure |
| CSS3 | Styling and layout |

## Project Structure

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

**`app.py`** — contains the Flask application and backend logic, including routes, student and grade management, photo uploads, form validation, and error handling.

**`alunos.json`** — stores student data, including names, grades, and photo filenames.

**`templates/`** — contains the HTML templates rendered by Flask using Jinja2.

**`static/style.css`** — contains the custom styling for the application.

**`static/uploads/`** — stores uploaded student profile photos.

## Getting Started

Requirements: Python 3 and pip.

Clone the repository, then run:

```bash
cd sistema-de-alunos
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install flask
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Application Navigation

The application is organized into three main sections:

### Home

The home page provides access to the main features of the system.

### Students

Allows users to view all students, open individual profiles, add new students, edit information, delete students, and add, replace, or remove profile photos.

### Grades

Allows users to add, view, edit, and delete grades, with validation accepting only values between 0 and 10.

## Student Workflow

```text
Add Student
     │
     ▼
Student Profile
     ├── Edit Information
     ├── Add / Replace Photo
     ├── Remove Photo
     └── Manage Grades (Add / Edit / Delete)
```

## Photo Management

The application includes a file upload system for student profile photos. Supported formats:

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

When a new photo replaces an existing photo, the previous file is removed from the uploads directory. Photos can also be removed independently from a student's profile.

## Data Storage

Data is persisted in a local file:

```text
alunos.json
```

Each student can contain information such as:

```json
{
    "nome": "Example Student",
    "foto": "example.png",
    "notas": [9.0, 8.5]
}
```

The repository contains fictional student data for demonstration purposes. A production environment would require authentication, authorization, secure file handling, database security, and input sanitization.

## Project Status

### Completed

- [x] Dashboard with statistics
- [x] Student registration, listing, profiles, editing, and deletion
- [x] Student filtering and search
- [x] Photo upload, replacement, and removal
- [x] Grade registration, editing, deletion, averages, and validation
- [x] Form validation
- [x] Custom interface

### Future Improvements

- [ ] User authentication and login
- [ ] User roles and permissions
- [ ] Database integration
- [ ] Sorting options
- [ ] Academic performance charts
- [ ] Improved mobile responsiveness
- [ ] Automated testing
- [ ] Production deployment
- [ ] Cloud storage for uploaded images

## Author

**Julia Mabel** — a personal project developed to practice Python and Flask web development.
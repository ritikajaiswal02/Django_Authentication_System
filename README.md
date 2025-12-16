# Django Auth Project

This project is a simple Django-based authentication system with user registration, login, and logout functionality. It demonstrates basic user management and email-based password delivery.

## Features
- User registration with email-based password delivery
- User login and logout
- Home page with personalized welcome message
- Simple, clean UI with navigation

## Project Structure
```
├── manage.py
├── db.sqlite3
├── auth_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── auapp/
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── ulogin.html
│   │   └── usignup.html
│   └── ...
├── templates/
│   └── base.html
├── static/
│   └── css/
│       └── mystyle.css
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   - Ensure you have Python and Django installed
   - Install Django: `pip install django`
3. **Configure Email Backend**
   - Update email settings in `settings.py` for production use
4. **Run migrations**
   - `python manage.py migrate`
5. **Start the development server**
   - `python manage.py runserver`
6. **Access the app**
   - Visit `http://127.0.0.1:8000/` in your browser

## Usage
- **Sign Up:** Register with your email. A random password will be sent to your email.
- **Login:** Use your email and the received password to log in.
- **Logout:** Click the logout link in the navigation bar.

## File Overview
- `auapp/views.py`: Contains logic for home, signup, login, and logout
- `auapp/templates/`: HTML templates for the app
- `templates/base.html`: Base template with navigation
- `static/css/mystyle.css`: Basic styling
- `auth_project/settings.py`: Django settings
- `auth_project/urls.py`: URL routing

## Notes
- This project uses Django's built-in User model.
- Passwords are randomly generated and sent via email (configure email backend for production).
- For demonstration only; not production-ready without further security and configuration.

## License
MIT License

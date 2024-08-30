# News Portal

This project is a simple news portal built using Python and Flask. The portal allows users to view news articles by categories, add new news articles, and view details of each article.

## Features

- View all news on the homepage.
- Filter news by categories.
- Detailed view for individual news articles.
- Add new news articles.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** SQLite with SQLAlchemy ORM
- **HTML Templating:** Jinja2
- **Form Handling:** Flask-WTF

## Installation & Setup

### 1. Clone the repository:

```commandline
git clone https://github.com/yourusername/news-portal.git
cd news-portal
```
### 2. Set up a virtual environment:

```commandline
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```
### 3. Install the dependencies:

```commandline
pip install -r requirements.txt
```

### 4. Initialize the database:

```commandline
flask shell
>>> from main import db
>>> db.create_all()
>>> exit()
```

### 5. Run the application:

```commandline
flask run
```

Access the portal at http://127.0.0.1:5000 in your web browser.

## Project Structure

- **main.py:** Core application logic, including routing and database models.
- **templates/:** HTML templates for different pages.
- **static/:** Static assets like CSS and JS files.
- **db.sqlite3:** SQLite database file.
- **requirements.txt:** List of Python dependencies.

## Usage

- **Homepage:** Displays a list of all news articles.
- **Add News:** Use the form to add a new news article, selecting a category.
- **Category View:** View all news articles within a specific category.
- **News Details:** View detailed information for a specific news article.


## Author
Developed by [iwannafly69](https://github.com/1sten)

- Email: iwannafly666@yandex.ru
- GitHub: [iwannafly69](https://github.com/iwannafly69)

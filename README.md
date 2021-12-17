# Movie Watchlist API

Movie Watchlist API built using Flask & SQLAlchemy, and validated with Postman. Movie metadata is provided by IMDb API.

## Getting Started

Essential Downloads:

Python 3.8 - https://www.python.org/downloads/
Postman - https://www.postman.com/downloads/
XAMPP - https://www.apachefriends.org/index.html

FAQs:

IMDbPY - https://imdbpy.readthedocs.io/en/latest/faqs.html

## Project Organization

```
Movie-API-Project
├─ .gitignore
├─ IMDb_query.py
├─ MovieApp.py
├─ MovieDB
│  ├─ movies_database.db
│  ├─ SetupDB.py
│  └─ __init__.py
├─ README.md
└─ templates
   ├─ create.html
   ├─ edit.html
   └─ read.html

```

## How to run

Run MovieApp.py -> Go to browser and enter http://127.0.0.1:5000/ (default)

View Current Movie List: Go to http://127.0.0.1:5000/read <br />
Add New Movie: Go to http://127.0.0.1:5000/create <br />
Delete Movie: Click on movie title -> Press delete <br />



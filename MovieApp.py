from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Import from your custom module
from MovieDB.SetupDB import Movie
import IMDb_query

# Connect to the database
engine = create_engine("sqlite:///MovieDB//movies_database.db")

# Basic Flask imports
from flask import Flask, request, redirect, url_for, render_template
# Initialize Flask
app = Flask(__name__)

# # routing for creating new records (the 'C' in CRUD)
# @app.route("/")
# def landing():
#     return render_template("read.html")

# routing for creating new records (the 'C' in CRUD)
@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/createmovie", methods = ["POST", "GET"])
def createMovie():
    
    if request.method == "POST":
        # Get the data from the form and placed into a variable. 
        input_data = request.form
        
        # A new session will have to be created in every function
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # create a new movie and enter it into the database
        #new_movie = Movie(title = input_data["name"], rating = input_data["rating"])

        # Access IMDb for movie data
        movie_data = IMDb_query.find_movie(input_data["name"])
        new_movie = Movie(title = movie_data['title'], rating = movie_data['rating'])
        session.add(new_movie)
        session.commit()
        session.close()
        return redirect(url_for("read"))
    
    else:
        return redirect(url_for("create"))

# Routing for simply reading the database (the 'R' in CRUD)
@app.route("/read")
def read():
    
    # Start this page's session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all results from the database
    query = session.query(Movie).all()
    
    # render the template and pass the query into the html
    return render_template("read.html", query = query)

# Routing for editing a movie, including deletion (the 'U' and 'D' in CRUD)
@app.route("/movie/<movie_id>")
def edit(movie_id):
    
    # Start this page's session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    # Query the movie based on the id
    query = session.query(Movie).filter(Movie.movie_id == movie_id).one()    
    
    session.close()
    
    # Render the html with the query passed through it
    return render_template("edit.html", query = query)

# Routing to actually update the movie
@app.route("/editmovie/<movie_id>", methods = ["POST", "GET"])
def editMovie(movie_id):
    
    if request.method == "POST":
        # Get the data from the form and placed into a variable. 
        input_data = request.form
        
        # A new session will have to be created in every function
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        
        # Search for the movie to change based on the movie id
        query = session.query(Movie).filter(Movie.movie_id == movie_id).one()  
        
        # Write the changes to the database
        query.title = input_data["name"]
        query.rating = input_data["rating"]
        session.commit()
        session.close()
        return redirect(url_for("read"))
    
    else:
        return redirect(url_for("read"))

# Routing for deleting a movie
@app.route("/deletemovie/<movie_id>", methods = ["POST", "GET"])
def deleteMovie(movie_id):
    if request.method == "POST":
        
        # A new session will have to be created in every function
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        
        # Search for the movie to change based on the movie id
        query = session.query(Movie).filter(Movie.movie_id == movie_id).one()
        
        # Delete the row
        session.delete(query)
        session.commit()
        session.close()
        
        return redirect(url_for("read"))
        
    else:
        return redirect(url_for("read"))

if __name__ == '__main__':
    app.run()
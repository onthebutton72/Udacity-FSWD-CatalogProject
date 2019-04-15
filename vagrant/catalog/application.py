from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql:///catalog')
metadata = MetaData()

Genres = Table('genres', metadata, autoload=True, autoload_with=engine)
Movies = Table('movies', metadata, autoload=True, autoload_with=engine)

DBSession = sessionmaker(bind=engine)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()

app = Flask(__name__)

@app.route('/')
@app.route('/genres/<int:genre_id>/')
def genreMenu(genre_id):
	genres = session.query(Genres).filter_by(id=genre_id).one()
	movies = session.query(Movies).filter_by(genre_id = genre_id)
	output = ''
	for i in movies:
		output += i.title
		output += '</br>'
	return output


#Create a route for newMovieItem function
@app.route('/genres/<int:genre_id>/new/')
def newMovieItem(genre_id):
	return "page to create a new movie item.  Task 1 complete!"


#Create a route for editMovieItem function
@app.route('/genres/<int:genre_id>/<int:movie_id>/edit/')
def editMovieItem(genre_id, movie_id):
	return "page to edit a new movie item.  Task 2 complete!"


@app.route('/genres/<int:genre_id>/<int:movie_id>/delete/')
def deleteMovieItem(genre_id, movie_id):
	return "page to delete a new movie item.  Task 3 complete!"


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
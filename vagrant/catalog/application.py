from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

Base = automap_base()
engine = create_engine('postgresql:///catalog')
Base.prepare(engine, reflect=True)
Genres = Base.classes.genres
Movies = Base.classes.movies
session = Session(engine)

@app.route('/')
@app.route('/genres/<int:genre_id>/')
def genreMenu(genre_id):
	genres = session.query(Genres).filter_by(id=genre_id).one()
	movies = session.query(Movies).filter_by(genre_id = genre_id)
	return render_template('menu.html', genres=genres, movies=movies)


#Create a route for newMovieItem function
@app.route('/genres/<int:genre_id>/new/', methods=['GET', 'POST'])
def newMovieItem(genre_id):
	if request.method == 'POST':
		newMovie = Movies(title = request.form['name'], genre_id = genre_id)
		session.add(newMovie)
		session.commit()
		return redirect(url_for('genreMenu', genre_id = genre_id))
	else:
		return render_template('newmovieitem.html', genre_id = genre_id)


#Create a route for editMovieItem function
@app.route('/genres/<int:genre_id>/<int:movie_id>/edit/')
def editMovieItem(genre_id, movie_id):
	return "page to edit a new movie item.  Task 2 complete!"

#Create a route for deleteMovieItem function
@app.route('/genres/<int:genre_id>/<int:movie_id>/delete/')
def deleteMovieItem(genre_id, movie_id):
	return "page to delete a new movie item.  Task 3 complete!"


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
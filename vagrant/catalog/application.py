from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask_marshmallow import Marshmallow #pip install flask-marshmallow, pip install marshmallow-sqlalchemy

app = Flask(__name__)

Base = automap_base()
engine = create_engine('postgresql:///catalog')
Base.prepare(engine, reflect=True)
Genres = Base.classes.genres
Movies = Base.classes.movies
session = Session(engine)
ma = Marshmallow(app)

class GenreSchema(ma.ModelSchema):
	class Meta:
		model = Genres

class MovieSchema(ma.ModelSchema):
	class Meta:
		model = Movies

@app.route('/')

@app.route('/catalog/')
def mainMenu():
	genres = session.query(Genres)
	return render_template('catalog.html', genres=genres)


#JSON Endpoints
@app.route('/catalog/<int:genre_id>/JSON/')
def oneGenreJSON(genre_id):
	genres = session.query(Genres).filter_by(id=genre_id).one()
	movies = session.query(Movies).filter_by(genre_id = genre_id).all()
	genre_schema = GenreSchema()
	movie_schema = MovieSchema(many=True)
	output = movie_schema.dump(movies).data
	return jsonify({'Genre_JSON' : output})


@app.route('/catalog/JSON/')
def allMoviesJSON():
	genres = session.query(Genres).all()
	movies = session.query(Movies).all()
	genre_schema = GenreSchema(many=True)
	movie_schema = MovieSchema(many=True)
	output = movie_schema.dump(movies).data
	return jsonify({'All_Movies_JSON' : output})

#Catalog Genre Menu
@app.route('/catalog/<int:genre_id>/')
def genreMenu(genre_id):
	genres = session.query(Genres).filter_by(id=genre_id).one()
	movies = session.query(Movies).filter_by(genre_id = genre_id)
	return render_template('menu.html', genres=genres, movies=movies)


#Create a route for newMovieItem function
@app.route('/catalog/<int:genre_id>/new/', methods=['GET', 'POST'])
def newMovieItem(genre_id):
	if request.method == 'POST':
		newMovie = Movies(title = request.form['title'], description = request.form['description'], genre_id = genre_id)
		session.add(newMovie)
		session.commit()
		flash("new movie created!")
		return redirect(url_for('genreMenu', genre_id = genre_id))
	else:
		return render_template('newmovieitem.html', genre_id = genre_id)


#Create a route for editMovieItem function
@app.route('/catalog/<int:genre_id>/<int:movie_id>/edit/', methods=['GET', 'POST'])
def editMovieItem(genre_id, movie_id):
	editedItem = session.query(Movies).filter_by(id = movie_id).one()
	if request.method == 'POST':
		if request.form['title']:
			editedItem.title = request.form['title']
		if request.form['description']:
			editedItem.description = request.form['description']
		session.add(editedItem)
		session.commit()
		flash("movie has been edited!")
		return redirect(url_for('genreMenu', genre_id = genre_id))
	else:
		return render_template('editmovieitem.html', genre_id = genre_id
			, movie_id = movie_id, i = editedItem)


#Create a route for deleteMovieItem function
@app.route('/catalog/<int:genre_id>/<int:movie_id>/delete/', methods=['GET', 'POST'])
def deleteMovieItem(genre_id, movie_id):
	itemToDelete = session.query(Movies).filter_by(id = movie_id).one()
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		flash("movie has been deleted!")
		return redirect(url_for('genreMenu', genre_id = genre_id))
	else:
		return render_template('deletemovieitem.html', i = itemToDelete)


if __name__ == '__main__':
	app.secret_key = 'mykey'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
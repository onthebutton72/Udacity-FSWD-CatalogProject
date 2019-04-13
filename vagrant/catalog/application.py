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
@app.route('/movies')
def getData():
	genres = session.query(Genres)[1]
	movies = session.query(Movies).filter_by(genre_id = genres.id)
	output = ''
	for i in movies:
		output += i.title
		output += '</br>'
	return output

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
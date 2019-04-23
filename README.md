# Udacity FSWD Catalog Project

This is the catalog project for the Udacity Full Stack Web Developer Nanodegree.  This project involves creating a website that displays a list of items within a variety of categories as well as providing a user registration and authentication system.  Registered users have the ability to post, edit and delete their own items.

## Table of Contents

* [Contents](#contents)
* [Attribution](#attribution)
* [Instructions](#instructions)
* [Dependencies](#dependencies)
* [Creator](#creators)

## Contents

*  All html and python files are located in the /vagrant/catalog/templates folder
    - HTML: catalog.html, deletemovieitem.html, editmovieitem.html, item.html, movies.html, newmovieitem.html
    - Python: database_setup.py, application.py

*  CSS files are located in the /vagrant/catalog//static folder
    - CSS: styles.css

## Attribution

*  Help with CSS from [w3schools](http://www.w3schools.com)
*  Converting Flask-SQLAlchemy to JSON with [Flask-Marshmallow](https://www.youtube.com/watch?v=kRNXKzfYrPU)

## Instructions

* Clone or download the repository: https://github.com/onthebutton72/fswd-catalog.git
* Change directory to the cloned/downloaded folder 
* Change directory to the vagrant/catalog folder: ```cd vagrant/catalog```
* Install [Virtualbox](https://www.virtualbox.org/)
* Install Vagrant VM: ```vagrant up```
* SSH to the Vagrant VM: ```vagrant ssh```
* Change directory to the vagrant/catalog folder: ```cd vagrant/catalog```
* Install Marshmallow: ```pip install flask-marshmallow marshmallow-sqlalchemy``` (If you receive error you may need to 
* ```sudo pip install```)
* Run the database_setup.py file: ```python database_setup.py```
* Run the application.py file: ```python application.py```
* Access the application by visiting http://localhost:5000 locally



## Dependencies

* This project was created with the Flask micro framework [Flask](http://flask.pocoo.org/)
* Browser: Best viewed in Google Chrome (javascript enabled)
* Google+ API

## Creators

* Jamie Martinez

## movie-catalog
movie-catalog is a REST API and a very simple web application where you can search for movies and create movie playlists! It is based on [MovieLens 1M Dataset](https://grouplens.org/datasets/movielens/1m/)

### Setting up

#### Prerequisites
* PostgreSQL

#### Setting up the environment

It is suggested to install the requirements to an isolated python environment.

##### Step 1: Create virtual environment (Optional, but suggested):
POSIX
```
python3 -m venv /path/to/myenv
source /path/to/myenv/Scripts/activate.bat
```
Windows
```
python -m venv \path\to\myenv
\path\to\myenv\Scripts\activate.bat
```
##### Step 2: Install requirements
```
pip install -r requirements.txt
```
##### Step 3: Run the migrations
It is necessary to run the migrations to create the tables and load the initial data into the tables.
```
python movie_catalog/manage.py migrate
```
##### Step 4: Run the web server
Now, it is time to run the web server and start the API! Run the following command and development server will start at http://127.0.0.1:8000
```
python movie_catalog/manage.py runserver
```
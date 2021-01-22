# cyphergen-web

Cypher character generator for custom settings

Present a website and API which allows GMs for the Cypher System RPG
to create settings, that players can then use to create Level 1
characters.

## Local Development

### Configure Python

Run the following commands to setup your Python environment.

    python -m venv venv
    pip install -r requirements.txt
    cp default.env .env

### Environment File

Set environment variables in `.env`

    FLASK_APP=cyphergen
    FLASK_ENV=decvelopment
    FLASK_DEBUG=0

Set the Flask environment variables. FLASK_APP is required.

    BASEURI=http://localhost:5000

Base URI of the application

    REDIS_URL=redis://:password@hostname:6379

Connection string for Redis.

### Start the Server

     flask run

## Deploy on Heroku

    heroku create
    heroku addons:create heroku-redis:hobby-dev
    git push heroku main

Note that this will provide REDIS_URL for you. You do not need to specify
anything in `.env` as the defaults provided by Heroku will be adequate. Note 
that the hobby-dev tier does not provide persistence. Data will be wiped every
time the app reloads.

Note that redis is not the ideal backend database for a service such as
this one, however since this is a hobby project, scalability is not as
large a concern as accessibility. The Character and Game classes must
be adjusted to change to a more appropriate backend, such as MongoDB.

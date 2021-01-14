# cyphergen-web
Cypher character generator for custom settings

Present a website and API which allows GMs for the Cypher System RPG 
to create settings, that players can then use to create Level 1 
characters.

## Development
Run the following commands to setup your Python environment.

    python -m venv venv
    pip install -r requirements.txt
    cp default.env .env

## Environment File
Set environment variables in `.env`

    FLASK_APP=cyphergen
    FLASK_ENV=decvelopment
    FLASK_DEBUG=0

Set the Flask environment variables.  FLASK_APP is required.

    BASEURI=http://localhost:5000

Base URI of the application

    APIPATH=/api/v1

Path at which to publish the API endpoint

    REDIS_URL=

Connection strong for Redis (only specify if not already provided by
the deployment platform, as with the Heroku directions below.)

## Deploy on Heroku

    heroku create
    heroku addons:create heroku-redis:hobby-dev
    git push heroku main

Note that this will provide REDIS_URL for you.  You do not need to specify
REDIS_URL in `.env`.  Note that the hobby-dev tier does not provide 
persistence.  Data will be wiped every time the app reloads.

Note that redis is not the ideal backend database for a service such as 
this one, however since this is a hobby project, scalability is not as
large a concern as accessibility.  The Character and Game classes must 
be adjusted to change to a more appropriate backend, such as MongoDB.

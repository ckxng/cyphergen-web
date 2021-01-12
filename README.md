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

    DBCONN=mongodb://abc@xyz:123/foo

Database connection string to a MongoDB
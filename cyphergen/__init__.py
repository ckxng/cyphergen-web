import os
from flask import Flask, jsonify, request
from . import helper
from . import character
from . import game

app = Flask(__name__)
app.config.from_mapping(
    DBCONN = os.environ.get('DBCONN'),
    BASEURI = os.environ.get('BASEURI') or '',
    APIPATH = os.environ.get('APIPATH') or '/api/v1'
)
app.helper = helper.Helper(app)

@app.route(app.helper.path('/games'))
def get_games():
    return jsonify({
        'games': [
            app.helper.uri("/games/1"),
            app.helper.uri("/games/2"),
            app.helper.uri("/games/3")
        ]
    })

@app.route(app.helper.path('/games/<id>'))
def get_game(id):
    return jsonify({
        'game': {
            'id': app.helper.uri('/games/'+id),
            'campaign' : game.Game().campaign
        }
    })

@app.route(app.helper.path('/characters'))
def get_characters():
    return jsonify({
        'games': [
            app.helper.uri("/character/1"),
            app.helper.uri("/character/2"),
            app.helper.uri("/character/3")
        ]
    })

@app.route(app.helper.path('/characters/<id>'))
def get_character(id):
    return jsonify({
        'character': {
            'id': app.helper.uri('/characters/'+id),
            'sheet': character.Character().sheet
        }
    })

if __name__ == "__main__":
    app.run()
'''Cypher character generator for custom settings

Present a website and API which allows GMs for the Cypher System RPG 
to create settings, that players can then use to create Level 1 
characters.
'''

import os
from flask import Flask, jsonify, request
from . import helper, character, game

app = Flask(__name__)
app.config.from_mapping(
    DBCONN=os.environ.get('DBCONN'),
    BASEURI=os.environ.get('BASEURI', ''),
    APIPATH=os.environ.get('APIPATH', '/api/v1')
)
app.helper = helper.Helper(app)


@app.route(app.helper.path('/games', methods=['POST', 'GET']))
def get_games():
    if request.method == 'POST':
        g = game.Game()
        g.sheet = request.get_json(force=True)  # TODO validation
        g.save()

    elif request.method == 'GET':
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
            'campaign': game.Game().setting
        }
    })


@app.route(app.helper.path('/characters', methods=['POST', 'GET']))
def get_characters():
    if request.method == 'POST':
        c = character.Character()
        c.sheet = request.get_json(force=True)  # TODO validation
        c.save()

    elif request.method == 'GET':
        return jsonify({
            'characters': [
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

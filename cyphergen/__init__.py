'''Cypher character generator for custom settings

Present a website and API which allows GMs for the Cypher System RPG 
to create settings, that players can then use to create Level 1 
characters.
'''

import os
import logging
from flask import Flask, jsonify, request, make_response
from . import helper, character, game

app = Flask(__name__)
app.config.from_mapping(
    DBCONN=os.environ.get('DBCONN'),
    BASEURI=os.environ.get('BASEURI', ''),
    APIPATH=os.environ.get('APIPATH', '/api/v1')
)
app.helper = helper.Helper(app)


@app.route(app.helper.path('/games'), methods=['POST'])
def get_games():
    g = None
    try:
        g = game.Game(**request.get_json(force=True))
        g.save()
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to save object'
        }), 500)
    return make_response(app.helper.uri('/games/%s' % g.id), 201)


@app.route(app.helper.path('/games/<id>'))
def get_game(id):
    try:
        return jsonify({
            'id': app.helper.uri('/games/'+id),
            'campaign': game.Game(id=id).setting
        })
    except KeyError:
        return make_response('', 404)
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to lookup object'
        }), 500)


@app.route(app.helper.path('/characters'), methods=['POST'])
def get_characters():
    c = None
    try:
        c = character.Character(**request.get_json(force=True))
        c.save()
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to save object'
        }), 500)
    return make_response(app.helper.uri('/characters/%s' % c.id), 201)


@app.route(app.helper.path('/characters/<id>'))
def get_character(id):
    try:
        return jsonify({
            'id': app.helper.uri('/characters/'+id),
            'sheet': character.Character(id=id).sheet
        })
    except KeyError:
        return make_response('', 404)
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to lookup object'
        }), 500)


if __name__ == "__main__":
    app.run()

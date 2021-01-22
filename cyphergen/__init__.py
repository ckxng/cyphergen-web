'''Cypher character generator for custom settings

Present a website and API which allows GMs for the Cypher System RPG 
to create settings, that players can then use to create Level 1 
characters.
'''

import os
import logging
from flask import Flask, jsonify, request, make_response, render_template, redirect
from . import helper, character, game

app = Flask(__name__)
app.config.from_mapping(
    DBCONN=os.environ.get('DBCONN'),
    BASEURI=os.environ.get('BASEURI', ''),
    APIPATH='/api/v1'
)
app.helper = helper.Helper(app)


@app.route('/')
def html_index():
    return render_template('index.html')


@app.route('/generate/<id>/')
def html_generate(id):
    try:
        return render_template('generate.html', setting=game.Game(id=id).setting)
    except KeyError:
        return make_response(render_template('404.html'), 404)
    except Exception as e:
        app.logger.error(e)
        return make_response(render_template('500.html'), 500)


@app.route('/character/<id>/')
def html_character_lookup(id):
    try:
        return render_template('character.html', sheet=character.Character(id=id).sheet)
    except KeyError:
        return make_response(render_template('404.html'), 404)
    except Exception as e:
        app.logger.error(e)
        return make_response(render_template('500.html'), 500)


@app.route(app.helper.apipath('/games'), methods=['POST'])
def post_games():
    '''create a new game setting

    data:
    JSON(str)  a character to pass to Character()

    required headers:
    Content-Type: application/json
    '''
    g = None
    try:
        g = game.Game(**request.get_json())
        g.save()
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to save object'
        }), 500)
    return make_response(jsonify({
        'id': g.id,
        'api': app.helper.apiuri("/games/%s" % g.id),
        'web': app.helper.uri("/generate/%s" % g.id)
    }), 201)


@app.route(app.helper.apipath('/games/<id>'))
def get_game(id):
    try:
        return jsonify({
            'id': id,
            'api': app.helper.apiuri('/games/'+id),
            'web': app.helper.uri('/generate/'+id),
            'campaign': game.Game(id=id).setting
        })
    except KeyError:
        return make_response('', 404)
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to lookup object'
        }), 500)


@app.route(app.helper.apipath('/characters'), methods=['POST'])
def post_characters():
    '''create a new character

    data:
    JSON(str)  a character to pass to Character()

    required headers:
    Content-Type: application/json
    '''
    c = None
    try:
        c = character.Character(**request.get_json())
        c.save()
    except Exception as e:
        app.logger.error(e)
        return make_response(jsonify({
            'error': 'Failed to save object'
        }), 500)
    return make_response(jsonify({
        'id': c.id,
        'api': app.helper.apiuri("/characters/%s" % c.id),
        'web': app.helper.uri("/character/%s" % c.id)
    }), 201)


@app.route(app.helper.apipath('/characters/<id>'))
def get_character(id):
    try:
        return jsonify({
            'id': id,
            'api': app.helper.apiuri('/characters/'+id),
            'web': app.helper.uri('/character/'+id),
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

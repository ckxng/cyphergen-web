'''A game setting in the Cypher System

Represents the model and associated helper functions for 
characters and character sheets.
'''

import os
import redis
import json
import uuid

r = redis.from_url(os.environ.get('REDIS_URL'))

class Game(object):
    '''A game setting in the Cypher System

    Data is stored in self.setting, in exactly the format that matches
    the document database and YAML export formats.
    '''

    def __init__(self, **kw):
        '''Create a game setting

        If id is specified, attempt to load the object stored with that id.
        If the load was sucessful, the object is populated with the stored
        data.  If the load was unsucessful, Exception('Not Found') is raised.
        
        If id is not specified, populate the object with the following 
        parameters or a default if not specified.

        Parameters:
        id(str): UUID
        name(str): Setting name
        types(dict): Types available in the setting
        abilities(dict): Abilities available in the setting
        skills(list): List of the skills available in the setting

        Raises:
        Exception('Not Found') if id is specified and the object is not found

        Use optional keyword parameters to set values in self.sheet.
        '''

        if 'id' in kw:
            self.load(kw['id'])
        else:
            self.id = uuid.uuid4()
            self.setting = {}
            self.setting['name'] = kw.get('name', 'Name')

            #types = {
            #    'Name': {
            #        'pools': { #remap names for pools
            #            'might': 'Might',
            #            'speed': 'Speed',
            #            'intellect': 'Intellect'
            #        },
            #        'base_points': { #base points for pools
            #            'might': 8,
            #            'speed': 8,
            #            'intellect': 8
            #        },
            #        'add_points': 6, #additional points
            #        'edge': {
            #            'might': 1,
            #            'speed': 0,
            #            'intellect': 0
            #        },
            #        'add_edge': 0,
            #        'base_skills': {
            #            'Name': 1 #-1=inability, 1=trained, 2=specialized
            #        },
            #        'add_skills': 0,
            #        'cyphers': 2, #number held
            #        'base_abilities': [
            #            'Name'
            #        ],
            #        'add_abilities': 3 #additional abilities
            #    }
            #}
            self.setting['types'] = kw.get('types', {})

            #abilities = {
            #    'Name': {
            #        'description': "...",
            #        'enabler': 0, #1 if enabler, else 0
            #        'cost': {
            #            'might': 1
            #        } # {} if no cost
            #    }
            #}
            self.setting['abilities'] = kw.get('abilities', {})

            #skills = ['Speed Defense', 'Archery', 'Hacking']
            self.setting['skills'] = kw.get('skills', [])

    def save(self):
        '''
        Save the object
        '''
        r.set('Game/%s'%self.id, json.dumps(self.sheet))
    
    def load(self, id):
        '''
        Load the object with id

        Parameters:
        id(str): UUID

        Raises:
        Exception('Not Found') if the object is not found
        '''
        sheet = json.loads(r.get('Game/%s'%id))
        if sheet:
            self.sheet = sheet
        else:
            raise Exception('Not Found')

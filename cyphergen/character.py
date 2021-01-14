'''A character in the Cypher System

Represents the model and associated helper functions for 
characters and character sheets.
'''

import os
import redis
import json
import uuid

r = redis.from_url(os.environ.get('REDIS_URL'))


class Character(object):
    '''A character in the Cypher System

    Data is stored in self.sheet, in exactly the format that matches
    the document database and YAML export formats.
    '''

    def __init__(self, **kw):
        '''Create a character

        If id is specified, attempt to load the object stored with that id.
        If the load was sucessful, the object is populated with the stored
        data.  If the load was unsucessful, Exception('Not Found') is raised.

        If id is not specified, populate the object with the following 
        parameters or a default if not specified.

        Parameters:
        id(str): UUID
        name(str): Charater name
        type(str): Type name
        tier(int): Tier (1-6)
        effort(int): Effort (1-6)
        edge(dict): Edge {'might':(1-6), 'speed':(1-6), 'intellect':(1-6)}
        might(int): Points in might pool
        speed(int): Points in speed pool
        intellect(int): Points in intellect pool
        armor(int): Armor
        abilities(list): List of ability names
        equipment(list): List of equipment item names

        Raises:
        Exception('Not Found') if id is specified and the object is not found

        Returns:
        Character
        '''

        if 'id' in kw:
            self.load(kw['id'])
        else:
            self.id = uuid.uuid4()
            self.sheet = {}
            self.sheet['name'] = str(kw.get('name', 'Name'))
            self.sheet['type'] = str(kw.get('type', 'Type'))
            self.sheet['tier'] = int(kw.get('tier', 1))
            self.sheet['effort'] = int(kw.get('effort', 1))
            edge = kw.get('edge', {})
            self.sheet['edge'] = {}
            self.sheet['edge']['might'] = int(edge.get('might', 0))
            self.sheet['edge']['speed'] = int(edge.get('speed', 0))
            self.sheet['edge']['intellect'] = int(edge.get('intellect', 0))
            self.sheet['might'] = int(kw.get('might', 0))
            self.sheet['speed'] = int(kw.get('speed', 0))
            self.sheet['intellect'] = int(kw.get('intellect', 0))
            self.sheet['armor'] = int(kw.get('armor', 0))
            abilities = kw.get('abilities', [])
            self.sheet['abilities'] = []
            for ability in abilities:
                self.sheet['abilities'].append(str(ability))
            self.sheet['abilities'] = kw.get('abilities', [])
            equipment = kw.get('equipment', [])
            self.sheet['equipment'] = []
            for item in equipment:
                self.sheet['equipment'].append(str(item))

    def save(self):
        '''
        Save the object
        '''
        r.set('Character/%s' % self.id, json.dumps(self.sheet))

    def load(self, id):
        '''
        Load the object with id

        Parameters:
        id(str): UUID

        Raises:
        Exception('Not Found') if the object is not found
        '''
        sheet = json.loads(r.get('Character/%s' % id))
        if sheet:
            self.sheet = sheet
        else:
            raise Exception('Not Found')

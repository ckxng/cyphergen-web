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
        pools(dict): Mapping for pool names
        types(dict): Types available in the setting
        abilities(dict): Abilities available in the setting
        skills(list): List of the skills available in the setting

        Raises:
        KeyError if id is specified and the object is not found

        Use optional keyword parameters to set values in self.sheet.
        '''

        if 'id' in kw:
            self.load(kw['id'])
        else:
            self.id = uuid.uuid4()
            self.setting = {}
            self.setting['name'] = str(kw.get('name', 'Name'))

            # 'pools': {
            #     'might': 'Might',
            #     'speed': 'Speed',
            #     'intellect': 'Intellect'
            # },
            # pools
            self.setting['pools'] = {}
            pools = kw.get('pools', {})
            self.setting['pools'] = {}
            self.setting['pools']['might'] = str(
                pools.get('might', 'Might'))
            self.setting['pools']['speed'] = str(
                pools.get('speed', 'Speed'))
            self.setting['pools']['intellect'] = str(
                pools.get('intellect', 'Intellect'))

            # types = {
            #    'Name': {
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
            # }
            types = kw.get('types', {})
            self.setting['types'] = {}
            for type in types.keys():
                self.setting['types'][type] = {}

                # base_points
                base_points = types[type].get('base_points', {})
                self.setting['types'][type]['base_points'] = {}
                self.setting['types'][type]['base_points']['might'] = int(
                    base_points.get('might', 0))
                self.setting['types'][type]['base_points']['speed'] = int(
                    base_points.get('speed', 0))
                self.setting['types'][type]['base_points']['intellect'] = int(
                    base_points.get('intellect', 0))

                # add_points
                self.setting['types'][type]['add_points'] = int(
                    types[type].get('add_points', 0))

                # edge
                edge = types[type].get('edge', {})
                self.setting['types'][type]['edge'] = {}
                self.setting['types'][type]['edge']['might'] = int(
                    edge.get('might', 0))
                self.setting['types'][type]['edge']['speed'] = int(
                    edge.get('speed', 0))
                self.setting['types'][type]['edge']['intellect'] = int(
                    edge.get('intellect', 0))

                # add_edge
                self.setting['types'][type]['add_edge'] = int(
                    types[type].get('add_edge', 0))

                # base_skills
                base_skills = types[type].get('base_skills', [])
                self.setting['types'][type]['base_skills'] = []
                for skill in base_skills:
                    self.setting['types'][type]['base_skills'].append(
                        str(skill))

                # add_skills
                self.setting['types'][type]['add_skills'] = int(
                    types[type].get('add_skills', 0))

                # cyphers
                self.setting['types'][type]['cyphers'] = int(
                    types[type].get('cyphers', 0))

                # base_abilities
                base_abilities = types[type].get('base_abilities', [])
                self.setting['types'][type]['base_abilities'] = []
                for ability in base_abilities:
                    self.setting['types'][type]['base_abilities'].append(
                        str(ability))

                # add_abilities
                self.setting['types'][type]['add_abilities'] = int(
                    types[type].get('add_abilities', 0))

            # abilities = {
            #    'Name': {
            #        'description': "...",
            #        'enabler': 0, #1 if enabler, else 0
            #        'cost': {
            #            'might': 1
            #        } # {} if no cost
            #    }
            # }
            abilities = kw.get('abilities', {})
            self.setting['abilities'] = {}
            for ability in abilities.keys():
                self.setting['abilities'][ability] = {}

                # description
                self.setting['abilities'][ability]['description'] = str(
                    abilities[ability].get('description', ''))

                # enabler
                enabler = int(abilities[ability].get('enabler', 0))
                if enabler == 0 or enabler == 1:
                    self.setting['abilities'][ability]['enabler'] = enabler

                # cost
                cost = abilities[ability].get('cost', {})
                self.setting['abilities'][ability]['cost'] = {}
                for pool in cost.keys():
                    self.setting['abilities'][ability]['cost'][pool] = int(
                        cost[pool])

            #skills = ['Speed Defense', 'Archery', 'Hacking']
            skills = kw.get('skills', [])
            self.setting['skills'] = []
            for skill in skills:
                self.setting['skills'].append(str(skill))

    def save(self):
        '''
        Save the object
        '''
        r.set('Game/%s' % self.id, json.dumps(self.setting))

    def load(self, id):
        '''
        Load the object with id

        Parameters:
        id(str): UUID

        Raises:
        KeyError if the object is not found
        '''
        setting = json.loads(r.get('Game/%s' % id))
        if setting:
            self.setting = setting
        else:
            raise KeyError()

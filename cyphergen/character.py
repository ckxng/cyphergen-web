'''A character in the Cypher System

Represents the model and associated helper functions for 
characters and character sheets.
'''

class Character(object):
    '''A character in the Cypher System

    Data is stored in self.sheet, in exactly the format that matches
    the document database and YAML export formats.
    '''

    def __init__(self, **kw):
        '''Create a character

        Parameters:
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

        Returns:
        Character
        '''
        
        self.sheet = {}
        self.sheet['name'] = kw.get('name', 'Name')
        self.sheet['type'] = kw.get('type', 'Type')
        self.sheet['tier'] = kw.get('tier', 1)
        self.sheet['effort'] = kw.get('effort', 1)
        self.sheet['edge'] = kw.get('edge', {
            'might': 0,
            'speed': 0,
            'intellect': 0
        })
        self.sheet['might'] = kw.get('might', 0)
        self.sheet['speed'] = kw.get('speed', 0)
        self.sheet['intellect'] = kw.get('intellect', 0)
        self.sheet['armor'] = kw.get('armor', 0)
        self.sheet['abilities'] = kw.get('abilities', [])
        self.sheet['equipment'] = kw.get('equipment', [])

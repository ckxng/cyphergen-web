
class Game(object):
    def __init__(self, **kw):
        self.campaign = {}
        self.campaign['name'] = kw.get('name', 'Name')

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
        self.campaign['types'] = kw.get('types', {})

        #abilities = {
        #    'Name': {
        #        'description': "...",
        #        'enabler': 0, #1 if enabler, else 0
        #        'cost': {
        #            'might': 1
        #        } # {} if no cost
        #    }
        #}
        self.campaign['abilities'] = kw.get('abilities', {})

        #skills = ['Speed Defense', 'Archery', 'Hacking']
        self.campaign['skills'] = kw.get('skills', [])


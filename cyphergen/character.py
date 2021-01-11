
class Character(object):
    def __init__(self, **kw):
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



def normalizePosition(pos):
    d = {
        'SG':'Guard',
        'PG':'Guard',
        'G':'Guard',
        'SF':'Forward',
        'PF':'Forward',
        'C':'Center',
        'Guard-Forward':'Guard',
        'Forward-Guard':'Forward',
        'Forward-Center':'Forward',
        'Point Guard':'Guard',
        'Shooting Guard':'Guard',
        'Small Forward':'Forward',
        'Power Forward': 'Forward',
        'Center-Forward':'Center',
        'RP' : 'None',
        'TE' : 'None',
        '':'Unknown'
    }
    if pos in d:
        return d[pos]
    return pos

class Player(object):
    boxScore = {}
    advanced = {}
    shotCharts = {}
    fourFactors = {}
    misc = {}
    usage = {}
    def addBoxScore(self,d):
        self.boxScore = d
    def addAdvanced(self,d):
        self.advanced = d
    def addShotCharts(self,d):
        self.shotCharts = d
    def addFourFactor(self,d):
        self.fourFactors = d
    def addMisc(self,d):
        self.misc = d
    def addUsage(self,d):
        self.usage = d
    def toString(self):
        s = str(self.id) + '\nNAME:' + self.name + '\nPOS:' + self.position + \
            '\nDK_POS:' + self.dk_position + '\nDK_ID:' + self.dk_id + '\n'
        return s
    def getPosition(self):
        pos = self.position
        if len(pos) == 0:
            pos = self.dk_position
        return normalizePosition(pos)
    def __init__(self,d):
        self.id = int(d['id'])
        self.team_id = int(d['team_id'])
        self.first = d['first_name']
        self.last = d['last_name']
        self.name = self.first + ' ' + self.last
        self.birth = d['birth_date']
        self.position = d['position']
        self.dk_position = d['dk_position']
        self.dk_id = d['dk_id']
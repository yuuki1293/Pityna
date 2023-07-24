import re
import random

class PatternItem:
    SEPARATOR = '^((-?\d+)##)?(.*)$'

    def __init__(self, pattern, phrases):
        self.initModifyAndPattern(pattern)
        self.initPhrases(phrases)

    def initModifyAndPattern(self, pattern):
        m = re.findall(PatternItem.SEPARATOR, pattern)
        self.modify = 0
        if m[0][1]:
            self.modify = int(m[0][1])
        self.pattern = m[0][2]

    def initPhrases(self, phrases):
        self.phrases = []
        dic = {}
        for phrase in phrases.split('|'):
            m = re.findall(PatternItem.SEPARATOR, phrase)
            dic['need'] = 0
            if m[0][1]:
                dic['need'] = int(m[0][1])
            dic['phrase'] = m[0][2]
            self.phrases.append(dic.copy())

    def match(self, str):
        return re.search(self.pattern, str)

    def choice(self, mood):
        choices = []
        for p in self.phrases:
            if(self.suitable(p['need'], mood)):
                choices.append(p['phrase'])

        if(len(choices) == 0):
            return None
        return random.choice(choices)

    def suitable(self, need, mood):
        if(need == 0):
            return True
        elif (need > 0):
            return (mood > need)
        else:
            return (mood < need)
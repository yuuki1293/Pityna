import responder
import random
import dictionary
from io import TextIOWrapper


class Pityna(object):
    def __init__(self, name):
        self.name = name
        self.dictionary = dictionary.Dictionary()
        self.emotion = Emotion(self.dictionary.pattern)
        self.res_random = responder.RandomResponder(
            'Random', self.dictionary.random)
        self.res_repeat = responder.RepeatResponder('Repeat?')
        self.res_pattern = responder.PatternResponder(
            'Pattern', self.dictionary)

        self.count = 0
        self.fp = open("emotion.csv", mode='w')
        log_init(self.fp)

    def dialogue(self, input):
        self.emotion.update(input)

        self.count += 1
        log_emotion(self.count, self.emotion, self.fp)

        self.responder = self.res_pattern

        resp = self.responder.response(input, self.emotion.mood)
        self.dictionary.study(input)
        return resp
    
    def save(self):
        self.dictionary.save()

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name


class Emotion:
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5

    def __init__(self, pattern):
        self.pattern = pattern
        self.mood = 0

    def update(self, input):
        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY

        for ptn_item in self.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break

    def adjust_mood(self, val):
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN


def log_init(fp: TextIOWrapper) -> None:
    fp.write("会話回数,機嫌値\n")


def log_emotion(count: int, emotion: Emotion, fp: TextIOWrapper) -> None:
    fp.write(str(count))
    fp.write(",")
    fp.write(str(emotion.mood))
    fp.write("\n")

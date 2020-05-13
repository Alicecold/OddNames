
from random import randint
from random import sample

class NameGenerator:
    name = ""

    repeatableConsonants = "bdfgklmnprst"
    vowels = "aeiou"
    unrepeatableConsonants = "chvwjzy"
    consonants = repeatableConsonants + unrepeatableConsonants

    acceptableJoins= ["ch", "ck", "mn", "nd", "ng", "sp", "rt", "rk", "sk", "rs", "ls", "ns", "rn", "kt"]

    def beginsWithVowel(self):
        x = randint(0, 2)
        if x == 0:
            return True
        elif x == 1:
            return False
    
    def numberOfSyllables(self):
        rand = randint(0,20)
        if rand % 2 == 0:
            return 2
        elif rand % 3 == 0:
            return 3
        elif rand % 5 == 0:
            return 4
        elif rand % 7 == 0:
            return 1
        return 3
    
    def consonantShouldRepeat(self, consonant):
        if consonant in self.repeatableConsonants:
            repeat = randint(0,10)
            if repeat > 5:
                return True
        return False
    
    def consonantJoin(self, consonant):
        acceptable = sample(self.acceptableJoins, len(self.acceptableJoins))
        for join in acceptable:
            if consonant in join:
                return join
        return consonant
    
    def endsWithConsonant(self):
        repeat = randint(0,10)
        if repeat > 6:
            return True
        return False
    
    def consonantRepeated(self, consonant):
        if self.endsWithConsonant(): #Temp Hack for randomizer
            consonant = self.consonantJoin(consonant)
        elif self.consonantShouldRepeat(consonant):
            consonant += consonant
        return consonant
    
    
    def constructSyllable(self, isStart, isEnd):
        vowelIndex = randint(0,len(self.vowels)-1)
        vowel = self.vowels[vowelIndex]
        consonantIndex = randint(0,len(self.consonants)-1)
        consonant = self.consonants[consonantIndex]
        if isStart:
            if self.beginsWithVowel():
                return vowel
        elif isEnd:
            if self.endsWithConsonant():
                return self.consonantRepeated(consonant) # This makes it more likely with one syllable names than intended, but I kind of like it better
        else:
            consonant = self.consonantRepeated(consonant)
        return consonant + vowel

    def generate(self):
        isStart = True
        num = self.numberOfSyllables()
        name = ""
        for i in range(num):
            isEnd = i == num - 1
            name += self.constructSyllable(isStart, isEnd)
            isStart = False
            if isEnd and len(name) == 1:
                name += self.constructSyllable(isStart, isEnd)
        return name.capitalize()
    
    def __init__(self):
        self.name = self.generate()
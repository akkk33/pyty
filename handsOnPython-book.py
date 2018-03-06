#! /usr/bin/env python3
letterFormat = '''
I'v a giraffe , and I told it to stay {animal}
but it didn't
so What should I do now ??!!

'''
'''
What is this ?
'''
def readLetter():
    userPicks = dict()
    addPick('animal', userPicks)
    letter = letterFormat.format(**userPicks)
    print(letter)
def addPick(cue, dictionary):
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response
readLetter()
input('Press enter to terminate.')
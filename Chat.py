# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2015 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.
from __future__ import print_function

DEBUG = True

import re
import random
from nltk import compat, corpus
import sys
import os
from subprocess import *
import urllib

import speech_recognition as sr
import warnings
import math
import time

warnings.filterwarnings("ignore")

reflections = {
  "gryffindor" : "griffin door",
  "slytherin"  : "sliderin",
  "ravenclaw"  : "raven claw",
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    str.lower())

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            response = response[:pos] + \
                self._substitute(match.group(num)) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        num_pairs = len(self._pairs)

        # check each pattern
        for idx, (pattern, response) in enumerate(self._pairs):
            match = pattern.match(str)

            # did the pattern match?
            if match:
                selection = random.randint(0, len(response) - 1)
                resp = response[selection]   # pick a random response

                if 'GRYFFINDOR' in resp:
                    house = 1
                    resp = resp.replace('GRYFFINDOR', 'GRIFFIN DOOR')
                elif 'SLYTHERIN' in resp:
                    house = 2
                    resp = resp.replace('SLYTHERIN', 'SLIDERIN')
                elif 'HUFFLEPUFF' in resp:
                    house = 3
                elif 'RAVENCLAW' in resp:
                    house = 4
                    resp = resp.replace('RAVENCLAW', 'RAVEN CLAW')
                else:
                    house = 0

                resp = self._wildcards(resp, match) # process wildcards

                if idx == num_pairs - 1 or idx == 0:
                    selection += 2
                else:
                    selection = 0

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'

                

                return selection, resp, house

    # Hold a conversation with a chatbot

    def converse(self, quit="quit"):

        input = ""

        # obtain audio from the microphone
        r = sr.Recognizer()
        m = sr.Microphone()
        entries = corpus.cmudict.entries()

        while input != quit:
            input = ""

            with m as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            # try recognize speech using Google Speech Recognition
            try:
                input = r.recognize_google(audio)
            except sr.UnknownValueError:
                output = [1, "I couldn't understand that. Pipe up little one.", 0]
                input = ""
            except sr.RequestError as e:
                output = [1, "Looks like I'm having some technical issues.", 0]
                input = ""

            # parsed valid input from speech recognition
            # generate output for the hat
            if input:
                while input[-1] in "!.": input = input[:-1]
                if DEBUG:
                    print(input)
                index, output_text, house = self.respond(input)
                

                # index=phrase, output_text=speech, house=
                output = [index, output_text, house]

            

            # hat output
            if DEBUG:
                print(output)
                Popen(['say', '"' + output[1] + '"']).communicate()
            else:
                call('python speak.py \"' + output[1] + '\" ' + str(output[0]) + ' ' + str(output[2]) + ' ' + str(0), shell=True)
                print('say \"' + str(output[1]) + '\"')
                call('say \"' + str(output[1]) + '\"', shell=True)
                time.sleep(2)



import os
import time
import string
import random
import subprocess as sp

# Playback imports
from pydub import AudioSegment
from pydub.playback import play

def playResponse(responsePath):
    song = AudioSegment.from_wav(responsePath)
    play(song+18)
    os.remove(responsePath)
    print("[*] Played response")


class SDK:
    def __init__(self, core):
        self.core = core

    def say(self, text):
        playResponse(self.core.speaker.say(text))

    def openBrowser(self, url=None):
        if url:
            sp.Popen(str(self.core.config["browserRun"] + " " + url).split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=False)
            return
        sp.Popen(self.core.config["browserRun"].split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=False)
    
    def closeBrowser(self):
        sp.Popen(str("pkill "+self.core.config["browserRun"].split()[0]).split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=False)

    def openSystemMonitor(self):
        sp.Popen(str(self.core.config["terminalRun"]+" -e htop").split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=False)

    def closeSystemMonitor(self):
        sp.Popen(["pkill","htop"], stdout=sp.PIPE, stderr=sp.STDOUT, text=False)

    def shutUp(self):
        sp.Popen(["pkill","vlc"], stdout=sp.PIPE, stderr=sp.STDOUT, text=False)

    def engoogle(self, text):
        sp.Popen(str(self.core.config["browserRun"] + " https://www.google.com/search?q=" + text.replace(" ", "+")).split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=False)
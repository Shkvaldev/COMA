# Default imports
import os
import json
import time
from pprint import pprint

# Playback imports
from pydub import AudioSegment
from pydub.playback import play

# Project's imports
from Speaker.main import Speaker
from Recognizer.main import Recognizer
from ModulesParser.main import ModulesParser
from API.main import API
from TGBot.main import TGBot


def importConfig(confPath):
    with open(confPath, "r") as config:
        config_data = json.loads(config.read())
        config.close()
        return config_data
'''
def playResponse(response):
    song = AudioSegment.from_wav(response)
    play(song+18)
    os.remove(response)
    print("[*] Played response")
'''
class COMA:
    def __init__(self, configPath):
        self.config = importConfig(configPath)
        print("[*] Config loading ...")
        pprint(self.config)
        print("[*] Speaker loading ...")
        self.speaker = Speaker(self)
        print("[*] Recognizer loading ...")
        self.recognizer = Recognizer(self)
        print("[*] API loading ...")
        self.api = API(self)
        print("[*] ModulesParser loading ...")
        self.modulesParser = ModulesParser(self)
        print("[*] TGBot loading ...")
        self.bot = TGBot(self)
        self.bot.run()
        #playResponse(self.speaker.say("Привет, Хозяин!"))
    
    def playResponse(response):
        song = AudioSegment.from_wav(response)
        play(song+18)
        os.remove(response)
        print("[*] Played response")

if __name__ == "__main__":
    COMA("config.json")
    os.system("rm -rf */__pycache__")

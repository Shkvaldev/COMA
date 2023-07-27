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
from SDK.main import SDK


def importConfig(confPath):
    with open(confPath, "r") as config:
        config_data = json.loads(config.read())
        config.close()
        return config_data

class COMA:
    def __init__(self, configPath):
        self.config = importConfig(configPath)
        print("[*] Config loading ...")
        pprint(self.config)

        print("[*] Speaker loading ...")
        self.speaker = Speaker(self)

        print("[*] Recognizer loading ...")
        self.recognizer = Recognizer(self)

        print("[*] SDK loading ...")
        self.sdk = SDK(self)

        print("[*] ModulesParser loading ...")
        self.modulesParser = ModulesParser(self)

        if self.config["useTelegram"]:

            from TGBot.main import TGBot

            print("[*] TGBot loading ...")
            self.bot = TGBot(self)
            self.bot.run()
        else:

            from LocalAPI.main import LocalAPI

            print("[*] LocalAPI loading ...")
            self.localAPI = LocalAPI(self)

            try:
                self.localAPI.run()
            except KeyboardInterrupt:
                del(self)
    
    def playResponse(responsePath):
        song = AudioSegment.from_wav(responsePath)
        play(song+18)
        os.remove(responsePath)
        print("[*] Played response")

if __name__ == "__main__":
    COMA("config.json")
    os.system("rm -rf */__pycache__")

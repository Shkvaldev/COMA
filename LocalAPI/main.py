import os
import time
import glob

class LocalAPI:
    def __init__(self, core):
        self.core = core
    
    # Checks if there is a user input by searching *.wav file in project's tmp dir
    def checkRequest(self):
        for request in glob.glob("tmp/*.wav"):
            answer = self.core.recognizer.recognize(request)
            self.core.modulesParser.handleModule(answer)
            os.remove(request)

    def run(self):
        while True:
            self.checkRequest()
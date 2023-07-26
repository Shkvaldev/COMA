import os
import time
import glob

import json

from pprint import pprint

class Action:
    def __init__(self, action, args):
        self.action = action
        self.args = args

    def perform(self, speech):
        try:
            currentArgs = []
            if self.args:
                for arg in self.args:
                    if "$speech" in arg:
                        currentArgs.append(arg.replace("$speech", speech))
                        continue
                    currentArgs.append(arg)
            else:
                self.action()
                return
            print(currentArgs)
            self.action(*currentArgs)
        except Exception as e:
            raise e

class ModulesParser:
    def __init__(self, core):
        self.core = core
        self.triggers = {}
        for modulePath in glob.glob("Modules/*/module.json"):
            self.parseModule(modulePath)

    def parseModule(self, modulePath):
        print(f"\t[*] Parsing module '{modulePath.split('/')[1]}' ...")
        with open(modulePath, "r") as module:
            moduleData = json.loads(module.read())
        for trigger, actions in moduleData["triggers"].items():
            self.triggers[trigger] = self.buildActionBundle(actions)
        pprint(self.triggers)
    
    def buildActionBundle(self, actions):
        actionBundle = []
        for action in actions:
            actionBundle.append(Action(getattr(self.core.api, action["apiFunc"]), action["args"]))
        return actionBundle

    # This method checks if there is trigger in speech and perform it if yes
    def handleModule(self, rawSpeechRecognized):
        for trigger in self.triggers.keys():
            if trigger in rawSpeechRecognized:
                self.performModule(trigger, rawSpeechRecognized.replace(trigger, ""))

    def performModule(self, trigger, speechRecognized):
        for action in self.triggers[trigger]:
            action.perform(speechRecognized)
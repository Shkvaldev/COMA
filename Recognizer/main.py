import os
import json
import subprocess as sp
from vosk import Model, KaldiRecognizer

class Recognizer:
    def __init__(self, core):
        self.core = core
        self.initModel()

    def initModel(self):
        try:
            modPath = os.path.join("Recognizer", "vosk_models", "RUS")
            if os.path.exists(modPath):
                self.model = KaldiRecognizer(Model(modPath), 16000)
                print("[*] Model has been loaded!")
            else:
                exit(f"[!] Language model not found! Exiting ...")
        except Exception as e:
            exit(e)

    def recognize(self, audioPath):
        try:
            with sp.Popen(['ffmpeg', '-loglevel', 'quiet', '-i', audioPath, '-ar', '16000', '-ac', '1', '-f', 's16le', '-'], stdout=sp.PIPE) as process:
                self.model.AcceptWaveform(process.stdout.read())
                os.remove(audioPath)
                return json.loads(self.model.FinalResult())["text"]
        except Exception as e:
            exit(e)

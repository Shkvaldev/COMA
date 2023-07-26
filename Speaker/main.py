import os
import time
import string
import random


class Speaker:
    def __init__(self, core):
        self.core = core

    def say(self, text):
        answer_name = time.strftime("%H%M%S")+"".join(random.choices(string.ascii_uppercase, k=10))
        os.system(f"echo '{text}' | RHVoice-test -p {self.core.config['voice']} -o {answer_name+'.wav'} -t {self.core.config['pitch']} -r {self.core.config['rate']}")
        return answer_name+'.wav'

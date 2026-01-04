import os
from helperFunctions import *

def stt_testing(file_name):
    print("The transcript from \'" + file_name + "\' is: " + speech_to_text(str(os.getcwd() + "/sample/" + file_name + ".wav")))

stt_testing("demo_2")
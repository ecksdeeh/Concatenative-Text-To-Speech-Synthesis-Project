'''The Concatenative Synthesis method of text to speech generation converts text to simple sounds(known as phonemes) and will join
the phonemes together in order to generate a human like speech. 
'''
import librosa #this will be used to process audio
import numpy as np
from nltk.tokenize import sent_tokenize

def load_wav(file_name):
    #loads wav file and returns waveform and sample rate
    audio, sr = librosa.load(file_name)
    return audio, sr
#adding silence between speech will help the speech seem more natural
def add_silence(audio, silence_duration):
    #adds a moment of silence to audio
    silence_length = int(silence_duration * sr / 1000)  #calculates duration based on sample rate
    silence = np.zeros(silence_length)
    return np.concatenate((silence, audio))
#next steps: using NLP to break down text(tokenization), looking for a database with phonemes for the algorithm to use, and more
#planning to possibly use the tokenization method that was used in a previous project
def tokenize_file(file_name):
    
    

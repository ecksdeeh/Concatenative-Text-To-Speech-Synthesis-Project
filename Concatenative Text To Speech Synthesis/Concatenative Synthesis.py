'''The Concatenative Synthesis method of text to speech generation converts text to simple sounds(known as phonemes) and will join
the phonemes together in order to generate a human like speech. 
'''
import librosa #this will be used to process audio
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize

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

def process_text(text):
    #processing text to make algorithm more efficient
    text_tokenize = word_tokenize(text)
def find_phoneme(phoneme, phoneme_data):
    #searches through dataset
    for entry in phoneme_data:
        if entry["phoneme"] == phoneme:
            return entry["audio_file"]
    return None #phoneme not found in data
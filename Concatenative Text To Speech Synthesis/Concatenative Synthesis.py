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
def synthesize_speech(text, phoneme_data, silence_ms=100):
    phonemes - process_text(text)
    concatenated_audio = None
    for phoneme in phonemes:
        audio_file = find_phoneme(phoneme, phoneme_data)
        if audio_file:
            phoneme_audio, _ = load_wav(audio_file)
            phoneme_audio = add_silence(phoneme_audio, silence_ms)
            if concatenated_audio is None:
                concatenated_audio = phoneme_audio
            else:
                concatenated_audio= np.concatenate((concatenated_audio, phoneme_audio))
    return concatenated_audio

text = "Hi"
synthesized_audio = synthesize_speech(text, find_phoneme)
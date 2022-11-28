from scipy.io.wavfile import write
import numpy as np
from playsound import playsound
    
import playing as play

samplerate = 44100

def main():
    # octave = 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'
    
    #Notes of "twinkle twinkle little star"
    #music_notes = 'F-F-E-E-D-D-C-F-F-E-E-D-D-C'
    music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
    #music_notes = 'C-D-C-G'
    data = play.get_song_data(music_notes)
    data = data * (16300/np.max(data))
    write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))
    
    #Playing chords
    #chords = 'EgB-DfA-AcE-BDf-gAcE-fAc'
    #data = play.get_chord_data(chords)
    #data = data * (16300/np.max(data))
    #data = np.resize(data, (len(data)*5,))
    #write('exp-C-Major.wav', samplerate, data.astype(np.int16))

    playsound('twinkle-twinkle.wav')
    
if __name__=='__main__':
    main()
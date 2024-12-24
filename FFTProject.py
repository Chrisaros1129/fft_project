from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import sys

from scipy.io import wavfile
from scipy.fft import fft, fftfreq

WAV_DIRECTORY = Path("C:/Users/ghost/OneDrive/Documents/Code Practice/Emily Python Lessons/fft_project/WAV_Files") ## Global variables typically upper case

# Double quotations typically used for strings or words or sentences.
# Single quotations are more for characters
# Can be interchangable

def load_audio_files(directory):
    # converts string of directory to a Path object
    # Get all .wav files in directory
    files = list(directory.glob('*.wav')) ## * is called wildcard
    return files
    

def process_audio_file(file):
    print(f"Processing: {file.name}") # f-string is what its called. It returned this: Processing: bellsTibetan.wav

    # load audio file
    sampling_rate, audio_data = wavfile.read(file)
    
    # sampling_rate, audio_data = wavefile.read(file) # It gave this warning: WavFileWarning: Chunk (non-data) not understood, skipping it.
    # Error is broken code, warning is like a flag for us to acknowledge something could be wrong in code. In our case we can ignore it.

    print("Sampling Rate: ", sampling_rate)
    print("Audio: ", audio_data)

    # Handling stereo by selecting one channel
    if len(audio_data.shape) > 1:
        audio_data = audio_data[:,0]
        print("Mono L: ",audio_data)
    return sampling_rate, audio_data

def audio_fft_time_data(audio_data,sampling_rate):
    # TIME

    # Normalize the data
    audio_data = audio_data / np.max(np.abs(audio_data), axis = 0)
    # Sampling points
    N = len(audio_data)
    # Spacing
    T = N/sampling_rate
    # Time array
    t = np.linspace(0., T, N)
    
    # FFT
    yf = fft(audio_data)
    xf = fftfreq(N, 1/sampling_rate)
    # Adjust to positive frequencies only
    xf = xf[:N//2]
    yf = np.abs(yf[:N//2])

    #PLOTS
    


    
   

    

    
    
    





def main():
    files = load_audio_files(WAV_DIRECTORY)
    if not files: # If files is empty. NOT is a boolean. 
        print("No .wav files found in the directory.")
        sys.exit()
    print(files)
    
    for file in files:
        print(f"Processing: {file}")
        sampling_rate, audio_data = process_audio_file(file)
        
        index = files.index(file)+1
        print(index)
        
        plt.figure(index,figsize=(10,4))
        plt.plot(t,audio_data)
        plt.title(f"Time Domain of {file.name}")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        audio_fft_time_data(audio_data)



    

if __name__ == "__main__":
    main()

    # directory 
    # C:\Users\ghost\OneDrive\Documents\Code Practice\Emily Python Lessons\fft_project\WAV_Files


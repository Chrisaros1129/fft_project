import pdb
import sys

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

import pdb


WAV_DIRECTORY = Path("C:/Users/ghost/OneDrive/Documents/Code Practice/Emily Python Lessons/fft_project/WAV_Files") ## Global variables typically upper case
SAVE_DIRECTORY = WAV_DIRECTORY.parent


#c to continue, n to next breakpoint, b (number) to set a breakpoint at line, q to quit pdb,
#pdb.set_trace() # <-- This is where python debugger starts

# Double quotations typically used for strings or words or sentences.
# Single quotations are more for characters
# Can be interchangable

def load_audio_files(directory: Path):
    '''Get all .wav files in directory and converts string of directory to a Path object directory = path type'''
    # 
    # Get all .wav files in directory
    files = list(directory.glob('*.wav')) ## * is called wildcard

    ## pdb.set_trace()
    return files
    

def process_audio_file(file: Path):
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

def audio_fft_time_data(audio_data: np.ndarray ,sampling_rate: int):
    '''returns array containing normalized audio, time, frequencies, and magnitude respectfully'''
    # TIME
    pdb.set_trace()

    # Normalize the data
    audio_data_norm = audio_data / np.max(np.abs(audio_data), axis = 0)
    print(f"Audio data after normalized {audio_data_norm}")
    # Sampling points
    N = len(audio_data)
    # Spacing
    T = N/sampling_rate
    # Time array
    t = np.linspace(0., T, N)
    
    # FFT
    yf = fft(audio_data_norm)
    xf = fftfreq(N, 1/sampling_rate)
    # Adjust to positive frequencies only
    xf = xf[:N//2]
    yf = np.abs(yf[:N//2])

    return audio_data_norm, t, xf, yf

#PLOTS

def plot_data(index: int, x: list, y: list, plot_title: str, x_label: str, y_label: str):
    '''Parameters: (index, x, y, plot_title, x_label, y_label)'''
    plt.figure(index,figsize=(6.4,4.8))
    plt.plot(x,y)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def main():
    files = load_audio_files(WAV_DIRECTORY)
    if not files: # If files is empty. NOT is a boolean. 
        print("No .wav files found in the directory.")
        sys.exit()
    
    for file in files:
        print(f"Processing: {file}")
        sampling_rate, audio_data = process_audio_file(file)
        index = files.index(file)+1
        print(index)
        audio_data_norm, t, xf, yf = audio_fft_time_data(audio_data,sampling_rate)
        plot_data(index, t, audio_data_norm, f"Time Domain of {file.name}","Time [s]","Amplitude")
        plt.savefig(SAVE_DIRECTORY/f"Time Domain of {file.name}.png")
        plt.show()
        plot_data(index, xf, yf, f"Frequency Domain of {file.name}", "Frequency [Hz]", "Magnitude")
        plt.savefig(SAVE_DIRECTORY/f"Frequency Domain of {file.name}.png")
        plt.show()

if __name__ == "__main__":
    main()

    # directory 
    # C:\Users\ghost\OneDrive\Documents\Code Practice\Emily Python Lessons\fft_project\WAV_Files
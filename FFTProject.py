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
    '''returns array containing normalized audio, time, frequencies, and magnitude respectfully'''
    # TIME

    # Normalize the data
    audio_data_n = audio_data / np.max(np.abs(audio_data), axis = 0)
    print(f"Audio data after normalized {audio_data_n}")
    # Sampling points
    N = len(audio_data)
    # Spacing
    T = N/sampling_rate
    # Time array
    t = np.linspace(0., T, N)
    
    # FFT
    yf = fft(audio_data_n)
    xf = fftfreq(N, 1/sampling_rate)
    # Adjust to positive frequencies only
    xf = xf[:N//2]
    yf = np.abs(yf[:N//2])

    return audio_data_n, t, xf, yf

#PLOTS

def plot_data(index,x,y,file,plot_title,x_label,y_label):
    '''Parameters: (index,x,y,file,plot_title,x_label,y_label)'''
    plt.figure(index,figsize=(10,4))
    plt.plot(x,y)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show()




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
        audio_data_n,t, xf, yf = audio_fft_time_data(audio_data,sampling_rate)
        plot_data(index,t,audio_data_n,file,f"Time Domain of {file.name}","Time [s]","Amplitude")
        plot_data(index,xf,yf,file,f"Frequency Domain of {file.name}","Frequency [Hz]","Magnitude")

if __name__ == "__main__":
    main()

    # directory 
    # C:\Users\ghost\OneDrive\Documents\Code Practice\Emily Python Lessons\fft_project\WAV_Files


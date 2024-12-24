from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

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
    if not files: # If files is empty. NOT is a boolean. 
        print("No .wav files found in the directory.")
        return
    # Process each file
    for file in files:
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

        ### Shortcut to comment out is ctrl and /
        
        # Normalize the data
        audio_data = audio_data / np.max(np.abs(audio_data))

        # Plotting Time Domain of File

        # Spacing
        T = len(audio_data)/sampling_rate

        # Sampling points
        N = len(audio_data)

        t = np.linspace(0., T, N)
        print(t)
        
        index = files.index(file)+1  # Try to get more WAV files and see what happens.
        print(index)

        plt.figure(index,figsize=(10,4))
        plt.plot(t,audio_data)
        plt.title(f"Time Domain of {file.name}")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")

        # Plotting FFT of File

        # We are attempting to only plot the positive frequency domain of the signal.

        audio_fft = fft(audio_data)
        freq = fftfreq(N, d=1/10000)
        print(len(audio_fft))
        print(len(freq))
        plt.figure(index+1,figsize=(10,4))
        plt.plot(freq,audio_fft)
        plt.title(f"Frequency Domain of {file.name}")
        plt.xlabel("Freq [Hz]")
        plt.ylabel("Magnitude")

        plt.show()  # From our experiment, we see that the loop waits for you to exit out the figure to proceed. Also the plt.show
                    # 

        # 1. Break this up into more functions
        # 2. Demonstrate making this into a module
        # 11/16/24



def main():
    load_audio_files(WAV_DIRECTORY)

if __name__ == "__main__":
    main()

    # directory 
    # C:\Users\ghost\OneDrive\Documents\Code Practice\Emily Python Lessons\fft_project\WAV_Files


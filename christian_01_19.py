import sys
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

WAV_DIRECTORY = Path("C:/Users/ghost/OneDrive/Documents/Code Practice/Emily Python Lessons/fft_project/WAV_Files")

def load_audio_files(directory):
    '''Get all .wav files in directory and converts string of directory to a Path object'''
    files = list(directory.glob('*.wav'))
    return files

def process_audio_file(file):
    '''Loads and returns audio file'''
    sampling_rate, audio_data = wavfile.read(file)

    # Handling stereo by selecting one channel
    if len(audio_data.shape) > 1:
        audio_data = audio_data[:, 0]

    return sampling_rate, audio_data

def audio_fft_time_data(audio_data: list , sampling_rate: list):
    '''Returns array containing normalized audio, time, frequencies, and magnitude respectfully'''
    # TIME
    # Normalize the data
    audio_data_norm = audio_data / np.max(np.abs(audio_data), axis = 0)
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

def plot_data(index, x, y, plot_title, x_label, y_label):
    '''Displays data. Parameters: (index, x, y, plot_title, x_label, y_label)'''
    plt.figure(index, figsize=(10, 4))
    plt.plot(x, y)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show()

def main():
    files = load_audio_files(WAV_DIRECTORY)
    
    if not files:
        print("No .wav files found in the directory.")
        sys.exit()
    
    for file in files:
        print(f"Processing: {file}")
        
        sampling_rate, audio_data = process_audio_file(file)
        index = files.index(file) + 1
        audio_data_norm, t, xf, yf = audio_fft_time_data(audio_data, sampling_rate)

        plot_data(index, t, audio_data_norm, f"Time Domain of {file.name}", "Time [s]", "Amplitude")
        plot_data(index, xf, yf, f"Frequency Domain of {file.name}", "Frequency [Hz]", "Magnitude")

if __name__ == "__main__":
    main()
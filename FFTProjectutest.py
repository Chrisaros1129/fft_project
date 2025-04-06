import FFTProject as fft
import numpy as np

from pathlib import Path

# Find a way to include sample data few terms. (numpy.ndarray type for audio_data, int is the type for sampling_rate)
# Include a global variable with some audio data, this will be input into fft.audio_fft_time_data and also an int for sampling rate
# Find ways to break program.

WAV_DIRECTORY = Path("C:/Users/ghost/OneDrive/Documents/Code Practice/Emily Python Lessons/fft_project/WAV_Files") ## Global variables typically upper case
SAVE_DIRECTORY = WAV_DIRECTORY.parent

# test NEEDS to be in front of functions actual name for the unit test to apply to it

def test_load_audio_files():
    fft.load_audio_files(WAV_DIRECTORY)

def test_process_audio_file():
    fft.process_audio_file(SAVE_DIRECTORY)

Sample_data = np.ndarray([1,2,3,4,5])
def test_audio_fft_time_data():
    fft.audio_fft_time_data(Sample_data)

# def test_plot_data(index: int, x: list, y: list, plot_title: str, x_label: str, y_label: str):
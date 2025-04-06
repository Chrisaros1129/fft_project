import FFTProject as fft
import numpy as np
import pdb

from pathlib import Path

# Find a way to include sample data few terms. (numpy.ndarray type for audio_data, int is the type for sampling_rate)
# Include a global variable with some audio data, this will be input into fft.audio_fft_time_data and also an int for sampling rate
# Find ways to break program.

WAV_DIRECTORY = Path("C:/Users/ghost/OneDrive/Documents/Code Practice/Emily Python Lessons/fft_project/WAV_Files") ## Global variables typically upper case
WAVFILE = WAV_DIRECTORY / "440Hz_44100Hz_16bit_05sec.wav"
audio_data_dummy = np.arange((21), dtype=np.float64)
pdb.set_trace()
audio_data_wav1 = np.array(([0, 1421, 2835, 4238, 5625, 6989, 8327, 9632, 10899, 12122, 13299, 14423, 15490, 16496, 17438, 18312, 19113, 19839, 20487, 21055]), dtype=np.float64)
audio_data_wav2 = np.array([11, -8, 5, -2, 1, -1, 2, -3, 4, -3, 1, 2, -5, 8, -9, 8, -5, 1, 4, -7], dtype=np.float64)
audio_data_wav3 = np.array([865, 953, 1037, 1101, 1153, 1191, 1223, 1244, 1254, 1255, 1247, 1232, 1228, 1228, 1235, 1241, 1248, 1254, 1258, 1247], dtype=np.float64)
audio_data_zeros = np.zeros((20,1), dtype=np.float64)
audio_data_empty = np.empty((20,1), dtype=np.float64)

audio_data = np.array([audio_data_dummy], [audio_data_wav1, audio_data_wav2, audio_data_wav3, audio_data_zeros, audio_data_empty])
pdb.set_trace()
sampling_rate = 44100
ind = 1

# test NEEDS to be in front of functions actual name for the unit test to apply to it
#pdb.set_trace()
def test_load_audio_files(): # This has to include test before, but can be called whatever
    fft.load_audio_files(WAV_DIRECTORY) # This HAS to include name of function in main script.

def test_process_audio_file():
    fft.process_audio_file(WAVFILE)

def test_audio_fft_time_data():
    fft.audio_fft_time_data(sample_data, sampling_rate)
    #fft.

def test_plot_data():
    fft.plot_data(ind,)



# def test_plot_data(index: int, x: list, y: list, plot_title: str, x_label: str, y_label: str):
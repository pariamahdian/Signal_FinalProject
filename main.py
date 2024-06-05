import numpy as np
import scipy.signal as signal
from scipy.io.wavfile import write

sampling_rate = 480_000


# Define the filtered frequencies
ava_freq = 96_000
eghtesad_freq = 144_000
goftogu_freq = 288_000
farhang_freq = 240_000

# Read the text file containing the signal data
signal_data = []
with open("signal_data.txt", "r") as file:
    for line in file:
        signal_data.append(float(line))

# Function to filter the signal using band-pass filter


def filter_signal(signal_data, low, high):
    low = low / sampling_rate
    high = high / sampling_rate
    b, a = signal.butter(2, [low, high], btype='band')
    filtered_signal = signal.lfilter(b, a, signal_data)
    return filtered_signal


# get a signal name from user


while True:
    inp = input("type the name of the signal: ")

# Filter and write the signal for each frequency
    if inp == "ava":

        filtered_signal_ava = filter_signal(
            signal_data, ava_freq-10000, ava_freq+10000)
        processed_signal_ava = np.real(np.fft.ifft(filtered_signal_ava))
        write("filtered_signal_ava.wav", sampling_rate, processed_signal_ava)
        break

    elif inp == "eghtesad":
        filtered_signal_eghtesad = filter_signal(
            signal_data, eghtesad_freq-10000, eghtesad_freq+10000)
        processed_signal_eghtesad = np.real(np.fft.ifft(filtered_signal_eghtesad))
        write("filtered_signal_eghtesad.wav", sampling_rate, processed_signal_eghtesad)
        break


    elif inp == "goftogu":
        filtered_signal_goftogu = filter_signal(
            signal_data, goftogu_freq-10000, goftogu_freq+10000)
        processed_signal_goftogu = np.real(np.fft.ifft(filtered_signal_goftogu))
        write("filtered_signal_goftogu.wav", sampling_rate, processed_signal_goftogu)
        break


    elif inp == "farhang":
        filtered_signal_farhang = filter_signal(
            signal_data, farhang_freq-10000, farhang_freq+10000)
        processed_signal_farhang = np.real(np.fft.ifft(filtered_signal_farhang))
        write("filtered_signal_farhang.wav", sampling_rate, processed_signal_farhang)
        break

    else:
        print("Oops! wrong input")
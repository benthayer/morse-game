import time
import numpy as np
from pycwgen import morse
import simpleaudio as sa

wpm = 35
SAMPLE_RATE = 44100


def convert32to16(raw32):
    if max(abs(raw32)) == 0:
        scaled32 = raw32
    else:
        scaled32 = raw32 * 32767 / max(abs(raw32))
    return scaled32.astype(np.int16)


def play_sample(text, sleep=False):
    wav32 = morse.generate_morse_code(text, wpm, normalize=False)
    wav16 = convert32to16(wav32)

    sound = sa.play_buffer(wav16, 1, 2, SAMPLE_RATE)

    if sleep:
        time.sleep(len(wav16)/SAMPLE_RATE)

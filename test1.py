import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
# import numpy as np
# import pandas as pd
import matlab.engine
# import io
# import numpy as np
# import midi
from scipy.io import wavfile
from feature2pred import get_pred
from predict import get_score


st.title('My first adsdspp')
# st.title(":musical_note: Convert a MIDI file to WAV")
#
uploaded_file = st.file_uploader("Upload MIDI file (you can fetch one on https://bitmidi.com/)", type=["wav"])
#st.write(type(uploaded_file))
#

if uploaded_file is None:
    st.info("Please upload a MIDI file")
    st.stop()

samplerate, data = wavfile.read(uploaded_file)
st.write(data.shape[0])

length = data.shape[0] / samplerate
st.write(f"length = {length}s")
# ui = wavfile.read(uploaded_file, mmap=False)
# st.write(type(ui))
# st.write(uploaded_file.getparams())
# midi_data = midi.PrettyMIDI(uploaded_file)
# audio_data = midi_data.fluidsynth()
# audio_data = np.int16(audio_data / np.max(np.abs(
#     audio_data)) * 32767 * 0.9)  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py
#
# virtualfile = io.BytesIO()
# wavfile.write(virtualfile, 44100, audio_data)
#
# st.audio(virtualfile)
# st.markdown("Download the audio by right-clicking on the media player")




# print('dada')
## matlab part
eng = matlab.engine.start_matlab()
resultt = eng.matlabp(7.7)
# print(resultt)
eng.quit()
pred = get_pred(resultt)
st.write(resultt)
st.write(pred)
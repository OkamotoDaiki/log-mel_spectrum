import soundfile
import mellogspec

fname = 'recordings/0_jackson_0.wav' #any wav file.
data, fs = soundfile.read(fname)
mellogspec_array, mel_scale = mellogspec.get_mellogspec(data, fs)
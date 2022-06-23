import soundfile
import logmelspec

fname = 'recordings/0_jackson_0.wav' #any wav file.
data, fs = soundfile.read(fname)
logmelspec_array, mel_scale = logmelspec.get_logmelspec(data, fs)
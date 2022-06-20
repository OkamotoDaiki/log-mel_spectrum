# mel-log spectrum
 
The function that extracts features of voice data by mel-log spectrum.

The definition of me-log spectrum is from the next paper
Deep Learning for Audio Signal Processing: https://arxiv.org/abs/1905.00078
 
# DEMO
 
This repository contains the generation of feature with mel-log spectrum. Comparing the mel-log spectrum with the logarithmic spectrum is as follows. The Mel scale emphasizes low frequencies.

![comparison_mel_Hz](https://user-images.githubusercontent.com/49944765/174479503-bb3fed4e-7dad-4839-a29a-db3f3b0d7ed4.png)

"""Machine Learning TEST"""<br>
The accuracy was about `93.1%` when the dataset of audio sample was as follows and output to Deep Learning of the machine learning algorithm.

* Name:  Jakobovski / Free Spoken Digit Dataset (FSDD)
* LICENCE: Creative Commons Attribution-ShareAlike 4.0 International
* Link: https://github.com/Jakobovski/free-spoken-digit-dataset

Please refer to the following repository for the above results.
* Link: https://github.com/OkamotoDaiki/mel-log-spec_DeepLearning_TEST

# Features

From mellogspec.py, you can get the data array of get_mellogspec() with the first return value. The data array of the mel frequency can be acquired with the second argument.
 
# Requirement

* Python 3.8.10
* numpy 1.21.4
 
# Installation
 
You can import it with the following program.
 
```python
import soundfile
import mellogspec

fname = 'recordings/0_jackson_0.wav' #any wav file.
data, fs = soundfile.read(fname)
mellogspec_array, mel_scale = mellogspec.get_mellogspec(data, fs)
```
 
# Usage
 
Refer to the sample program.

# Author
* Oka.D.
* okamotoschool2018@gmail.com

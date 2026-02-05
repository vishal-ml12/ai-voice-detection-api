import librosa
import numpy as np

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)
    pitch = np.mean(librosa.yin(y, fmin=50, fmax=300))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    spec_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    spec_bandwidth = np.mean(
        librosa.feature.spectral_bandwidth(y=y, sr=sr)
    )


    return np.hstack([mfcc, pitch, zcr, spec_centroid,spec_bandwidth])
    
